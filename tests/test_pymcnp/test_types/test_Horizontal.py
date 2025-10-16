import pymcnp
from ... import consts
from ... import classes


class Test_Repeat:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Repeat
        EXAMPLES_VALID = [
            {'n': 1},
            {'n': None},
        ]
        EXAMPLES_INVALID = [
            {'n': -1},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Repeat
        EXAMPLES_VALID = [
            consts.string.types.REPEAT,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]


class Test_Insert:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Insert
        EXAMPLES_VALID = [
            {'n': 1},
            {'n': None},
        ]
        EXAMPLES_INVALID = [
            {'n': -1},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Insert
        EXAMPLES_VALID = [
            consts.string.types.INSERT,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]


class Test_Jump:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Jump
        EXAMPLES_VALID = [
            {'n': 1},
            {'n': None},
        ]
        EXAMPLES_INVALID = [
            {'n': -1},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Jump
        EXAMPLES_VALID = [
            consts.string.types.JUMP,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]


class Test_Multiply:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Multiply
        EXAMPLES_VALID = [
            {'x': 1},
            {'x': None},
        ]
        EXAMPLES_INVALID = [
            {'x': 0},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Multiply
        EXAMPLES_VALID = [
            consts.string.types.MULTIPLY,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]


class Test_Log:
    class Test_Init(classes.Test_Init):
        element = pymcnp.types.Log
        EXAMPLES_VALID = [
            {'n': 1},
            {'n': None},
        ]
        EXAMPLES_INVALID = [
            {'n': -1},
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.types.Log
        EXAMPLES_VALID = [
            consts.string.types.LOG,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]
