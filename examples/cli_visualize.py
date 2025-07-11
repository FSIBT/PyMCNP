"""
Examples for visualizing INP files using ``Visualize``.
"""

import pathlib

import pymcnp

# Reading INP.
inp = pymcnp.Inp.from_file(pathlib.Path(__file__).parent / 'files' / 'inp' / 'F1F8.i')

# Visualizing surfaces using ``Visualize``.
visualizer = pymcnp.cli.Visualize(inp)
visualizer.to_show_surfaces().plot()

# Converting to PDF.
visualizer.to_pdf_surfaces('F1F8-surfaces.pdf')
