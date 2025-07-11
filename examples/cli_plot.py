"""
Examples for plotting OUTP files using ``Plot``.
"""

import pathlib

import matplotlib.pyplot

import pymcnp

TALLY = '1'

# Reading OUTP.
outp = pymcnp.Outp.from_file(pathlib.Path(__file__).parent / 'files' / 'outp' / 'F1F8.o')

# Converting.
plotter = pymcnp.cli.Plot(outp)
plotter.to_show(TALLY)
matplotlib.pyplot.show()

# Writting PDF.
plotter.to_pdf(TALLY, f'F1F8-{TALLY}.pdf')
