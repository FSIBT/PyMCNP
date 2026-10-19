"""
Example creating INP files.

This example creates an INP file. First, it creates surfaces, and second,
it defines materials. Third, it defines cells by combining geometries using
operators and assigning materials. Fourth, it creates a point source and a
type #4 tally. Fifth, it creates a INP file using `Inp` and prints the result.
"""

import pymcnp

RADIUS_WORLD: float = 100
RADIUS_INNER: float = 50
RADIUS_OUTER: float = 10

# Creating surfaces.
surface_inner = pymcnp.inp.card.surface.Rpp(
    j='21',
    xmin=-RADIUS_INNER,
    xmax=RADIUS_INNER,
    ymin=-RADIUS_INNER,
    ymax=RADIUS_INNER,
    zmin=-RADIUS_INNER,
    zmax=RADIUS_INNER,
)
surface_outer = pymcnp.inp.card.surface.Rpp(
    j='22',
    xmin=-RADIUS_OUTER,
    xmax=RADIUS_OUTER,
    ymin=-RADIUS_OUTER,
    ymax=RADIUS_OUTER,
    zmin=-RADIUS_OUTER,
    zmax=RADIUS_OUTER,
)
surface_world = pymcnp.inp.card.surface.So(
    j='99',
    r=RADIUS_WORLD,
)

# Creating materials.
material_air = pymcnp.inp.card.data.M.from_formula(suffix=31, formulas={'N2': 0.8, 'O2': 0.2})
material_lead = pymcnp.inp.card.data.M.from_formula(suffix=32, formulas={'Pb': 1})

# Creating cells.
imp = pymcnp.inp.option.cell.Imp(particle='n', x=1)
cell_inside = pymcnp.inp.card.Cell_1(j=1, m=0, geom=-surface_inner, options=[imp])
cell_shield = pymcnp.inp.card.Cell_0(j=2, m=material_lead.suffix, d=0.5, geom=+surface_inner & -surface_outer, options=[imp])
cell_air = pymcnp.inp.card.Cell_0(j=3, m=material_air.suffix, d=0.5, geom=-surface_inner | (+surface_outer & -surface_world), options=[imp])
cell_world = pymcnp.inp.card.Cell_1(j=4, m=0, geom=+surface_world, options=[imp])

# Creating source.
source = pymcnp.inp.card.data.Sdef(options=['POS=0 0 0', 'ERG=14.4', 'PAR=1'])

# Creating tally.
tally = pymcnp.inp.card.data.F_0(
    suffix=4,
    particle='n',
    s=[2],
)

# Creating inp.
inp = pymcnp.Inp(
    title='Create `Inp`\n',
    cells=[cell_inside, cell_shield, cell_air, cell_world],
    surfaces=[surface_inner, surface_outer, surface_world],
    data=[material_air, material_lead, source, tally],
)
inp.nps = int(1e5)
inp.seed = 1232209489

print('INP file created using `__init__`:')
print(inp)
