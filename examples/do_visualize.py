"""
Example visualizing INP files using `Visualize`.

This example visualizes the surfaces in `valid_29.inp` INP file using
`to_show_surfaces`, and it generates a PDF file containing the images.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path(__file__).parent.parent / 'files' / 'inp' / 'valid_29.inp'
inp = pymcnp.Inp.from_file(path)

# Visualizing surfaces.
print(f'Visualizing all surfaces from `{path}`.')
visualizer = pymcnp.Visualize(inp)
visualizer.to_show_surfaces().show()

# Converting to PDF.
print(f'Writing visualizations of all surfaces from `{path}` to `valid_29-surfaces.pdf`')
visualizer.to_pdf_surfaces('valid_29-surfaces.pdf')
