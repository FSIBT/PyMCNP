"""
Examples for creating INP files using ``build``.
"""

import pymcnp

RADIUS_AIR: float = 60
RADIUS_SHIELD: float = 5
RADIUS_LEAD: float = 1

# Creating cell geometries.
geometry_air = pymcnp.utils.types.Geometry('11')
geometry_shield = pymcnp.utils.types.Geometry('12:11')
geometry_lead = pymcnp.utils.types.Geometry('13:12')
geometry_world = pymcnp.utils.types.Geometry('14')

# Creating cells.
cell_air_number = pymcnp.utils.types.Integer(1)
cell_air_material = pymcnp.utils.types.Integer(21)
cell_air_density = pymcnp.utils.types.Real(0.5)
cell_air = pymcnp.inp.Cell(
    number=cell_air_number,
    material=cell_air_material,
    density=cell_air_density,
    geometry=geometry_air,
)
cell_shield_number = pymcnp.utils.types.Integer(2)
cell_shield_material = pymcnp.utils.types.Integer(22)
cell_shield_density = pymcnp.utils.types.Real(0.5)
cell_shield = pymcnp.inp.Cell(
    number=cell_shield_number,
    material=cell_shield_material,
    density=cell_shield_density,
    geometry=geometry_shield,
)
cell_lead_number = pymcnp.utils.types.Integer(3)
cell_lead_material = pymcnp.utils.types.Integer(23)
cell_lead_density = pymcnp.utils.types.Real(0.5)
cell_lead = pymcnp.inp.Cell(
    number=cell_lead_number,
    material=cell_lead_material,
    density=cell_lead_density,
    geometry=geometry_lead,
)
cell_world_number = pymcnp.utils.types.Integer(4)
cell_world_material = pymcnp.utils.types.Integer(0)
cell_world = pymcnp.inp.Cell(
    number=cell_world_number,
    material=cell_world_material,
    density=None,
    geometry=geometry_world,
)

# Creating surface options.
rpp_air_xmin = pymcnp.utils.types.Real(-RADIUS_AIR)
rpp_air_xmax = pymcnp.utils.types.Real(RADIUS_AIR)
rpp_air_ymin = pymcnp.utils.types.Real(-RADIUS_AIR)
rpp_air_ymax = pymcnp.utils.types.Real(RADIUS_AIR)
rpp_air_zmin = pymcnp.utils.types.Real(-RADIUS_AIR)
rpp_air_zmax = pymcnp.utils.types.Real(RADIUS_AIR)
rpp_air = pymcnp.inp.surface.Rpp(
    xmin=rpp_air_xmin,
    xmax=rpp_air_xmax,
    ymin=rpp_air_ymin,
    ymax=rpp_air_ymax,
    zmin=rpp_air_zmin,
    zmax=rpp_air_zmax,
)
rpp_shield_xmin = pymcnp.utils.types.Real(-RADIUS_SHIELD)
rpp_shield_xmax = pymcnp.utils.types.Real(RADIUS_SHIELD)
rpp_shield_ymin = pymcnp.utils.types.Real(-RADIUS_SHIELD)
rpp_shield_ymax = pymcnp.utils.types.Real(RADIUS_SHIELD)
rpp_shield_zmin = pymcnp.utils.types.Real(-RADIUS_SHIELD)
rpp_shield_zmax = pymcnp.utils.types.Real(RADIUS_SHIELD)
rpp_shield = pymcnp.inp.surface.Rpp(
    xmin=rpp_shield_xmin,
    xmax=rpp_shield_xmax,
    ymin=rpp_shield_ymin,
    ymax=rpp_shield_ymax,
    zmin=rpp_shield_zmin,
    zmax=rpp_shield_zmax,
)
rpp_lead_xmin = pymcnp.utils.types.Real(-RADIUS_LEAD)
rpp_lead_xmax = pymcnp.utils.types.Real(RADIUS_LEAD)
rpp_lead_ymin = pymcnp.utils.types.Real(-RADIUS_LEAD)
rpp_lead_ymax = pymcnp.utils.types.Real(RADIUS_LEAD)
rpp_lead_zmin = pymcnp.utils.types.Real(-RADIUS_LEAD)
rpp_lead_zmax = pymcnp.utils.types.Real(RADIUS_LEAD)
rpp_lead = pymcnp.inp.surface.Rpp(
    xmin=rpp_lead_xmin,
    xmax=rpp_lead_xmax,
    ymin=rpp_lead_ymin,
    ymax=rpp_lead_ymax,
    zmin=rpp_lead_zmin,
    zmax=rpp_lead_zmax,
)
so_world_r = pymcnp.utils.types.Real(RADIUS_AIR + RADIUS_SHIELD + RADIUS_LEAD + 1)
so_world = pymcnp.inp.surface.So(
    r=so_world_r,
)

# Creating surfaces.
surface_air_number = pymcnp.utils.types.Integer(11)
surface_air = pymcnp.inp.Surface(
    number=surface_air_number,
    option=rpp_air,
)
surface_shield_number = pymcnp.utils.types.Integer(12)
surface_shield = pymcnp.inp.Surface(
    number=surface_shield_number,
    option=rpp_shield,
)
surface_lead_number = pymcnp.utils.types.Integer(13)
surface_lead = pymcnp.inp.Surface(
    number=surface_lead_number,
    option=rpp_lead,
)
surface_world_number = pymcnp.utils.types.Integer(99)
surface_world = pymcnp.inp.Surface(
    number=surface_world_number,
    option=so_world,
)

# Creating data options.
n14 = pymcnp.utils.types.Zaid(7, 14)
n15 = pymcnp.utils.types.Zaid(7, 15)
o16 = pymcnp.utils.types.Zaid(8, 16)
o17 = pymcnp.utils.types.Zaid(8, 17)
o18 = pymcnp.utils.types.Zaid(8, 18)
ti46 = pymcnp.utils.types.Zaid(22, 46)
ti47 = pymcnp.utils.types.Zaid(22, 47)
ti48 = pymcnp.utils.types.Zaid(22, 48)
ti49 = pymcnp.utils.types.Zaid(22, 49)
ti50 = pymcnp.utils.types.Zaid(22, 50)
pb204 = pymcnp.utils.types.Zaid(82, 204)
pb206 = pymcnp.utils.types.Zaid(82, 206)
pb207 = pymcnp.utils.types.Zaid(82, 207)
pb208 = pymcnp.utils.types.Zaid(82, 208)

n14_frac = pymcnp.utils.types.Real(-0.797088)
n15_frac = pymcnp.utils.types.Real(-0.002912)
o16_frac_air = pymcnp.utils.types.Real(-0.199514)
o16_frac_shield = pymcnp.utils.types.Real(-0.19984179019595494)
o16_frac_lead = pymcnp.utils.types.Real(-0.03575396279808631)
o17_frac_air = pymcnp.utils.types.Real(-7.6e-05)
o17_frac_shield = pymcnp.utils.types.Real(-7.612486369323746e-05)
o17_frac_lead = pymcnp.utils.types.Real(-1.361960149490542e-05)
o18_frac_air = pymcnp.utils.types.Real(-0.00041000000000000005)
o18_frac_shield = pymcnp.utils.types.Real(-0.00041067360676614944)
o18_frac_lead = pymcnp.utils.types.Real(-7.347416595935819e-05)
ti46_frac = pymcnp.utils.types.Real(-0.02472289143502082)
ti47_frac = pymcnp.utils.types.Real(-0.02229555300321877)
ti48_frac = pymcnp.utils.types.Real(-0.22091776443511935)
ti49_frac = pymcnp.utils.types.Real(-0.016212223353146985)
ti50_frac = pymcnp.utils.types.Real(-0.015522979107079737)
pb204_frac_shield = pymcnp.utils.types.Real(-0.006498225208082432)
pb204_frac_lead = pymcnp.utils.types.Real(-0.014)
pb206_frac_shield = pymcnp.utils.types.Real(-0.11186230536770471)
pb206_frac_lead = pymcnp.utils.types.Real(-0.241)
pb207_frac_shield = pymcnp.utils.types.Real(-0.10257912649901553)
pb207_frac_lead = pymcnp.utils.types.Real(-0.221)
pb208_frac_shield = pymcnp.utils.types.Real(-0.24321928635965673)
pb208_frac_lead = pymcnp.utils.types.Real(-0.524)

n14_substance = pymcnp.utils.types.Substance(n14, n14_frac)
n15_substance = pymcnp.utils.types.Substance(n15, n15_frac)
o16_substance_air = pymcnp.utils.types.Substance(o16, o16_frac_air)
o16_substance_shield = pymcnp.utils.types.Substance(o16, o16_frac_shield)
o16_substance_lead = pymcnp.utils.types.Substance(o16, o16_frac_lead)
o17_substance_air = pymcnp.utils.types.Substance(o17, o17_frac_air)
o17_substance_shield = pymcnp.utils.types.Substance(o17, o17_frac_shield)
o17_substance_lead = pymcnp.utils.types.Substance(o17, o17_frac_lead)
o18_substance_air = pymcnp.utils.types.Substance(o18, o18_frac_air)
o18_substance_shield = pymcnp.utils.types.Substance(o18, o18_frac_shield)
o18_substance_lead = pymcnp.utils.types.Substance(o18, o18_frac_lead)
ti46_substance = pymcnp.utils.types.Substance(ti46, ti46_frac)
ti47_substance = pymcnp.utils.types.Substance(ti47, ti47_frac)
ti48_substance = pymcnp.utils.types.Substance(ti48, ti48_frac)
ti49_substance = pymcnp.utils.types.Substance(ti49, ti49_frac)
ti50_substance = pymcnp.utils.types.Substance(ti50, ti50_frac)
pb204_substance_shield = pymcnp.utils.types.Substance(pb204, pb204_frac_shield)
pb204_substance_lead = pymcnp.utils.types.Substance(pb204, pb204_frac_lead)
pb206_substance_shield = pymcnp.utils.types.Substance(pb206, pb206_frac_shield)
pb206_substance_lead = pymcnp.utils.types.Substance(pb206, pb206_frac_lead)
pb207_substance_shield = pymcnp.utils.types.Substance(pb207, pb207_frac_shield)
pb207_substance_lead = pymcnp.utils.types.Substance(pb207, pb207_frac_lead)
pb208_substance_shield = pymcnp.utils.types.Substance(pb208, pb208_frac_shield)
pb208_substance_lead = pymcnp.utils.types.Substance(pb208, pb208_frac_lead)

material_air_suffix = pymcnp.utils.types.Integer(21)
material_shield_suffix = pymcnp.utils.types.Integer(22)
material_lead_suffix = pymcnp.utils.types.Integer(23)
material_air_substances = pymcnp.utils.types.Tuple(
    [
        o16_substance_air,
        o17_substance_air,
        o18_substance_air,
        n14_substance,
        n15_substance,
    ]
)
material_shield_substances = pymcnp.utils.types.Tuple(
    [
        o16_substance_shield,
        o17_substance_shield,
        o18_substance_shield,
        ti46_substance,
        ti47_substance,
        ti48_substance,
        ti49_substance,
        ti50_substance,
        pb204_substance_shield,
        pb206_substance_shield,
        pb207_substance_shield,
        pb208_substance_shield,
    ]
)
material_lead_substances = pymcnp.utils.types.Tuple(
    [
        o16_substance_lead,
        o17_substance_lead,
        o18_substance_lead,
        pb204_substance_lead,
        pb206_substance_lead,
        pb207_substance_lead,
        pb208_substance_lead,
    ]
)
material_air = pymcnp.inp.data.M_0(suffix=material_air_suffix, substances=material_air_substances)
material_shield = pymcnp.inp.data.M_0(suffix=material_shield_suffix, substances=material_shield_substances)
material_lead = pymcnp.inp.data.M_0(suffix=material_lead_suffix, substances=material_lead_substances)

# Creating data.
data_air = pymcnp.inp.Data(material_air)
data_shield = pymcnp.inp.Data(material_shield)
data_lead = pymcnp.inp.Data(material_lead)

# Creating inp parameters.
title = pymcnp.utils.types.String('Create ``Inp`` Using ``build``\n')
cells = pymcnp.utils.types.Tuple([cell_air, cell_shield, cell_lead, cell_world])
surfaces = pymcnp.utils.types.Tuple([surface_air, surface_shield, surface_lead, surface_world])
data = pymcnp.utils.types.Tuple([data_air, data_shield, data_lead])

# Creating inp.
inp = pymcnp.Inp(
    title=title,
    cells=cells,
    surfaces=surfaces,
    data=data,
)

print(inp)
