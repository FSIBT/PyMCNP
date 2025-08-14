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
surface_inner = pymcnp.inp.Surface(
    option=pymcnp.inp.surface.Rpp(
        xmin=-RADIUS_INNER,
        xmax=RADIUS_INNER,
        ymin=-RADIUS_INNER,
        ymax=RADIUS_INNER,
        zmin=-RADIUS_INNER,
        zmax=RADIUS_INNER,
    ),
)
surface_outer = pymcnp.inp.Surface(
    option=pymcnp.inp.surface.Rpp(
        xmin=-RADIUS_OUTER,
        xmax=RADIUS_OUTER,
        ymin=-RADIUS_OUTER,
        ymax=RADIUS_OUTER,
        zmin=-RADIUS_OUTER,
        zmax=RADIUS_OUTER,
    ),
)
surface_world = pymcnp.inp.Surface(
    option=pymcnp.inp.surface.So(
        r=RADIUS_WORLD,
    ),
)

# Creating materials.
material_air = pymcnp.inp.M_0.from_formula(formulas={'N2': 0.8, 'O2': 0.2})
material_lead = pymcnp.inp.M_0.from_formula(formulas={'Pb': 1})

# Creating cells.
cell_inside = pymcnp.inp.Cell(material=0, geometry=-surface_inner)
cell_shield = pymcnp.inp.Cell(material=material_lead, density=0.5, geometry=+surface_inner & -surface_outer)
cell_air = pymcnp.inp.Cell(material=material_air, density=0.5, geometry=-surface_inner | (+surface_outer & -surface_world))
cell_world = pymcnp.inp.Cell(material=0, geometry=+surface_world)

# Creating source.
source = pymcnp.inp.Sdef(
    options=[
        pymcnp.inp.sdef.Pos_0(0, 0, 0),
        pymcnp.inp.sdef.Erg_0(14.4),
        pymcnp.inp.sdef.Par_0(1),
    ]
)

# Creating tally.
tally = pymcnp.inp.F_0(
    suffix=4,
    designator='n',
    problems=[2],
)

# Creating inp.
inp = pymcnp.Inp(
    title='Create `Inp`\n',
    cells=[cell_inside, cell_shield, cell_air, cell_world],
    surfaces=[surface_inner, surface_outer, surface_world],
    data=[material_air, material_lead, source, tally],
)
inp.nps = 1e5
inp.seed = 1232209489

print('INP file created using `__init__`:')
print(inp)
