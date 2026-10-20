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
import copy, pymcnp
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

Scan: read a file, mutate a field, `copy.deepcopy` per value (`examples/do_parameter_scan.py`):

```python
base, rest = pymcnp.Inp.from_file('model.inp'); assert rest == ''
inps = []
for r in (9, 10, 11):
    base.surfaces[0].r = r            # surfaces/cells/data are indexable lists of cards; fields are named as in the MCNP manual
    inps.append(copy.deepcopy(base))
```

Run: `pymcnp.Run(inps, command='mcnp6').run(directory)` writes `directory/pymcnp-<timestamp>/run-00000/run-00000.inp` ..., starts all runs in parallel, waits, returns the batch directory. `Run(...)` raises `abc.Error` if `command` is not on `PATH` (use `command='echo'` to dry-run). Subclass `Run` and override `prehook_file(path, index)`, `posthook_file(path, index)`, `prehook_batch(path)`, `posthook_batch(path)` to read each `run-NNNNN.outp` afterwards (`examples/do_run.py`). CLI: `pymcnp run [-c CMD] [-p DIR] a.inp b.inp`.

## b) Read outputs

- `outp, rest = pymcnp.Outp.from_file(p)`; `outp.to_dataframe()` returns `{tally_number: pandas.DataFrame}`.
- `pymcnp.Convert(outp).to_csv('1', path)` / `.to_parquet('1', path)`; `pymcnp.Plot(outp).to_pdf('1', path)` / `.to_show('1')`. Tally number is a string. CLI: `pymcnp convert --csv f.outp 1`, `pymcnp plot --pdf f.outp 1`.
- **PTRAC files can be huge: stream them, parse once.** `for nps, kind, event in pymcnp.Ptrac.iter_events(path)` reads the file history by history and yields every event with its history number and its own event type (the `J`-line bookkeeping is done for you); memory stays flat (about 300 MB for a 345 MB file). `Ptrac.iter_histories(path)` yields `History` objects. `pymcnp.PtracProcessor` (override `process_source/bank/surface/collision/terminal`) and `pymcnp.PtracFilter` (override `check_*`; `.run` yields accepted events) both accept the path directly: `.run(path)`. Do **not** call `Ptrac.from_file` on anything large: it builds the whole object tree, about 35x the file size in RAM (10 GB for 345 MB) and the file is parsed again for every extra pass. Do all the work in one pass over the generator. `Ptrac.from_file(p)` (returns `(ptrac, rest)`, `ptrac.histories` is a list) is fine for small files and for inspecting the structure.
- PTRAC object model (`ptrac.header`, `ptrac.histories`; check `rest == ''` and `len(ptrac.histories) > 0`, a header-only file gives zero histories):
  - `history.i.nps`, `history.i.event_type`; `history.events` is a list of `Event` with `event.j` and `event.p`. All fields are fixed-width strings: `float(event.p.x)`, `int(event.j.type)`.
  - **The type on an event's `J` line is the type of the NEXT event, not of this one.** An event's own type is the previous event's `j.type`; for the first event it is `history.i.event_type`. Types: `1000` source, `3000` surface, `4000` collision, `5000` terminal, `9000` end of history, `2xxx` bank (`PtracProcessor.run` does this bookkeeping already). The other `J` fields and the `P` line belong to the current event.
  - `event.j` has forms `J_0`..`J_3` with generic slot names (e.g. `nsr__nsx_nsf_nter`, `ipt__ntyn_mtp_angle_branch`, `ncl__ipt`, `mat__ncl`): the same slot means different things per event type, so read the manual's PTRAC tables and check a few events. Verified on the sample files: `nsr__nsx_nsf_nter` is the nuclide ZAID of a collision (`4000`) and the surface number of a surface crossing (`3000`, e.g. `3.1`); in `J_2`, `ncl__ipt` is the particle type `ipt` (1 neutron, 2 photon, 34 alpha), and bank events (`2xxx`) carry the banked particle's `ipt` there too.
  - `event.p` is `P_0` (`x y z`, default `WRITE=POS`) or `P_1` (`x y z u v w erg wgt tme`, needs `PTRAC ... WRITE=ALL`). **Direction and energy exist only with `WRITE=ALL`**; with `P_0` they are not in the file, so rerun MCNP rather than guess. `TYPE=P` restricts to photons, `CELL=`/`SURFACE=` (macrobody facets like `3.1` work) restrict events inside MCNP.
  - **Originating isotope**: it is on the collision (`4000`) event, never on the surface event. The card needs `EVENT=` with `COL` (e.g. `EVENT=SUR,COL`; add `BNK` to see where secondaries are born). Walk each history in order and remember the ZAID of the latest collision; a photon created in that collision is then banked and later crosses the surface, so attach that ZAID to it. Without collision events the isotope is unknowable: say so and ask for a rerun.
  - Pattern, table of surface crossings with the last collision's isotope, streamed in one pass (gammas at a detector surface: `TYPE=P`, and compare the surface number to the detector's):

    ```python
    import pandas, pymcnp
    rows, zaid, last = [], None, None
    for nps, kind, e in pymcnp.Ptrac.iter_events('ptrac'):   # kind: this event's own type
        if nps != last:
            zaid, last = None, nps                            # new history
        if kind == '4000':
            zaid = int(e.j.nsr__nsx_nsf_nter)                 # nuclide of the latest collision
        elif kind == '3000' and isinstance(e.p, pymcnp.ptrac.line.P_1):
            rows.append({'nps': nps, 'surface': float(e.j.nsr__nsx_nsf_nter), 'zaid': zaid,
                         'x': float(e.p.x), 'y': float(e.p.y), 'z': float(e.p.z),
                         'u': float(e.p.u), 'v': float(e.p.v), 'w': float(e.p.w), 'erg': float(e.p.erg)})
    assert rows, 'no surface events with WRITE=ALL'
    pandas.DataFrame(rows).to_parquet('out.parquet')          # keep rows small; for hundreds of millions of events write in chunks
    ```

    The `J` slot names above are for `J_2` (particle type present); for another form check `type(e.j)._fields` first.
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
