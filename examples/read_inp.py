"""
Example reading INP files.
"""

import pathlib

import pymcnp

RADIUS_AIR: float = 60
RADIUS_SHIELD: float = 5
RADIUS_LEAD: float = 1

# Reading INP using `from_file`.
path = pathlib.Path(__file__).parent.parent / 'files' / 'inp' / 'example_00.inp'
inp = pymcnp.Inp.from_file(path)

print(inp)

# Reading INP using `from_mcnp`.
inp = pymcnp.Inp.from_mcnp(f"""Create `Inp` Using `build`
c ============================================================================
c                                    cells                                    
c ============================================================================
1 21 0.5 11
2 22 0.5 (12):(11)
3 23 0.5 (13):(12)
4 0 14

c ============================================================================
c                                   surfaces                                  
c ============================================================================
11 rpp -{RADIUS_AIR} {RADIUS_AIR} -{RADIUS_AIR} {RADIUS_AIR} -{RADIUS_AIR} {RADIUS_AIR}
11 rpp -{RADIUS_SHIELD} {RADIUS_SHIELD} -{RADIUS_SHIELD} {RADIUS_SHIELD} -{RADIUS_SHIELD} {RADIUS_SHIELD}
11 rpp -{RADIUS_LEAD} {RADIUS_LEAD} -{RADIUS_LEAD} {RADIUS_LEAD} -{RADIUS_LEAD} {RADIUS_LEAD}
99 so {RADIUS_AIR + RADIUS_SHIELD + RADIUS_LEAD + 1}

c ============================================================================
c                                     data                                    
c ============================================================================
m21 007014 -0.797088 007015 -0.002912 008016 -0.199514 008017 -7.6e-05 008018 &
      -0.00041000000000000005
m22 008016 -0.19984179019595494 008017 -7.612486369323746e-05 008018 &
      -0.00041067360676614944 022046 -0.02472289143502082 022047 &
      -0.02229555300321877 022048 -0.22091776443511935 022049 &
      -0.016212223353146985 022050 -0.015522979107079737 008016 &
      -0.03575396279808631 008017 -1.361960149490542e-05 008018 &
      -7.347416595935819e-05 082204 -0.006498225208082432 082206 &
      -0.11186230536770471 082207 -0.10257912649901553 082208 &
      -0.24321928635965673
m23 082204 -0.014 082206 -0.241 082207 -0.221 082208 -0.524
""")

print(inp)
