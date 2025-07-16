import pymcnp
from ... import consts
from ... import classes


class Test_Like:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Like
        EXAMPLES_VALID = [
            {
                'number': consts.string.types.INTEGER,
                'cell': consts.string.types.INTEGER,
                'options': [consts.string.inp.like.IMP],
            },
            {
                'number': 1,
                'cell': 2,
                'options': [consts.ast.inp.like.IMP],
            },
            {
                'number': consts.ast.types.INTEGER,
                'cell': consts.ast.types.INTEGER,
                'options': [consts.ast.inp.like.IMP],
            },
            {'number': consts.string.types.INTEGER, 'cell': consts.string.types.INTEGER, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'number': None, 'cell': consts.string.types.INTEGER, 'options': [consts.string.inp.like.IMP]},
            {
                'number': consts.string.types.INTEGER,
                'cell': None,
                'options': [consts.string.inp.like.IMP],
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Like
        EXAMPLES_VALID = [
            # 3.2
            '3 LIKE 2 BUT IMP:N=10 TRCL=1',
            '2 like 1 but trcl = (2 0 0)',
            # 3.3
            '21 like 1 but *trcl=(20 0 0 45 -45 90 135 45 90 90 90 0)',
            consts.string.inp.LIKE,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]
