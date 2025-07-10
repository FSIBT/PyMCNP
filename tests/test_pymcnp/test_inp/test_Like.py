import pymcnp
from ... import consts
from ... import classes


class Test_Like:
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


class Test_LikeBuilder:
    class Test_Build(classes.Test_Build):
        element = pymcnp.inp.LikeBuilder
        EXAMPLES_VALID = [
            {
                'number': consts.string.type.INTEGER,
                'original': consts.string.type.INTEGER,
                'options': [consts.string.inp.like.IMP],
            },
            {
                'number': 1,
                'original': 2,
                'options': [consts.builder.inp.like.IMP],
            },
            {
                'number': consts.ast.type.INTEGER,
                'original': consts.ast.type.INTEGER,
                'options': [consts.ast.inp.like.IMP],
            },
            {'number': consts.string.type.INTEGER, 'original': consts.string.type.INTEGER, 'options': None},
        ]
        EXAMPLES_INVALID = [
            {'number': None, 'original': consts.string.type.INTEGER, 'options': [consts.string.inp.like.IMP]},
            {
                'number': consts.string.type.INTEGER,
                'original': None,
                'options': [consts.string.inp.like.IMP],
            },
        ]
