import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Ptrac:
    """
    Tests ``Ptrac``.
    """

    class Test_Init(classes.Test_Init):
        element = pymcnp.Ptrac
        EXAMPLES_VALID = [
            {
                'header': consts.string.type.STRING,
                'histories': [consts.string.type.STRING],
            },
        ]
        EXAMPLES_INVALID = [
            {
                'header': None,
                'histories': [consts.string.type.STRING],
            },
            {
                'header': consts.string.type.STRING,
                'histories': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.Ptrac
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = ['hello']

    class Test_File(classes.Test_File):
        element = pymcnp.Ptrac
        EXAMPLES_VALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac').glob('valid*.ptrac'),
        ]
        EXAMPLES_INVALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac').glob('invalid*.ptrac'),
        ]
