"""
Examples for creating INP materials using ``__init__``.
"""

import pymcnp

# Creating substances.
h1 = pymcnp.utils.types.Substance(
    pymcnp.utils.types.Zaid(1, 1),
    pymcnp.utils.types.Real(0.1118855432927602),
)
h2 = pymcnp.utils.types.Substance(
    pymcnp.utils.types.Zaid(1, 2),
    pymcnp.utils.types.Real(1.2868317335160966e-05),
)
o16 = pymcnp.utils.types.Substance(
    pymcnp.utils.types.Zaid(8, 16),
    pymcnp.utils.types.Real(0.8859435015301171),
)
o17 = pymcnp.utils.types.Substance(
    pymcnp.utils.types.Zaid(8, 17),
    pymcnp.utils.types.Real(0.00033747860358816377),
)
o18 = pymcnp.utils.types.Substance(
    pymcnp.utils.types.Zaid(8, 18),
    pymcnp.utils.types.Real(0.0018206082561993046),
)

# Creating parameters.
suffix = pymcnp.utils.types.Integer(3)
substances = pymcnp.utils.types.Tuple(
    [
        h1,
        h2,
        o16,
        o17,
        o18,
    ]
)

# Creating material.
material = pymcnp.inp.data.M_0(
    suffix,
    substances,
)

print(material)
