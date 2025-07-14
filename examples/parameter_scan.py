"""
Example parameter scan.
"""

import copy
import shutil
import pathlib

import pymcnp


# Reading INP.
path_inp = pathlib.Path(__file__).parent / 'files' / 'inp' / 'inp_A.i'
inp = pymcnp.Inp.from_file(path_inp)

# Scanning.
inps = []
for vy in [-2, -1, 0, 1, 2]:
    inp.surfaces[0].option.vy = vy
    inps.append(copy.deepcopy(inp))

# Visualizing.
for inp in inps:
    visualizer = pymcnp.cli.Visualize(inp)
    visualization = visualizer.to_show_surfaces()
    visualization.show()


class MyRun(pymcnp.cli.Run):
    def posthook_file(self, path, index):
        # Copying OUTP (ECHO used for demo).
        path_copy = pathlib.Path(__file__).parent / 'files' / 'outp' / 'F1.o'
        path_outp = path / f'run-{index}.outp'
        path_outp.open('w').write(path_copy.open('r').read())

        # Reading OUTP.
        path_outp = path / f'run-{index}.outp'
        outp = pymcnp.Outp.from_file(path_outp)

        # Plotting.
        path_pdf = path / '..' / f'run-{index}.pdf'
        plotter = pymcnp.cli.Plot(outp)
        plotter.to_pdf('1', path_pdf)

        # Deleting Run.
        shutil.rmtree(path)

    def posthook_batch(self, path):
        print('DONE! :)')


# Running.
runner = MyRun(inps, command='echo')
runner.run('.')
