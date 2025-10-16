import pytest

import pymcnp
from ... import consts
from ... import classes


class Test_Cell:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Cell
        EXAMPLES_VALID = [
            {
                'number': consts.string.types.INTEGER,
                'material': consts.string.types.INTEGER,
                'density': consts.string.types.REAL,
                'geometry': consts.string.types.GEOMETRY,
                'options': [consts.string.inp.cell.IMP],
            },
            {
                'number': 1,
                'material': 1,
                'density': 3.1,
                'geometry': consts.string.types.GEOMETRY,
                'options': [consts.string.inp.cell.IMP],
            },
            {
                'number': consts.ast.types.INTEGER,
                'material': consts.ast.types.INTEGER,
                'density': consts.ast.types.REAL,
                'geometry': consts.ast.types.GEOMETRY,
                'options': [consts.ast.inp.cell.IMP],
            },
            {'number': consts.string.types.INTEGER, 'material': consts.ast.inp.M_0, 'density': consts.string.types.REAL, 'geometry': consts.ast.inp.SURFACE, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'number': None, 'material': consts.string.types.INTEGER, 'density': consts.string.types.REAL, 'geometry': consts.string.types.GEOMETRY, 'options': [consts.string.inp.cell.IMP]},
            {
                'number': consts.string.types.INTEGER,
                'material': '0',
                'density': consts.string.types.REAL,
                'geometry': consts.string.types.GEOMETRY,
                'options': [consts.string.inp.cell.IMP],
            },
            {
                'number': consts.string.types.INTEGER,
                'material': consts.string.types.INTEGER,
                'density': None,
                'geometry': consts.string.types.GEOMETRY,
                'options': [consts.string.inp.cell.IMP],
            },
            {'number': consts.string.types.INTEGER, 'material': None, 'density': consts.string.types.REAL, 'geometry': consts.string.types.GEOMETRY, 'options': [consts.string.inp.cell.IMP]},
            {'number': consts.string.types.INTEGER, 'material': consts.string.types.REAL, 'density': consts.string.types.INTEGER, 'geometry': None, 'options': [consts.string.inp.cell.IMP]},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Cell
        EXAMPLES_VALID = [
            # 1.3
            '1 0 -7',
            '2 0 -8',
            '3 0 1 -2 -3 4 -5 6 7 8',
            '4 0 -1 : 2 : 3 : -4 : 5 : -6',
            '1 1 -0.0014 -7 IMP:N=1',
            '1 0 -7 IMP:N=1',
            '1 1 -0.0014 -7',
            '2 2 -7.86 -8',
            '3 3 -1.60 1 -2 -3 4 -5 6 7 8',
            '4 0 -1:2:3:-4:5:-6',
            # 3.2
            '3 0 -1 2 -4 $ definition of cell 3',
            '5 0 #3',
            '5 0 #(-1 2 -4)',
            '5 0 (+1 : -2 : +4)',
            '2 3 -3.7 -1 IMP:N=2 IMP:P=4',
            '10 16 -4.2 1 -2 3 IMP:N=4 IMP:P=8 EXT:N=-0.4',
            '3 0 -1.2 -1.1 1.4 -1.5 -1.6 99',
            '4 0 1.1 -2001.1 -5.3 -5.5 -5.6 -5.4',
            '5 0 -5',
            '1 0 -1',
            '9 0 (-5.1:1.3:2001.1:-99:5.5:5.6) #5',
            '3 0 5.1 -1.1 -5.3 -5.5 -5.6 99',
            '3 0 5.1 -1.1 1.4 -5.5 -5.6 -5.4',
            '3 0 -1.2 -1.1 -5.3 -5.5 -5.6 -5.4',
            '1 0 1 -2 3 $ cell 1',
            # 3.3
            '1 0 -17 $ rcc can',
            '1 0 1 -2 -3 4 -5 6 fill=1',
            '2 0 -7 1 -3 8 u=1 fill=2 lat=1',
            '3 0 -11 u=-2',
            '4 0 11 u=2',
            '5 0 -1:2:3:-4:5:-6',
            '5 0 20',
            '999 0 -999 $ cookie cutter cell CCC',
            '1 0 -2 1 -3 $ inside cylinder 2, right of plane 1, left of plane 3',
            '2 0 -4 3 -5 $ inside cylinder 4, right of plane 3, left of plane 5',
            '3 0 (2 3): 1:4:5 $ parentheses used for clarity; not required',
            '3 0 4: 1:5:(2 3) $ parentheses not required',
            '3 0 (1:2) (-3:4):5 $ parentheses are requireed for correctness',
            '3 0 #1 #2 $ everything that is “not” cell 1 or 2',
            # 4.1
            '1 0 -1 : -2',
            '2 0 1 2',
            '1 0 -1 2',
            '2 0 -2 1',
            '3 0 4 0 3',
            '1 0 1 -2 -3',
            '2 0 3 -4 -5',
            '3 0 5 -6 -7',
            '4 0 #1 #2 #3 -8 $ or (-1:4:7:2 -3:5 6) -8',
            '5 0 8 $ everything outside the outer sphere',
            '1 0 -1',
            '2 0 -2 1',
            '3 0 -3 2 (-4:5:-6:7:8:-9) $ These parentheses are required.',
            '4 0 3',
            '5 0 4 -5 6 -7 -8 9',
            '3 0 -3 2 #(4 -5 6 -7 -8 9)',
            '3 0 -3 2 #5',
            '5 0 -4 $ Cell card',
            '1 0 -2 -3 4 1 5 -6',
            '2 0 -7 -8 9 10 11 -12\n    (2 : 3 : -4 : -1 : -5 : 6)',
            '3 0 -13 -14 15 16 17 -18\n    (7 : 8 : -9 : -10 : -11 : 12)',
            '4 0 13 : 14 : -15: -16 : -17: 18',
            '1 0 -1 4',
            '2 0 -2 (1 : -4)',
            '3 0 2',
            '1 0 -1 : -4',
            '2 0 -2 1 4',
            '3 0 2',
            '9 0 -3 -2 4 1 8 -9',
            '17 0 -5 (3 : -4 : -1 : 2 : 9 : -8) : -6 : -7',
            '22 0 5 6 7',
            '9 0 -3 -2 4 1 8 -9',
            '17 0 -5 (3 : -4 : -1 : 2 : 9 : -8) : -6 -7',
            '22 0 5 (6 : 7)',
            '1 0 1 2 -3 (-4 : -5) -6 7',
            '2 0 -1 : -2 : 3 : 4 5 : 6 : -7',
            '1 0 -8:(-5 8.5)',
            '2 0 #1 $ or -8.4:-8.6:8.3:(8.5 5):8.1:-8.2',
            '1 0 -1 2 3 (-4 : -16) 5 -6 (12 : 13 : -14)\n    (10 : -9 : -11 : -7 : 8) 15',
            '2 0 -10 9 11 7 -8 -1 : 2 -12 14 -6 -13 3',
            '3 0 -17 (1 : -2 : -5 : 6 : -3 : -15 : 16 4)',
            '4 0 17',
            '1 0 (2 -1 -5 (7:8:-6)):(4 -3 5(-6:8:7))',
            '2 0 -8 6 -7',
            '3 0 (-2:1:5) (-4:3:-5)',
            '1 0 (2 -1 -5:4 -3 5) (-6:8:7)',
            '1 0 1 -2 -23',
            '2 0 -3 25 -24 2',
            '3 0 3 -5 12 -15 16 -11',
            '4 0 5 -6 12 -17 18 -11',
            '5 0 6 -8 12 -13 -19 20',
            '6 0 8 -9 -26',
            '7 0 -12 4 -7 -27',
            '8 0 -12 7 -10 14 -21 22',
            '9 0 2 -3 -25',
            '10 0 (-1:2:23) (3:-25:24:-2)\n    (-3:5:-12:15:-16:11)\n    (-5:6:-12:17:-18:11)\n    (-6:8:-12:13:19:-20)\n    (-8:9:26) (12:-4:7:27)\n    (12:-7:10:-14:21:-22)\n    (-2:3:25) -28',
            '10 0 #1 #2 #3 #4 #5 #6 #7 #8 #9 -28',
            '3 0 8 -9 -10 11 -12 13 #2 #1',
            '4 0 -11 12 -14 13 imp:n=1 lat=1 u=1 fill=3',
            consts.string.inp.CELL,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]

    class Test_Show:
        EXAMPLES: list[str] = [
            '1 0 +1',
            '1 0 (1)',
            '1 0 1',
        ]

        def test_valid(self):
            """
            Tests `EXAMPLES` on `to_show`.
            """

            for example in self.EXAMPLES:
                pymcnp.inp.Cell.from_mcnp(example).to_show({'1': consts.ast._show.pyvista.SPHERE}, {})

        def test_invalid(self):
            """
            Tests `EXAMPLES` on `to_show`.
            """

            for example in self.EXAMPLES:
                with pytest.raises(pymcnp.errors.TypesError):
                    pymcnp.inp.Cell.from_mcnp(example).to_show({}, {})
