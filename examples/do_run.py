"""
Example running INP files using `Run`.

This example runs three input files, `example_00.inp`, `example_01.inp`, and
`example_02.inp`. First, it subclasses `Run`, adding callbacks. Second, it
reads the input files and sets their nps and seed. Finally, it runs the INP
files in parallel (two at a time) and prints the result of each run. `Run` also
collects `.outp`, `.ptrac` and `.runtpe` files, and raises if a run failed.
"""

import typing
import pathlib

import pymcnp


COMMAND = 'echo'
HERE = pathlib.Path(__file__).parent
OUTPUT = HERE / 'output'
OUTPUT.mkdir(exist_ok=True)


# Creating `Run` subclass.
class MyRun(pymcnp.Run):
    def prehook_file(self, inp: pymcnp.Inp, index: int) -> None:
        print(f'Calling `prehook_file` {index}')

    def posthook_file(self, result: pymcnp.Result, index: int) -> typing.Any:
        print(f'Calling `posthook_file` {result.directory} {result.index} (ok={result.ok})')
        return super().posthook_file(result, index)

    def prehook_batch(self, *inps: pymcnp.Inp) -> None:
        print('Calling `prehook_batch')

    def posthook_batch(self, results: tuple[typing.Any, ...]) -> typing.Any:
        print('Calling `posthook_batch`')
        return super().posthook_batch(results)


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
runner = MyRun(command=COMMAND, directory=OUTPUT)
results = runner.run(inp0, inp1, inp2)

for result in results:
    print(f'Run {result.index}: exit code {result.returncode}, input `{result.inp.name}`, output `{result.outp}`')
