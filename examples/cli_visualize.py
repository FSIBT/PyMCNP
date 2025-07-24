"""
Example visualizing INP files using ``Visualize``.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path(__file__).parent.parent / 'files' / 'inp' / 'example_00.inp'
inp = pymcnp.Inp.from_file(path)

# Visualizing surfaces using ``Visualize``.
visualizer = pymcnp.Visualize(inp)
visualizer.to_show_surfaces().show()

# Converting to PDF.
visualizer.to_pdf_surfaces('example_00-surfaces.pdf')
