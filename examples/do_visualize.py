"""
Example visualizing INP files using `Visualize`.

This example visualizes the surfaces in `example_05.inp` INP file using
`to_show_surfaces`, and it generates a PDF file containing the images.
"""

import pathlib

import pymcnp

# Reading INP.
path = pathlib.Path('example_05.inp')
inp = pymcnp.Inp.from_file(path)

# Visualizing surfaces.
print(f'Visualizing all surfaces from `{path}`.')
visualizer = pymcnp.Visualize(inp)
visualizer.to_show_surfaces(skip=(1,3)).show()

# Converting to PDF.
print(f'Writing visualizations of all surfaces from `{path}` to `example_05-surfaces.pdf`')
visualizer.to_pdf_surfaces('example_05-surfaces.pdf')
