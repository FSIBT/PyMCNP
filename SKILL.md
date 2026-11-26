---
name: pymcnp
description: Use when creating, editing, scanning, checking, or running MCNP input files (.inp) from Python, reading MCNP output (OUTP, MESHTAL, PTRAC), validating an MCNP input's syntax, or when PyMCNP fails to parse a valid MCNP file or lacks a card/feature.
---

# PyMCNP

Python API and CLI for MCNP inputs and outputs (`pip install pymcnp`, Python 3.11-3.15). Working scripts live in `examples/` of the repository (`create_*.py`, `read_*.py`, `do_*.py`; https://github.com/FSIBT/PyMCNP/tree/main/examples, not installed by pip); copy from them.

## Parsing contract

`X.from_mcnp(text)` and `X.from_file(path)` return `(obj, remainder)`. Parsing stops silently at the first card it cannot parse; that card and everything after it is the `remainder`. **Always check `remainder == ''`**, otherwise part of the file was dropped. Unparseable input with nothing parseable raises `pymcnp.abc.Error`. For OUTP files an empty remainder is not enough: tally blocks in a layout PyMCNP cannot parse yet (e.g., F8, and some F1/F2/F4/F5 layouts) are kept as unparsed text, so they leave no remainder; each one issues a `pymcnp.abc.Warning` ("Tally not parsed.", with the tally number and type), is missing from `outp.tallies()` and `outp.to_dataframe()`, and `outp.tally(n)` raises `abc.Error` "Tally not parsed.". Do not silence these warnings; report the missing tally type (see "d) Missing feature or parse failure").

`obj.to_mcnp()` writes MCNP text. For OUTP, PTRAC and MESHTAL, `obj.to_mcnp() + remainder` is the original text. `Inp.to_mcnp()` writes equivalent input, not the same text: it expands the shorthands `nR`, `nI`, `nILOG`/`nLOG`, `nJ` and `xM` of cards (not comments) into explicit entries (`e1 0.1 511i 10` becomes 512 numbers, with float noise such as `0.17734375000000002`), may pad a card with trailing `J`s, and wraps card lines longer than 80 columns with `&` (MCNP rejects data past column 80). So compare inputs by parsing both, not by diffing text. `obj.to_file(path)` writes.

## a) Create inputs, scan, run

```python
import pymcnp
from pymcnp.inp import card
from pymcnp.inp.card import surface, data

s = surface.So(j=1, r=10)
mat = data.M.from_formula(suffix=1, formulas={'H2O': 1}, is_weight=False)  # default is weight fractions
cell = card.Cell_0(j=1, m=1, d=1.0, geom=-s, options=['imp:n=1'])  # -s, +s build senses; & is intersection ('1 2'), | is union ('(1:2)')
outside = card.Cell_1(j=2, m=0, geom=+s, options=['imp:n=0'])  # Cell_1 = void (no density)
inp = pymcnp.Inp(title='Sphere\n', cells=[cell, outside], surfaces=[s], data=[mat, data.Sdef(options=['ERG=14'])])
inp.nps = 1000  # setters add the card if missing
inp.seed = 42
```

Import the subpackages (`from pymcnp.inp import card`, `from pymcnp.inp.card import surface, data`) instead of spelling out `pymcnp.inp.card.surface.` each time; scripts read much better. Cards also accept strings (`geom='#(99:3)'`, `options=['imp:n=1.0']`). Field names follow the class, not the manual: `Nps(npp=...)`, `Rcc` has `h1 h2 h3` for the height vector. `M.from_formula(..., library='80c')` appends a library suffix to every ZAID (without it MCNP needs a default library); fractions are weight (negative) or atom (positive) fractions per element and isotope. See `examples/create_inp.py` for tallies and multi-surface geometry.

Scan: read a file, then `inp.scan(nps=[...], seed=[...])` yields independent deep copies for every combination of the values of fields or settable properties such as `nps`, `seed` or `title` (the last one varies fastest; a title value gets the trailing newline of the title card if it has none, e.g., `title=['Case A', 'Case B']`). A key may also be a path to a nested field, `inp.scan(**{'surfaces[0].r': [9, 10, 11]})` (attributes with `.name`, list items with `[i]`; the index into `cells`, `surfaces` or `data` counts cards and skips comment cards, unlike `inp.surfaces[i]`, so it is a position, not a surface number: to pick a card by its number prefer `scan_with` + `surface_cards(n)`; values become the field's literal type, e.g., `inp.literal.Real`, which compares and computes as a number; `abc.Error` if the path does not exist). For changes that need code (several fields, computed values) use `inp.scan_with(values, apply)`, which deep-copies per value and calls `apply(copy, value)` (`examples/do_parameter_scan.py`). Use `list(...)` to pass the copies to `Run`:

```python
base, rest = pymcnp.Inp.from_file('model.inp')
assert rest == ''
# surface_cards(n) finds cards by number; inp.surfaces[i] also counts comment cards; fields are named as in the MCNP manual
inps = list(base.scan_with((9, 10, 11), lambda inp, r: setattr(inp.surface_cards(1)[0], 'r', r)))
inps += list(base.scan(nps=[10**4, 10**5]))
```

(`copy.deepcopy(inp)` also works; never reuse one mutated `Inp` for several runs.)

Lookups: `inp.cell_cards(number=None, material=None, density=None, kind=Cell)`, `inp.surface_cards(number=None, kind=Surface)` and `inp.data_cards(kind=Data)` return a tuple of the cards themselves, so edits change the input (`inp.surface_cards(1)[0].r = 5`); the tuple is empty if nothing matches, and the filters combine (`inp.cell_cards(material=2)` lists the cells with material `2`, following `LIKE n BUT`; `material=0` lists void cells). `kind` restricts the card class: `inp.data_cards(data.M)` returns the material cards, `inp.data_cards(data.Fmesh)` the mesh tallies. `inp.cells`, `inp.surfaces` and `inp.data` are the indexable card lists, whose `filter(kind, field=value)` skips items without that field. Warnings use Python's standard `warnings` module (PyMCNP installs no hook).

Run: `results = pymcnp.Run(inps, command='mcnp6', max_workers=4, names='case-{index}').run(directory)` runs each input in its own directory `directory/pymcnp-<timestamp>/<name>/` (default names `run-00000`, ...; `run.directory` holds the batch path after `run`; `batch=False` skips the timestamp directory and uses `directory/<name>/`, which must not exist yet; MCNP refuses to reuse output files, so never share one directory), at most `max_workers` at a time (default: CPU count). It returns one `Result` per input, in order, with `.inp`, `.outp`, `.ptrac`, `.runtpe` (paths, `None` if not written), `.log`, `.returncode`, `.fatal_errors` and `.ok`. It waits for all runs, then raises `abc.Error` listing the failed ones (non-zero exit code or `fatal error` in the output), unless `check=False`; then test `result.ok`. `Run(...)` raises `abc.Error` if `command` is not on `PATH`. To dry-run, use `command='echo', check=False` (`echo` writes no output file, so with the default `check=True` the run fails with `exit code 0, no output file`). Subclass `Run` and override `prehook_file(path, index)`, `posthook_file(result)` (runs in the worker thread, so heavy post-processing such as PTRAC to parquet runs in parallel without your own pool; skipped for failed runs unless `check=False`), `prehook_batch(path)`, `posthook_batch(path)` (`examples/do_run.py`). `Outp.fatal_errors` lists the fatal errors of any parsed output. CLI: `pymcnp run [-c CMD] [-p DIR] a.inp b.inp` (runs nothing and exits 3 if PyMCNP cannot parse a card of an input).

## b) Read outputs

- `outp, rest = pymcnp.Outp.from_file(p)`; `outp.to_dataframe()` returns all tallies in one `pandas.DataFrame` with a `number` column (untyped string columns); prefer `outp.tally(n)` below. `outp.activity('photon')` / `outp.activity('neutron')` returns the activity table (print table 126) as a dataframe, one row per cell (`cell`, `tracks` entering, `population`, `collisions`, ...) plus a final totals row with `cell` missing; use it to cross-check counts from a PTRAC file, e.g., photon tracks entering a cell. `outp.fatal_errors` lists MCNP's fatal errors. `outp.summary` gives the headline results without regexes: `.version`, `.nps` (histories run), `.run_time` (minutes), `.terminated` (`'histories'`, `'cycles'` or `'fatal errors'`), `.ok`, `.keff` / `.keff_sd` (final combined, `KCODE` problems only, else `None`), `.warnings` (unique), `.fatal_errors`, and `.checks` (tally number to `TallyCheck(passed, failed, message)`: MCNP's 10 statistical checks of the tally fluctuation bin) with `.checks_passed` (`None` if no checks are printed). Always check `summary.ok` and `summary.checks_passed` before trusting results. `outp.tallies()` returns the parsed tally blocks (`outp.block.Tally`, not a dataframe; `outp.tallies(n)` picks one number) and `outp.activities()` the activity blocks; `outp.tally(n)` returns one tally as a dataframe with typed columns: `bins, counts, errors`, then where present `angle_from`/`angle_to` (float) and `cell` or `surface`/`facet` (`Int64`), then `number` (int), `quantity`, `particles`, `nps` (int).
- `outp.to_file_csv(path)` / `outp.to_file_parquet(path)` write all tallies (`Meshtal` and `Ptrac` have the same methods; for one tally use `outp.tally(n).to_csv(path)`); `pymcnp.Plot().to_pdf(outp, '1', path)` / `pymcnp.Plot().to_show(outp, '1')` (the tally number may be an `int` or a `str`). CLI: `pymcnp convert outp --csv f.outp` (also `ptrac`, `meshtal`; writes `f.csv`; for `meshtal` every mesh tally, with a `number` column), `pymcnp plot --pdf f.outp 1`; both write or plot the parsed part and exit 3 if PyMCNP cannot parse all of the file.
- **PTRAC files can be huge: stream them, parse once.** `pymcnp.Ptrac.stream(path)` reads the file history by history and yields one `ptrac.Event` at a time with flat memory (about 300 MB for a 345 MB file); `Ptrac.tracks(path)` yields one `ptrac.Track` per particle; `Ptrac.iter_histories(path)` yields `History` objects (or `ptrac.block.HistoryTruncated`, see below). `pymcnp.PtracProcessor` (override `process_source/bank/surface/collision/terminal`; `.run` returns the non-`None` results) and `pymcnp.PtracFilter` (override `check_*`; `.run` yields accepted events) accept the path directly: `.run(path)`. Do **not** call `Ptrac.from_file` on anything large: it builds the whole object tree, about 35x the file size in RAM (10 GB for 345 MB), and the file is parsed again for every extra pass. Do all the work in one pass over the generator. A PTRAC file cut short, e.g., by a killed MCNP run, keeps its truncated last history: `stream`, `tracks`, `to_parquet` and `iter_histories` (which yields it as `HistoryTruncated`) read it and issue an `abc.Warning`, while damage anywhere before the final event still raises `abc.Error`. `Ptrac.from_file` on such a file leaves the partial last history in `rest`, so use the streaming functions for files that may be truncated. `Ptrac.from_file(p)` (returns `(ptrac, rest)`, `ptrac.histories` is a list) is fine for small files and for inspecting the structure.
- `ptrac.Event` (from `stream`) has the type and meaning already worked out, so do not read raw `J`-line slots:
  - `event.nps`, `event.type` (`pymcnp.ptrac.EventType`: `SOURCE`, `BANK`, `SURFACE`, `COLLISION`, `TERMINAL`, `END`; for banked particles `event.creation_code` keeps the `2xxx` code), `event.particle` (`pymcnp.ptrac.Particle`, e.g., `PHOTON`; a plain `int` for rare ones), `event.cell`, `event.material`.
  - `event.surface` (`ptrac.Surface` with `.number` and `.facet`, e.g., `3.1` is surface 3 facet 1; surface crossings only), `event.cell_entered` (surface crossings only), `event.zaid` (collisions: the nuclide hit; bank events: the nuclide of the collision that made the particle, `None` if it is 0, e.g., photons made by photon interactions).
  - `event.position`, and with `PTRAC ... WRITE=ALL` also `event.direction`, `event.energy`, `event.weight`, `event.time`. **Without `WRITE=ALL` these are `None`: they are not in the file, so rerun MCNP rather than guess.** `event.raw` is the text as written, `event.block` is the parsed event block, `event.to_dict()` is a flat row of plain values, `pymcnp.ptrac.to_dataframe(rows)` gives proper dtypes (nullable `Int64`, `string`).
  - `TYPE=P` restricts what MCNP writes to photons, `CELL=`/`SURFACE=` (macrobody facets like `3.1` work) restrict events inside MCNP, `EVENT=` chooses event types: add `COL` for collisions and `BNK` for bank events, otherwise the originating nuclide is unknowable (say so and ask for a rerun). Separate several values with commas, e.g., `PTRAC FILE=ASC WRITE=ALL TYPE=P EVENT=SRC,BNK,SUR,COL,TER CELL=3,4 SURFACE=3.1,4`; PyMCNP reads only ASCII PTRAC files, so always write `FILE=ASC`.
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

  For big files or many rows write straight to parquet in chunks instead (flat memory; columns of `Event.to_dict` plus `track` and `parent_zaid`, typed `Int64`/`string`/`float64`; returns the row count): `pymcnp.Ptrac.to_parquet('ptrac', 'out.parquet', particle=pymcnp.ptrac.Particle.PHOTON, cell_entered=3, surface=3)`. With `cell_entered`/`surface` only matching surface crossings are written; `types={pymcnp.ptrac.EventType.SURFACE}` restricts event types.
- Object model behind it (`from_file`, `iter_histories`; check `rest == ''` and `len(ptrac.histories) > 0`, a header-only file gives zero histories): `history.nps`, `history.event_type`; `history.events` is a list of event blocks (`pymcnp.ptrac.block.EventSource_1`, ..., `EventTermination_4`, named after the variables of the MCNP manual, e.g., `pbl_r_x`, `ncl_pbl_i_icl`), all fixed-width strings. **The `type` on an event's `J` line is the type of the NEXT event**; an event's own type is the previous event's `type` (for the first event `history.event_type`), which PyMCNP uses to pick the event block class. `Ptrac.stream` gives the values by meaning, whatever the PTRAC options.
- `pymcnp.Meshtal.from_file(p)` parses only the FIRST mesh tally of a file (the others come back as the non-empty `rest`, check it): for files with several `FMESH` tallies use `for tally in pymcnp.Meshtal.iter_tallies(p)`, which yields one `Meshtal` per tally with `tally.tally_number` (`int`) and `tally.particle_name` (plain `str`). A `Meshtal` parses header, title, histories, tally number, particle, bin boundaries and every data row (`.rows`). `meshtal.names` (list of `str`) lists the columns (`Energy`/`Time` only if present, then `X Y Z Result Rel Error`); `meshtal.to_dataframe()` returns a `pandas.DataFrame` with float columns (one frame per tally; `Energy`/`Time` stay strings if a bin is `Total`).
- Parsing time is linear in file size: about 0.01 ms per PTRAC event with `Ptrac.from_file` (a 1.1 MB file with 10,000 events takes about a tenth of a second; at that rate a file with 1.7 million events, e.g., 345 MB, takes roughly 20 seconds). Older versions (before the offset-based parser) were quadratic, so upgrade before parsing large PTRAC or OUTP files. To save time, restrict what MCNP writes (`PTRAC ... EVENT=`, `CELL=`, `SURFACE=`, `TYPE=`, `MAX=`) rather than filtering afterwards. PyMCNP cannot parse the `FILTER=` keyword yet, so an input using it leaves a remainder; avoid it, or tell the user.

## c) Check and modify existing files

CLI `pymcnp check [--diff] [--fix] f.inp`:

| Exit | Meaning |
|---|---|
| 0 | clean (or `--fix` applied and no line is left over 80 columns) |
| 1 | lines over 80 columns (error); with `--fix`, lines it cannot shorten (long `c` or `$` comments), so shorten those by hand |
| 2 | file not found |
| 3 | PyMCNP cannot parse a card (warning; MCNP may still accept it). Checking stops at the first such card, so recheck after fixing |

`--diff` shows what `--fix` would change; `--fix` rewrites the file in place (re-wrapping to 80 columns) and refuses on exit-3 files. Work on a copy if the original matters.

Python: `c = pymcnp.Check(path)`; `c.problems()` returns `Problem(line, kind, message)` (kind is `'error'` or `'warning'`); `c.check()` yields a unified diff; `c.fix()` rewrites in place and returns the problems left (e.g., comments still over 80 columns).

Edit loop: `inp, rest = Inp.from_file(p)`; assert `rest == ''`; change fields or use `inp.nps` / `inp.seed`; `inp.to_file(p2)`. Visualize geometry: `pymcnp.Visualize().to_show_surfaces(inp)` (pyvista; also `to_show_cells`, `to_show_cell(inp, n)`, and `to_pdf_surfaces(inp, path)` / `to_pdf_cells`).

## d) Missing feature or parse failure

PyMCNP does not cover all MCNP options. If a valid MCNP file fails (`abc.Error`, non-empty `remainder`, `check` exit 3) or a card/feature is missing, or MCNP rejects a PyMCNP round trip, do not work around it silently. Draft a GitHub issue for https://github.com/FSIBT/PyMCNP/issues (CONTRIBUTING.md asks for exactly this) and show it to the user before posting:

- a minimal input: trim to the few cards that trigger it,
- the full traceback or `remainder` / unexpected output,
- PyMCNP version (`pip show pymcnp`), Python version, MCNP version (PyMCNP supports 6.1 to 6.3),
- nothing export-controlled or sensitive.

Failing inputs are explicitly welcome, so say what you were trying to do.
