"""
Examples for creating INP files using ``build``.
"""

import pymcnp

RADIUS_AIR: float = 60
RADIUS_SHIELD: float = 5
RADIUS_LEAD: float = 1

# Creating cell geometries.
geometry_air = pymcnp.utils.types.Geometry('11')
geometry_shield = pymcnp.utils.types.Geometry('12')
geometry_lead = pymcnp.utils.types.Geometry('13')
geometry_world = pymcnp.utils.types.Geometry('14')

# Creating cells.
cell_air = pymcnp.inp.Cell(number=1, material=21, density=0.5, geometry=geometry_air)
cell_shield = pymcnp.inp.Cell(number=2, material=22, density=0.5, geometry=geometry_shield & geometry_air)
cell_lead = pymcnp.inp.Cell(number=3, material=23, density=0.5, geometry=geometry_lead & geometry_shield)
cell_world = pymcnp.inp.Cell(number=4, material=0, geometry=geometry_world)

# Creating surface options.
rpp_air = pymcnp.inp.surface.Rpp(
    xmin=-RADIUS_AIR,
    xmax=RADIUS_AIR,
    ymin=-RADIUS_AIR,
    ymax=RADIUS_AIR,
    zmin=-RADIUS_AIR,
    zmax=RADIUS_AIR,
)
rpp_shield = pymcnp.inp.surface.Rpp(
    xmin=-RADIUS_SHIELD,
    xmax=RADIUS_SHIELD,
    ymin=-RADIUS_SHIELD,
    ymax=RADIUS_SHIELD,
    zmin=-RADIUS_SHIELD,
    zmax=RADIUS_SHIELD,
)
rpp_lead = pymcnp.inp.surface.Rpp(
    xmin=-RADIUS_LEAD,
    xmax=RADIUS_LEAD,
    ymin=-RADIUS_LEAD,
    ymax=RADIUS_LEAD,
    zmin=-RADIUS_LEAD,
    zmax=RADIUS_LEAD,
)
so_world = pymcnp.inp.surface.So(r=RADIUS_AIR + RADIUS_SHIELD + RADIUS_LEAD + 1)

# Creating surfaces.
surface_air = pymcnp.inp.Surface(
    number=11,
    option=rpp_air,
)
surface_shield = pymcnp.inp.Surface(
    number=11,
    option=rpp_shield,
)
surface_lead = pymcnp.inp.Surface(
    number=11,
    option=rpp_lead,
)
surface_world = pymcnp.inp.Surface(
    number=99,
    option=so_world,
)

# Creating data options.
material_air = pymcnp.inp.data.M_0.from_formula(number=21, formulas={'N2': 0.8, 'O2': 0.2})
material_shield = pymcnp.inp.data.M_0.from_formula(number=22, formulas={'TiO2': 0.5, 'PbO': 0.5})
material_lead = pymcnp.inp.data.M_0.from_formula(number=23, formulas={'Pb': 1})

# Creating data.
data_air = pymcnp.inp.Data(material_air)
data_shield = pymcnp.inp.Data(material_shield)
data_lead = pymcnp.inp.Data(material_lead)

# Creating inp.
inp = pymcnp.Inp(
    title='Create ``Inp`` Using ``build``\n',
    cells=[cell_air, cell_shield, cell_lead, cell_world],
    surfaces=[surface_air, surface_shield, surface_lead, surface_world],
    data=[data_air, data_shield, data_lead],
)

print(inp)
