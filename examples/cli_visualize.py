"""
Example visualizing INP files using ``Visualize``.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i'
inp = pymcnp.Inp.from_file(path)

# Visualizing surfaces using ``Visualize``.
visualizer = pymcnp.cli.Visualize(inp)
visualizer.to_show_surfaces().show()

# Converting to PDF.
visualizer.to_pdf_surfaces('F1F8-surfaces.pdf')
