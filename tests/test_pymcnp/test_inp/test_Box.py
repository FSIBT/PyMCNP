import pytest

import pymcnp
from ... import consts
from ... import classes


class Test_Box:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Box
        EXAMPLES_VALID = [
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {'prefix': '*', 'number': 1, 'transform': 1, 'vx': 3.1, 'vy': 3.1, 'vz': 3.1, 'a1x': 1, 'a1y': 0, 'a1z': 0, 'a2x': 0, 'a2y': 1, 'a2z': 0, 'a3x': 0, 'a3y': 0, 'a3z': 1},
            {
                'prefix': pymcnp.types.String('*'),
                'number': consts.ast.types.INTEGER,
                'transform': consts.ast.types.INTEGER,
                'vx': consts.ast.types.REAL,
                'vy': consts.ast.types.REAL,
                'vz': consts.ast.types.REAL,
                'a1x': pymcnp.types.Real(1),
                'a1y': pymcnp.types.Real(0),
                'a1z': pymcnp.types.Real(0),
                'a2x': pymcnp.types.Real(0),
                'a2y': pymcnp.types.Real(1),
                'a2z': pymcnp.types.Real(0),
                'a3x': pymcnp.types.Real(0),
                'a3y': pymcnp.types.Real(0),
                'a3z': pymcnp.types.Real(1),
            },
            {
                'prefix': None,
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': None,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': None,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
        ]
        EXAMPLES_INVALID = [
            {
                'prefix': 'a',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': '0',
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': '1000',
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': None,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': None,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': None,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': None,
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': None,
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': None,
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': None,
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': None,
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': None,
                'a3x': '0',
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': None,
                'a3y': '0',
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': None,
                'a3z': '1',
            },
            {
                'prefix': '*',
                'number': consts.string.types.INTEGER,
                'transform': consts.string.types.INTEGER,
                'vx': consts.string.types.REAL,
                'vy': consts.string.types.REAL,
                'vz': consts.string.types.REAL,
                'a1x': '1',
                'a1y': '0',
                'a1z': '0',
                'a2x': '0',
                'a2y': '1',
                'a2z': '0',
                'a3x': '0',
                'a3y': '0',
                'a3z': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Box
        EXAMPLES_VALID = [
            # 4.1
            '8 box -2.5 -2.5 0 5 0 0 0 5 0 0 0 5',
            consts.string.inp.BOX,
        ]
        EXAMPLES_INVALID = ['hello']

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Box
        EXAMPLES = [consts.string.inp.BOX]

    class Test_Operations(classes.Test_Operations):
        EXAMPLES = [(consts.ast.inp.BOX, consts.ast.inp.BOX)]


class Test_Box_Orthogonality:
    ORTHOGONAL = (1, 0, 0, 0, 1, 0, 0, 0, 1)

    def box(self, vectors):
        return pymcnp.inp.Box(0, 0, 0, *vectors, number=1)

    def test_valid(self):
        """
        Tests orthogonal, scaled and slightly skewed (within MCNP's tolerance) vectors.
        """

        assert self.box(self.ORTHOGONAL).to_mcnp() == '1  box 0 0 0 1 0 0 0 1 0 0 0 1'
        self.box((2, 0, 0, 0, 3, 0, 0, 0, 4))
        self.box((1, 0, 0, 0.01, 1, 0, 0, 0, 1))

    def test_invalid(self):
        """
        Tests non-orthogonal and zero-length vectors, as rejected by MCNP.
        """

        for vectors in [(1, 0, 0, 1, 1, 0, 0, 0, 1), (1, 0, 0, 0, 1, 0, 1, 0, 1), (0, 0, 0, 0, 1, 0, 0, 0, 1)]:
            with pytest.raises(pymcnp.errors.InpError):
                self.box(vectors)

    def test_mutation(self):
        """
        Tests that assigning a component that breaks orthogonality is rejected.
        """

        box = self.box(self.ORTHOGONAL)

        with pytest.raises(pymcnp.errors.InpError):
            box.a2x = 1
        assert str(box.a2x) == '0'
