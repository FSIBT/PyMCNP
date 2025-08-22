"""
Example plotting OUTP files using `Plot`.

This example plots tally #1 from `example_00.outp` using `to_show`, and it
writes the plots to a pdf file using `to_pdf`.
"""

import pathlib

import matplotlib.pyplot

import pymcnp

TALLY = '1'

# Reading OUTP.
path = pathlib.Path('example_00.outp')
outp = pymcnp.Outp.from_file(path)

# Initializing `Plot`
plotter = pymcnp.Plot(outp)

# Ploting.
print(f'Plotting tally #{TALLY} from {path}.')
plotter.to_show(TALLY)
matplotlib.pyplot.show()
matplotlib.pyplot.close()

# Writting PDF.
print(f'Writing plots tally #{TALLY} from {path} to `example_00-{TALLY}.pdf`.')
plotter.to_pdf(TALLY, f'example_00-{TALLY}.pdf')
