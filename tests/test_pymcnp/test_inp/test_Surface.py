import pymcnp
from ... import consts
from ... import classes


class Test_Surface:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Surface
        EXAMPLES_VALID = [
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'option': consts.string.inp.surface.SO},
            {'prefix': '*', 'number': 1, 'transform': 1, 'option': consts.ast.inp.surface.SO},
            {'prefix': pymcnp.types.String('*'), 'number': consts.ast.types.INTEGER, 'transform': consts.ast.types.INTEGER, 'option': consts.ast.inp.surface.SO},
            {'prefix': None, 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'option': consts.string.inp.surface.SO},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': None, 'option': consts.string.inp.surface.SO},
        ]
        EXAMPLES_INVALID = [
            {'prefix': 'a', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'option': consts.string.inp.surface.SO},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': '1000', 'option': consts.string.inp.surface.SO},
            {'prefix': '*', 'number': None, 'transform': consts.string.types.INTEGER, 'option': consts.string.inp.surface.SO},
            {'prefix': '*', 'number': consts.string.types.INTEGER, 'transform': consts.string.types.INTEGER, 'option': None},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Surface
        EXAMPLES_VALID = [
            # 1.3
            '1 PZ -5',
            '1 PZ 5',
            '1 PY 5',
            '1 PY -5',
            '1 PX 5',
            '1 PX -5',
            '7 S 0 -4 -2.5 0.5 $ oxygen sphere',
            '8 S 0 4 4 0.5 $ iron sphere',
            # 3.2
            '1 PY 3',
            '3 K/Y 0 0 2 0.25 1',
            '11 GQ 1 0.25 0.75 0 -0.866\n 0 -12 -2 3.464 39',
            '11 7 CX 1',
            '12 X 7 5 3 2 4 3',
            '12 SQ -0.083333333 1 1 0 0 0 68.52083 -26.5 0 0.',
            '12 Y 1 2 1 3 3 4',
            '12 Y 3 0 4 1 5 0',
            '12 Z 1 0 2 1 3 4',
            '12 Z 2 1 3 4 5 9.380832',
            '1 Y -3 2 2 1 $ surface 1',
            '2 Y 2 3 3 3 4 2 $ surface 2',
            '3 Y 2 1 4 1 4 2 $ surface 3',
            '3 SQ 1 -1.5 1 0 0 0 -0.625 0 2.5 0',
            '5 rpp -2 0 -2 0 -1 1',
            '1 rpp 0 2 0 2 -1 1',
            '99 py -2',
            # 3.3
            '17 4 RCC 0 0 0 0 12 0 5',
            '11 4 PX 5',
            '11 PY 4.1',
            '1 px 0',
            '2 px 50',
            '3 py 10',
            '4 py -10',
            '5 pz 5',
            '6 pz -5',
            '7 px 10',
            '8 py 0',
            '10 py 10',
            '11 s 5 5 0 4',
            '11 s 5 5 0 4',
            '20 rpp 0 50 -10 10 -5 5',
            '30 rpp 0 10 0 10',
            '11 s 5 5 0 4',
            '999 SQ 25 100 0 0 0 0 -4 0 0 0 $ surface for cell CCC',
            # 4.1
            '1 PX 0 $ plane perpendicular to the X axis at x=0',
            '2 CX 2 $ cylinder on the X axis of radius 2',
            '3 PX 2 $ plane perpendicular to the X axis at x=2',
            '4 CX 3 $ cylinder on the X axis of radius 3',
            '5 PX 6 $ plane perpendicular to the X axis at x=6',
            '1 PX -3',
            '2 CX 2',
            '3 PX -1',
            '4 CX 5',
            '5 PX 1',
            '6 CX 3.5',
            '7 PX 3',
            '8 SO 8',
            '1 rcc 0 -2 0 0 4 0 4',
            '2 rcc 0 0 0 0 0 7 1',
            '4 rpp 2 4 7.5 8.5 -2 2 $ Surface card',
            '5 kz 8 0.25 -1',
            '8 box -2.5 -2.5 0 5 0 0 0 5 0 0 0 5',
            '1 1 CY 4',
            '2 1 PY -7',
            '3 1 PY 7',
            # 4.2
            '7 PX 0.5',
            '8 PX -0.5',
            '9 PZ 0.5',
            '10 PZ -0.5',
            consts.string.inp.SURFACE,
        ]
        EXAMPLES_INVALID = ['hello']

    class Test_Operations:
        EXAMPLES = [
            (consts.ast.inp.SURFACE, consts.ast.inp.SURFACE),
        ]

        def test_and(self):
            """
            Tests `EXAMPLES` on `__and__`.
            """

            for a, b in self.EXAMPLES:
                a & b

        def test_or(self):
            """
            Tests `EXAMPLES` on `__or__`.
            """

            for a, b in self.EXAMPLES:
                a | b

        def test_neg(self):
            """
            Tests `EXAMPLES` on `__neg__`.
            """

            for a, b in self.EXAMPLES:
                -a

        def test_pos(self):
            """
            Tests `EXAMPLES` on `__pos__`.
            """

            for a, b in self.EXAMPLES:
                +a

        def test_invert(self):
            """
            Tests `EXAMPLES` on `__or__`.
            """

            for a, b in self.EXAMPLES:
                ~a

    class Test_Show(classes.Test_Show):
        element = pymcnp.inp.Surface
        EXAMPLES = [
            consts.string.inp.SURFACE,
        ]
