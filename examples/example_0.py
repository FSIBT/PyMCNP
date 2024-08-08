"""
'example_0' demonstrates PYMCNP's cadquery functionalities.

Example #0 reads 'example_0_input.inp' and outputs 'example_0_output.py'. To
display the cadquery result, copy the output into a Jupyter notebook and call
'display(surfaces)' after importing cadquery.
"""

import pymcnp

# Reading in MCNP INP.
simulation = pymcnp.files.inp.inp.Inp().from_mcnp_file('files/example_0_input.inp')

# Writing Cadquery.
simulation.surfaces.to_cadquery_file('files/example_0_output.py')
