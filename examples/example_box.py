import pymcnp


RADIUS_AIR = 60
RADIUS_SHIELD = 15
RADIUS_LEAD = 1

BOX_AIR = pymcnp.inp.SurfaceOption_Rpp.from_mcnp(
    f'rpp {-RADIUS_AIR} {RADIUS_AIR} {-RADIUS_AIR} {RADIUS_AIR} {-RADIUS_AIR} {RADIUS_AIR}'
)
BOX_SHIELD = pymcnp.inp.SurfaceOption_Rpp.from_mcnp(
    f'rpp {-RADIUS_SHIELD} {RADIUS_SHIELD} {-RADIUS_SHIELD} {RADIUS_SHIELD} {-RADIUS_SHIELD} {RADIUS_SHIELD}'
)
BOX_LEAD = pymcnp.inp.SurfaceOption_Rpp.from_mcnp(
    f'rpp {-RADIUS_LEAD} {RADIUS_LEAD} {-RADIUS_LEAD} {RADIUS_LEAD} {-RADIUS_LEAD} {RADIUS_LEAD}'
)

MATERIAL_AIR = pymcnp.inp.DataOption_M.from_formula(1, {'N2': 0.8, 'O2': 0.2})
MATERIAL_SHIELD = pymcnp.inp.DataOption_M.from_formula(2, {'TiO2': 0.5, 'PbO': 0.5})
MATERIAL_LEAD = pymcnp.inp.DataOption_M.from_formula(3, {'Pb': 1})

inp = pymcnp.inp.Inp.from_mcnp(
    f"""
Box Example
10 1 0.5 20
11 2 0.5 21:20
12 3 0.5 22:21
13 0     23

20 {BOX_AIR}
21 {BOX_SHIELD}
22 {BOX_LEAD}
23 SO {RADIUS_AIR + RADIUS_SHIELD + RADIUS_LEAD + 1}

SDEF X=0 Y=0 Z=0 ERG=2.2
"""[1:-1]
)

print(inp.data)
