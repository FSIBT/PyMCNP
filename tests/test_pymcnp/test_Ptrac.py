import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Ptrac:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Ptrac
        EXAMPLES_VALID = [
            {
                'header': consts.string.ptrac.HEADER,
                'histories': [consts.string.ptrac.HISTORY],
            },
        ]
        EXAMPLES_INVALID = [
            {
                'header': None,
                'histories': [consts.string.ptrac.HISTORY],
            },
            {
                'header': consts.string.ptrac.HEADER,
                'histories': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.Ptrac
        EXAMPLES_VALID = [consts.string.PTRAC]
        EXAMPLES_INVALID = ['hello']

    class Test_File(classes.Test_File):
        element = pymcnp.Ptrac
        EXAMPLES_VALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac').glob('valid*.ptrac'),
        ]
        EXAMPLES_INVALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'ptrac').glob('invalid*.ptrac'),
        ]
