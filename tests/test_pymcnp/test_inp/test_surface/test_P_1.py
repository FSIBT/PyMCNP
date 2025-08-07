import pytest

import pymcnp
from .... import consts
from .... import classes


class Test_P_1:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.surface.P_1
        EXAMPLES_VALID = [
            {
                'x1': '1',
                'y1': '0',
                'z1': '0',
                'x2': '0',
                'y2': '1',
                'z2': '0',
                'x3': '0',
                'y3': '0',
                'z3': '1',
            },
            {
                'x1': 1,
                'y1': 0,
                'z1': 0,
                'x2': 0,
                'y2': 1,
                'z2': 0,
                'x3': 0,
                'y3': 0,
                'z3': 1,
            },
            {
                'x1': pymcnp.types.Real.from_mcnp('1'),
                'y1': pymcnp.types.Real.from_mcnp('0'),
                'z1': pymcnp.types.Real.from_mcnp('0'),
                'x2': pymcnp.types.Real.from_mcnp('0'),
                'y2': pymcnp.types.Real.from_mcnp('1'),
                'z2': pymcnp.types.Real.from_mcnp('0'),
                'x3': pymcnp.types.Real.from_mcnp('0'),
                'y3': pymcnp.types.Real.from_mcnp('0'),
                'z3': pymcnp.types.Real.from_mcnp('1'),
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x1': None,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': None,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': None,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': None,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': None,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': None,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': None,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': None,
                'z3': consts.string.types.REAL,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': None,
            },
            {
                'x1': consts.string.types.REAL,
                'y1': consts.string.types.REAL,
                'z1': consts.string.types.REAL,
                'x2': consts.string.types.REAL,
                'y2': consts.string.types.REAL,
                'z2': consts.string.types.REAL,
                'x3': consts.string.types.REAL,
                'y3': consts.string.types.REAL,
                'z3': consts.string.types.REAL,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.surface.P_1
        EXAMPLES_VALID = [consts.string.inp.surface.P_1]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.surface.P_1
        EXAMPLES = [consts.string.inp.surface.P_1]

    class Test_Properties:
        def test(self):
            element = pymcnp.inp.surface.P_1(1, 0, 0, 0, 0, 0, 0, 0, 1)

            with pytest.raises(pymcnp.errors.InpError):
                element.x1 = 0

            element = pymcnp.inp.surface.P_1(0, 1, 0, 0, 0, 0, 0, 0, 1)

            with pytest.raises(pymcnp.errors.InpError):
                element.y1 = 0

            element = pymcnp.inp.surface.P_1(0, 0, 1, 0, 0, 0, 0, 1, 0)

            with pytest.raises(pymcnp.errors.InpError):
                element.z1 = 0

            element = pymcnp.inp.surface.P_1(0, 0, 0, 1, 0, 0, 0, 0, 1)

            with pytest.raises(pymcnp.errors.InpError):
                element.x2 = 0

            element = pymcnp.inp.surface.P_1(0, 0, 0, 0, 1, 0, 0, 0, 1)

            with pytest.raises(pymcnp.errors.InpError):
                element.y2 = 0

            element = pymcnp.inp.surface.P_1(0, 0, 0, 0, 0, 1, 0, 1, 0)

            with pytest.raises(pymcnp.errors.InpError):
                element.z2 = 0

            element = pymcnp.inp.surface.P_1(0, 0, 1, 0, 0, 0, 1, 0, 0)

            with pytest.raises(pymcnp.errors.InpError):
                element.x3 = 0

            element = pymcnp.inp.surface.P_1(0, 0, 1, 0, 0, 0, 0, 1, 0)

            with pytest.raises(pymcnp.errors.InpError):
                element.y3 = 0
