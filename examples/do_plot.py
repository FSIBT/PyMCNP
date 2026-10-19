"""
Example plotting OUTP files using `Plot`.

This example plots tally #1 from `example_00.outp` using `to_show`, and it
writes the plots to a pdf file using `to_pdf`.
"""

import pathlib

import matplotlib.pyplot

import pymcnp

TALLY = '1'
HERE = pathlib.Path(__file__).parent
OUTPUT = HERE / 'output'
OUTPUT.mkdir(exist_ok=True)

# Reading OUTP.
path = HERE / 'example_00.outp'
outp, _ = pymcnp.Outp.from_file(path)

# Initializing `Plot`
plotter = pymcnp.Plot(outp)

# Ploting.
print(f'Plotting tally #{TALLY} from {path}.')
plotter.to_show(TALLY)
matplotlib.pyplot.show()
matplotlib.pyplot.close()

# Writting PDF.
print(f'Writing plots tally #{TALLY} from {path} to `{OUTPUT}/example_00-{TALLY}.pdf`.')
plotter.to_pdf(TALLY, OUTPUT / f'example_00-{TALLY}.pdf')
