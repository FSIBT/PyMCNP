"""
Example parameter scan.

This example mocks the parameter scan workflow. First, it reads INP file `example_04.inp`.
Second, it create multiple INP files by iterates over a surface's `vy` parameter. Thrid,
it visualizes the surfaces. Fourth, it subclasses `Run`, adding callbacks that process
the output files. Finaly, it runs the input files in parallel.
"""

import copy
import pathlib

import pymcnp


COMMAND = 'echo'
HERE = pathlib.Path(__file__).parent
OUTPUT = HERE / 'output'
OUTPUT.mkdir(exist_ok=True)


class MyRun(pymcnp.Run):
    def posthook_file(self, result):
        # Copying OUTP (ECHO used for demo).
        path_copy = HERE / 'example_01.outp'
        path_outp = result.directory / f'run-{result.index}.outp'

        with path_outp.open('w') as file_outp, path_copy.open('r') as file_copy:
            file_outp.write(file_copy.read())

        # Reading OUTP.
        # outp, _ = pymcnp.Outp.from_file(result.outp)

        # Plotting.
        # path_pdf = result.directory / '..' / f'run-{result.index}.pdf'
        # plotter = pymcnp.Plot(outp)
        # plotter.to_pdf('1', path_pdf)

    def posthook_batch(self, path):
        # Deleting Run.
        # shutil.rmtree(path)
        print('DONE! :)')


# Reading INP.
path_inp = HERE / 'example_04.inp'
inp, _ = pymcnp.Inp.from_file(path_inp)

# Scanning.
inps = []
for vy in [-2, -1, 0, 1, 2]:
    assert isinstance(inp.surfaces[0], pymcnp.inp.card.surface.Sph)
    inp.surfaces[0].vy = vy
    inps.append(copy.deepcopy(inp))

# Visualizing.
for inp in inps:
    visualizer = pymcnp.Visualize(inp)
    visualization = visualizer.to_show_surfaces()
    visualization.show()

# Running.
print(f'Running parameter scan `{COMMAND}` in `{OUTPUT}`:')
runner = MyRun(inps, command=COMMAND)
runner.run(OUTPUT)
