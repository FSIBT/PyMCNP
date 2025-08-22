"""
Example parameter scan.

This example mocks the parameter scan workflow. First, it reads INP file `example_04.inp`.
Second, it create multiple INP files by iterates over a surface's `vy` parameter. Thrid,
it visualizes the surfaces. Fourth, it subclasses `Run`, adding callbacks that process
the output files. Finaly, it runs the input files in parallel.
"""

import copy
import shutil
import pathlib

import pymcnp


COMMAND = 'echo'


class MyRun(pymcnp.Run):
    def posthook_file(self, path, index):
        # Copying OUTP (ECHO used for demo).
        path_copy = pathlib.Path('example_01.outp')
        path_outp = path / f'run-{index}.outp'

        with path_outp.open('w') as file_outp:
            with path_copy.open('r') as file_copy:
                file_outp.write(file_copy.read())

        # Reading OUTP.
        path_outp = path / f'run-{index}.outp'
        outp = pymcnp.Outp.from_file(path_outp)

        # Plotting.
        path_pdf = path / '..' / f'run-{index}.pdf'
        plotter = pymcnp.Plot(outp)
        plotter.to_pdf('1', path_pdf)

        # Deleting Run.
        shutil.rmtree(path)

    def posthook_batch(self, path):
        print('DONE! :)')


# Reading INP.
path_inp = pathlib.Path('example_04.inp')
inp = pymcnp.Inp.from_file(path_inp)

# Scanning.
inps = []
for vy in [-2, -1, 0, 1, 2]:
    inp.surfaces[0].option.vy = vy
    inps.append(copy.deepcopy(inp))

# Visualizing.
for inp in inps:
    visualizer = pymcnp.Visualize(inp)
    visualization = visualizer.to_show_surfaces()
    visualization.show()

# Running.
print(f'Running parameter scan `{COMMAND}` in the current working directory:')
runner = MyRun(inps, command=COMMAND)
runner.run('.')
