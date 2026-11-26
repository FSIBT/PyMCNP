"""
Example running INP files using `Run`.

This example runs three input files, `example_00.inp`, `example_01.inp`, and
`example_02.inp`. First, it subclasses `Run`, adding callbacks. Second, it
reads the input files and sets their nps and seed. Finally, it runs the INP
files in parallel (two at a time) and prints the result of each run. Every input runs in its own directory inside a new `pymcnp-<timestamp>`
directory, and `Run` collects the `.outp`, `.ptrac` and `.runtpe` files in each `Result`. With `check` (the default) `run` raises if a run failed.
"""

import os
import pathlib

import pymcnp


# A stand-in for MCNP that writes no files: `echo`, or on Windows, which has no `echo` program, `where`.
COMMAND = 'where' if os.name == 'nt' else 'echo'
HERE = pathlib.Path(__file__).parent
OUTPUT = HERE / 'output'
OUTPUT.mkdir(exist_ok=True)


# Creating `Run` subclass.
class MyRun(pymcnp.Run):
    def prehook_file(self, path: pathlib.Path, index: int) -> None:
        print(f'Calling `prehook_file` {index} in {path.name}')

    def posthook_file(self, result: pymcnp.Result) -> None:
        print(f'Calling `posthook_file` {result.directory.name} {result.index} (ok={result.ok})')

    def prehook_batch(self, path: pathlib.Path) -> None:
        print(f'Calling `prehook_batch` {path.name}')

    def posthook_batch(self, path: pathlib.Path) -> None:
        print(f'Calling `posthook_batch` {path.name}')


# Reading INP.
path0 = HERE / 'example_00.inp'
path1 = HERE / 'example_01.inp'
path2 = HERE / 'example_02.inp'
inp0, _ = pymcnp.Inp.from_file(path0)
inp1, _ = pymcnp.Inp.from_file(path1)
inp2, _ = pymcnp.Inp.from_file(path2)

inp0.nps = int(1e4)
inp1.nps = int(1e5)
inp2.nps = int(1e6)
inp0.seed = 123534727
inp1.seed = 123534727
inp2.seed = 123534727

# Running.
print(f'Running `{COMMAND}` in `{OUTPUT}`:')
# `check=False`, since ECHO writes no OUTP, so the runs count as failed; use `command='mcnp6'` for real runs.
runner = MyRun([inp0, inp1, inp2], command=COMMAND, max_workers=2, check=False)
results = runner.run(OUTPUT)

for result in results:
    print(f'Run {result.index}: exit code {result.returncode}, input `{result.inp.name}`, output `{result.outp}`')
