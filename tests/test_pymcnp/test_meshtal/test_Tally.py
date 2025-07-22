import pymcnp
from ... import consts
from ... import classes


class Test_Tally:
    class Test_Init(classes.Test_Init):
        element = pymcnp.meshtal.Tally
        EXAMPLES_VALID = [
            {
                'result': consts.ast.types.STRING,
                'error': consts.ast.types.STRING,
                'x': consts.ast.types.STRING,
                'y': consts.ast.types.STRING,
                'z': consts.ast.types.STRING,
                'energy': consts.ast.types.STRING,
                'time': consts.ast.types.STRING,
            },
            {
                'result': consts.ast.types.STRING,
                'error': consts.ast.types.STRING,
                'x': None,
                'y': consts.ast.types.STRING,
                'z': consts.ast.types.STRING,
                'energy': consts.ast.types.STRING,
                'time': consts.ast.types.STRING,
            },
            {
                'result': consts.ast.types.STRING,
                'error': consts.ast.types.STRING,
                'x': consts.ast.types.STRING,
                'y': None,
                'z': consts.ast.types.STRING,
                'energy': consts.ast.types.STRING,
                'time': consts.ast.types.STRING,
            },
            {
                'result': consts.ast.types.STRING,
                'error': consts.ast.types.STRING,
                'x': consts.ast.types.STRING,
                'y': consts.ast.types.STRING,
                'z': None,
                'energy': consts.ast.types.STRING,
                'time': consts.ast.types.STRING,
            },
            {
                'result': consts.ast.types.STRING,
                'error': consts.ast.types.STRING,
                'x': consts.ast.types.STRING,
                'y': consts.ast.types.STRING,
                'z': consts.ast.types.STRING,
                'energy': None,
                'time': consts.ast.types.STRING,
            },
            {
                'result': consts.ast.types.STRING,
                'error': consts.ast.types.STRING,
                'x': consts.ast.types.STRING,
                'y': consts.ast.types.STRING,
                'z': consts.ast.types.STRING,
                'energy': consts.ast.types.STRING,
                'time': None,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'result': None,
                'error': consts.ast.types.STRING,
                'x': consts.ast.types.STRING,
                'y': consts.ast.types.STRING,
                'z': consts.ast.types.STRING,
                'energy': consts.ast.types.STRING,
                'time': consts.ast.types.STRING,
            },
            {
                'result': consts.ast.types.STRING,
                'error': None,
                'x': consts.ast.types.STRING,
                'y': consts.ast.types.STRING,
                'z': consts.ast.types.STRING,
                'energy': consts.ast.types.STRING,
                'time': consts.ast.types.STRING,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.meshtal.Tally
        EXAMPLES_VALID = [
            consts.string.meshtal.TALLY,
        ]
        EXAMPLES_INVALID = [
            'hello',
        ]
