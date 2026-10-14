import pymcnp
from .... import consts
from .... import classes


class Test_Sphere:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.f_1.Sphere
        EXAMPLES_VALID = [
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'ro': consts.string.types.REAL,
            },
            {
                'x': 0.5,
                'y': 0.5,
                'z': 1.5,
                'ro': -0.5,
            },
            {
                'x': consts.ast.types.REAL,
                'y': consts.ast.types.REAL,
                'z': consts.ast.types.REAL,
                'ro': consts.ast.types.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x': None,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'ro': consts.string.types.REAL,
            },
            {
                'x': consts.string.types.REAL,
                'y': None,
                'z': consts.string.types.REAL,
                'ro': consts.string.types.REAL,
            },
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': None,
                'ro': consts.string.types.REAL,
            },
            {
                'x': consts.string.types.REAL,
                'y': consts.string.types.REAL,
                'z': consts.string.types.REAL,
                'ro': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.f_1.Sphere
        EXAMPLES_VALID = [consts.string.inp.f_1.SPHERE]
        EXAMPLES_INVALID = ['hello']

    def test_real_coordinates_roundtrip(self):
        """
        Tests that non-integer z and exclusion radius survive a round trip (negative radius is in mean free paths).
        """

        for source in ['1 2 3.5 0.25', '1 2 3 -2.5']:
            assert pymcnp.inp.f_1.Sphere.from_mcnp(source).to_mcnp() == source
