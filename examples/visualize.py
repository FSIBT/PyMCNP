"""
Examples for visualizing INP files using ``draw``.
"""

import pathlib

import pymcnp

# Reading from file.
inp = pymcnp.Inp.from_file(pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i')

# Visualizing surfaces.
vista = inp.draw()
vista.plot()
