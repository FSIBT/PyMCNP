"""
Example parameter scan.

This example mocks the parameter scan workflow. First, it reads INP file `example_04.inp`.
Second, it creates independent copies of the input with `Inp.scan`, setting the `vy` parameter of surface 11
through the path `surfaces[11].vy` (`Inp.scan(nps=..., seed=...)` scans `nps` and `seed`, and `Inp.scan_with`
applies a function to each copy). Third,
it visualizes the surfaces. Fourth, it subclasses `Run`, adding callbacks that process
the output files. Finally, it runs the input files in parallel.
"""

import pathlib

import pymcnp


COMMAND = 'echo'
HERE = pathlib.Path(__file__).parent
OUTPUT = HERE / 'output'
OUTPUT.mkdir(exist_ok=True)


class MyRun(pymcnp.Run):
    def posthook_file(self, result: pymcnp.Result) -> None:
        # Copying OUTP (ECHO used for demo).
        path_copy = HERE / 'example_01.outp'
        path_outp = result.inp.with_suffix('.outp')

        with path_outp.open('w') as file_outp, path_copy.open('r') as file_copy:
            file_outp.write(file_copy.read())

        # Reading OUTP.
        # outp, _ = pymcnp.Outp.from_file(path_outp)

        # Plotting.
        # path_pdf = result.directory / '..' / f'run-{result.index}.pdf'
        # pymcnp.Plot().to_pdf(outp, '1', path_pdf)

    def posthook_batch(self, path: pathlib.Path) -> None:
        # Deleting Run.
        # shutil.rmtree(path)
        print('DONE! :)')


# Reading INP.
path_inp = HERE / 'example_04.inp'
inp, _ = pymcnp.Inp.from_file(path_inp)
inps = tuple(inp.scan(**{'surfaces[11].vy': [-2, -1, 0, 1, 2]}))

# Visualizing.
visualizer = pymcnp.Visualize()
for inp in inps:
    visualization = visualizer.to_show_surfaces(inp)
    visualization.show()

# Running.
print(f'Running parameter scan `{COMMAND}` in `{OUTPUT}`:')
# `check=False`, since ECHO writes no OUTP, so MCNP would count the runs as failed.
runner = MyRun(inps, command=COMMAND, check=False)
runner.run(OUTPUT)
