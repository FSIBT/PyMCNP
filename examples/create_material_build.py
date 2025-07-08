"""
Examples for creating INP materials using ``build``.
"""

import pymcnp

# Creating material.
material = pymcnp.inp.data.MBuilder_0(
    suffix=1, substances=['001001 0.1118855432927602', '001002 1.2868317335160966e-05', '008016 0.8859435015301171', '008017 0.00033747860358816377', '008018 0.0018206082561993046']
).build()

print(material)
