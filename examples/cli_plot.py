"""
Example plotting OUTP files using ``Plot``.
"""

import pathlib

import matplotlib.pyplot

import pymcnp

TALLY = '1'

# Reading OUTP.
path = pathlib.Path(__file__).parent.parent / 'files' / 'outp' / 'example_00.outp'
outp = pymcnp.Outp.from_file(path)

# Plotting.
plotter = pymcnp.Plot(outp)
plotter.to_show(TALLY)
matplotlib.pyplot.show()

# Writting PDF.
plotter.to_pdf(TALLY, f'example_00-{TALLY}.pdf')
