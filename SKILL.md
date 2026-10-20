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
s = pymcnp.inp.card.surface.So(j=1, r=10)
mat = pymcnp.inp.card.data.M.from_formula(suffix=1, formulas={'H2O': 1}, is_weight=False)  # default is weight fractions
cell = pymcnp.inp.card.Cell_0(j=1, m=1, d=1.0, geom=-s, options=['imp:n=1'])  # -s, +s, &, | build geometry
outside = pymcnp.inp.card.Cell_1(j=2, m=0, geom=+s, options=['imp:n=0'])      # Cell_1 = void (no density)
inp = pymcnp.Inp(title='Sphere\n', cells=[cell, outside], surfaces=[s],
                 data=[mat, pymcnp.inp.card.data.Sdef(options=['ERG=14'])])
inp.nps = 1000      # setters add the card if missing
inp.seed = 42
```

Cards also accept strings (`geom='#(99:3)'`, `options=['imp:n=1.0']`). See `examples/create_inp.py` for tallies and multi-surface geometry.

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
- `ptrac, rest = pymcnp.Ptrac.from_file(p)`; `ptrac.histories` is a list. Subclass `pymcnp.PtracProcessor` (override `process_source/bank/surface/collision/terminal`, then `.run(ptrac)`) or `pymcnp.PtracFilter` (override `check_*`, `.run(ptrac)` yields accepted events).
- `pymcnp.Meshtal.from_file(p)` parses header, title, histories, tally number, particle and bin boundaries; the data columns are one unparsed string (`.columns`).
- Parsing time is linear in file size: a 1 MB PTRAC file takes about a second. Older versions (before the offset-based parser) were quadratic, so upgrade before parsing large PTRAC or OUTP files.

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
