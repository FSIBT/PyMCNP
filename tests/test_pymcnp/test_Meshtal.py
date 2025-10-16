import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Meshtal:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Meshtal
        EXAMPLES_VALID = [
            {
                'header': consts.string.meshtal.HEADER,
                'tallies': [consts.string.meshtal.TALLY],
            },
        ]
        EXAMPLES_INVALID = [
            {
                'header': None,
                'tallies': [consts.string.meshtal.TALLY],
            },
            {
                'header': consts.string.meshtal.HEADER,
                'tallies': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.Meshtal
        EXAMPLES_VALID = [consts.string.MESHTAL]
        EXAMPLES_INVALID = ['hello']

    class Test_File(classes.Test_File):
        element = pymcnp.Meshtal
        EXAMPLES_VALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'meshtal').glob('valid*.meshtal'),
        ]
        EXAMPLES_INVALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'meshtal').glob('invalid*.meshtal'),
        ]
