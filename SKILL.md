---
name: pymcnp
description: Use when creating, editing, scanning, checking, or running MCNP input files (.inp) from Python, reading MCNP output (OUTP, MESHTAL, PTRAC), validating an MCNP input's syntax, or when PyMCNP fails to parse a valid MCNP file or lacks a card/feature.
---

# PyMCNP

Python API and CLI for MCNP inputs and outputs (`pip install pymcnp`, Python 3.11-3.14). Working scripts live in `examples/` (`create_*.py`, `read_*.py`, `do_*.py`); copy from them.

## Parsing contract

`X.from_mcnp(text)` and `X.from_file(path)` return `(obj, remainder)`. Parsing stops silently at the first card it cannot parse; that card and everything after it is the `remainder`. **Always check `remainder == ''`**, otherwise part of the file was dropped. Unparseable input with nothing parseable raises `pymcnp.abc.Error`.

`obj.to_mcnp()` round-trips exactly, except `Inp.to_mcnp()` wraps card lines longer than 80 columns with `&` (MCNP rejects data past column 80). `obj.to_file(path)` writes.

## a) Create inputs, scan, run

```python
import pymcnp
from pymcnp.inp import card
from pymcnp.inp.card import surface, data
s = surface.So(j=1, r=10)
mat = data.M.from_formula(suffix=1, formulas={'H2O': 1}, is_weight=False)  # default is weight fractions
cell = card.Cell_0(j=1, m=1, d=1.0, geom=-s, options=['imp:n=1'])  # -s, +s build senses; & is intersection ('1 2'), | is union ('(1:2)')
outside = card.Cell_1(j=2, m=0, geom=+s, options=['imp:n=0'])      # Cell_1 = void (no density)
inp = pymcnp.Inp(title='Sphere\n', cells=[cell, outside], surfaces=[s],
                 data=[mat, data.Sdef(options=['ERG=14'])])
inp.nps = 1000      # setters add the card if missing
inp.seed = 42
```

Import the subpackages (`from pymcnp.inp import card`, `from pymcnp.inp.card import surface, data`) instead of spelling out `pymcnp.inp.card.surface.` each time; scripts read much better. Cards also accept strings (`geom='#(99:3)'`, `options=['imp:n=1.0']`). Field names follow the class, not the manual: `Nps(npp=...)`, `Rcc` has `h1 h2 h3` for the height vector. `M.from_formula(..., library='80c')` appends a library suffix to every ZAID (without it MCNP needs a default library); fractions are weight (negative) or atom (positive) fractions per element and isotope. See `examples/create_inp.py` for tallies and multi-surface geometry.

Scan: read a file, then `inp.scan(nps=[...], seed=[...])` yields independent deep copies for every combination (`nps` and `seed` only; the last field varies fastest). For any other field use `inp.scan_with(values, apply)`, which deep-copies per value and calls `apply(copy, value)` (`examples/do_parameter_scan.py`). Use `list(...)` to pass the copies to `Run`:

```python
base, rest = pymcnp.Inp.from_file('model.inp'); assert rest == ''
inps = list(base.scan_with((9, 10, 11), lambda inp, r: setattr(inp.surfaces[0], 'r', r)))  # surfaces/cells/data are indexable lists of cards; fields are named as in the MCNP manual
inps += list(base.scan(nps=[10**4, 10**5]))
```

(`copy.deepcopy(inp)` also works; never reuse one mutated `Inp` for several runs.)

Run: `results = pymcnp.Run(inps, command='mcnp6', max_workers=4, names='case-{index}').run(directory)` runs each input in its own directory `directory/pymcnp-<timestamp>/<name>/` (default names `run-00000`, ...; `run.directory` holds the batch path after `run`; `batch=False` skips the timestamp directory and uses `directory/<name>/`, which must not exist yet; MCNP refuses to reuse output files, so never share one directory), at most `max_workers` at a time (default: CPU count). It returns one `Result` per input, in order, with `.inp`, `.outp`, `.ptrac`, `.runtpe` (paths, `None` if not written), `.log`, `.returncode`, `.fatal_errors` and `.ok`. It waits for all runs, then raises `abc.Error` listing the failed ones (non-zero exit code or `fatal error` in the output), unless `check=False`; then test `result.ok`. `Run(...)` raises `abc.Error` if `command` is not on `PATH` (use `command='echo'` to dry-run). Subclass `Run` and override `prehook_file(path, index)`, `posthook_file(result)` (runs in the worker thread, so heavy post-processing such as PTRAC to parquet runs in parallel without your own pool; skipped for failed runs), `prehook_batch(path)`, `posthook_batch(path)` (`examples/do_run.py`). `Outp.fatal_errors` lists the fatal errors of any parsed output. CLI: `pymcnp run [-c CMD] [-p DIR] a.inp b.inp`.

## b) Read outputs

- `outp, rest = pymcnp.Outp.from_file(p)`; `outp.to_dataframe()` returns `{tally_number: pandas.DataFrame}`. `outp.activity('photon')` / `outp.activity('neutron')` returns the activity table (print table 126) as a dataframe, one row per cell (`cell`, `tracks` entering, `population`, `collisions`, ...) plus a final totals row with `cell` missing; use it to cross-check counts from a PTRAC file, e.g., photon tracks entering a cell. `outp.fatal_errors` lists MCNP's fatal errors.
- `pymcnp.Convert(outp).to_csv('1', path)` / `.to_parquet('1', path)`; `pymcnp.Plot(outp).to_pdf('1', path)` / `.to_show('1')`. Tally number is a string. CLI: `pymcnp convert --csv f.outp 1`, `pymcnp plot --pdf f.outp 1`.
- **PTRAC files can be huge: stream them, parse once.** `pymcnp.Ptrac.stream(path)` reads the file history by history and yields one `ptrac.Event` at a time with flat memory (about 300 MB for a 345 MB file); `Ptrac.tracks(path)` yields one `ptrac.Track` per particle; `Ptrac.iter_histories(path)` yields `History` objects. `pymcnp.PtracProcessor` (override `process_source/bank/surface/collision/terminal`) and `pymcnp.PtracFilter` (override `check_*`; `.run` yields accepted events) accept the path directly: `.run(path)`. Do **not** call `Ptrac.from_file` on anything large: it builds the whole object tree, about 35x the file size in RAM (10 GB for 345 MB), and the file is parsed again for every extra pass. Do all the work in one pass over the generator. `Ptrac.from_file(p)` (returns `(ptrac, rest)`, `ptrac.histories` is a list) is fine for small files and for inspecting the structure.
- `ptrac.Event` (from `stream`) has the type and meaning already worked out, so do not read raw `J`-line slots:
  - `event.nps`, `event.type` (`pymcnp.ptrac.EventType`: `SOURCE`, `BANK`, `SURFACE`, `COLLISION`, `TERMINAL`, `END`; for banked particles `event.creation_code` keeps the `2xxx` code), `event.particle` (`pymcnp.ptrac.Particle`, e.g., `PHOTON`; a plain `int` for rare ones), `event.cell`, `event.material`.
  - `event.surface` (`ptrac.Surface` with `.number` and `.facet`, e.g., `3.1` is surface 3 facet 1; surface crossings only), `event.cell_entered` (surface crossings only), `event.zaid` (collisions: the nuclide hit; bank events: the nuclide of the collision that made the particle, `None` if it is 0, e.g., photons made by photon interactions).
  - `event.position`, and with `PTRAC ... WRITE=ALL` also `event.direction`, `event.energy`, `event.weight`, `event.time`. **Without `WRITE=ALL` these are `None`: they are not in the file, so rerun MCNP rather than guess.** `event.raw` is the text as written, `event.j` / `event.p` are the parsed lines, `event.to_dict()` is a flat row of plain values, `pymcnp.ptrac.to_dataframe(rows)` gives proper dtypes (nullable `Int64`, `string`).
  - `TYPE=P` restricts what MCNP writes to photons, `CELL=`/`SURFACE=` (macrobody facets like `3.1` work) restrict events inside MCNP, `EVENT=` chooses event types: add `COL` for collisions and `BNK` for bank events, otherwise the originating nuclide is unknowable (say so and ask for a rerun).
- **Originating isotope of a photon**: use `Ptrac.tracks(path, particle=None, entered=None)`. A `Track` is one particle (its `events` start with the source or bank event); `track.parent` is the track it was banked from (`None` for source particles or if not found) and `track.parent_zaid` is the nuclide of the collision that started its chain (inherited from the parent when the bank event has ZAID 0; `None` if unknown, never 0). `particle=pymcnp.ptrac.Particle.PHOTON` and `entered=<cell>` drop other tracks early (parents are still resolved); `track.entries(cell=3, surface=3)` yields a track's matching surface crossings (any facet). Needs `EVENT=` with `BNK` (and `COL`). Gammas entering a detector cell, one pass:

    ```python
    import pandas, pymcnp
    rows = []
    for track in pymcnp.Ptrac.tracks('ptrac', particle=pymcnp.ptrac.Particle.PHOTON, entered=3):
        for e in track.entries(cell=3, surface=3):
            rows.append({**e.to_dict(), 'parent_zaid': track.parent_zaid})
    assert rows, 'no photons entered the detector (or EVENT= lacks SUR)'
    pandas.DataFrame(rows).to_parquet('out.parquet')
    ```

  For big files or many rows write straight to parquet in chunks instead (flat memory; columns of `Event.to_dict` plus `track` and `parent_zaid`, typed `Int64`/`string`/`float64`; uses `pyarrow` if installed, else `fastparquet`; returns the row count): `pymcnp.Ptrac.to_parquet('ptrac', 'out.parquet', particle=pymcnp.ptrac.Particle.PHOTON, cell_entered=3, surface=3)`. With `cell_entered`/`surface` only matching surface crossings are written; `types={pymcnp.ptrac.EventType.SURFACE}` restricts event types.
- Object model behind it (`from_file`, `iter_histories`; check `rest == ''` and `len(ptrac.histories) > 0`, a header-only file gives zero histories): `history.i.nps`, `history.i.event_type`; `history.events` is a list of `block.Event` with `.j` and `.p`, all fixed-width strings. **The type on an event's `J` line is the type of the NEXT event**; an event's own type is the previous event's `j.type` (for the first event `history.i.event_type`). `Ptrac.stream` does this bookkeeping and normalises the `J_0`..`J_3` forms, whose slot names are generic (`nsr__nsx_nsf_nter`, `ncl__ipt`, ...). `event.p` is `P_0` (`x y z`, default `WRITE=POS`) or `P_1` (`x y z u v w erg wgt tme`).
- `pymcnp.Meshtal.from_file(p)` parses header, title, histories, tally number, particle, bin boundaries and every data row (`.rows`). `meshtal.names` lists the columns (`Energy`/`Time` only if present, then `X Y Z Result Rel Error`); `meshtal.to_dataframe()` returns a `pandas.DataFrame` with float columns (Energy/Time stay strings if any bin is `Total`).
- Parsing time is linear in file size: about 0.07 ms per PTRAC event (a 345 MB file with 1.7 million events takes about two minutes, a 1 MB file a second or so). Older versions (before the offset-based parser) were quadratic, so upgrade before parsing large PTRAC or OUTP files. To save time, restrict what MCNP writes (`PTRAC ... EVENT=`, `CELL=`, `SURFACE=`, `TYPE=`, `FILTER=`, `MAX=`) rather than filtering afterwards.

## c) Check and modify existing files

CLI `pymcnp check [--diff] [--fix] f.inp`:

| Exit | Meaning |
|---|---|
| 0 | clean (or `--fix` applied) |
| 1 | lines over 80 columns (error), no `--fix` |
| 2 | file not found |
| 3 | PyMCNP cannot parse a card (warning; MCNP may still accept it). Checking stops at the first such card, so recheck after fixing |

`--diff` shows what `--fix` would change; `--fix` rewrites the file in place (re-wrapping to 80 columns) and refuses on exit-3 files. Work on a copy if the original matters.

Python: `c = pymcnp.Check(path)`; `c.problems()` returns `Problem(line, kind, message)` (kind is `'error'` or `'warning'`); `c.check()` yields a unified diff; `c.fix()` rewrites in place.

Edit loop: `inp, rest = Inp.from_file(p)`; assert `rest == ''`; change fields or use `inp.nps` / `inp.seed`; `inp.to_file(p2)`. Visualize geometry: `pymcnp.Visualize(inp).to_show_surfaces()` (pyvista).

## d) Missing feature or parse failure

PyMCNP does not cover all MCNP options. If a valid MCNP file fails (`abc.Error`, non-empty `remainder`, `check` exit 3) or a card/feature is missing, or MCNP rejects a PyMCNP round trip, do not work around it silently. Draft a GitHub issue for https://github.com/FSIBT/PyMCNP/issues (CONTRIBUTING.md asks for exactly this) and show it to the user before posting:

- a minimal input: trim to the few cards that trigger it,
- the full traceback or `remainder` / unexpected output,
- PyMCNP version (`pip show pymcnp`), Python version, MCNP version (6.1 mostly tested, 6.3 starting),
- nothing export-controlled or sensitive.

Failing inputs are explicitly welcome, so say what you were trying to do.
