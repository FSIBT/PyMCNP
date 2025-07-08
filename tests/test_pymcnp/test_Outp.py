import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Outp:
    """
    Tests ``Outp``.
    """

    class Test_Init(classes.Test_Init):
        element = pymcnp.Outp
        EXAMPLES_VALID = [
            {
                'header': consts.string.type.STRING,
                'blocks': [consts.string.type.STRING],
            },
        ]
        EXAMPLES_INVALID = [
            {
                'header': None,
                'blocks': [consts.string.type.STRING],
            },
            {
                'header': consts.string.type.STRING,
                'blocks': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.Outp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = ['hello']

    class Test_File(classes.Test_File):
        element = pymcnp.Outp
        EXAMPLES_VALID = [
            *(pathlib.Path(__file__).parent.parent / 'files' / 'outp').glob('valid*.o'),
        ]
        EXAMPLES_INVALID = [
            *(pathlib.Path(__file__).parent.parent / 'files' / 'outp').glob('invalid*.o'),
        ]

    class Test_Dataframe(classes.Test_Dataframe):
        element = pymcnp.Outp
        EXAMPLES = [path.read_text() for path in (pathlib.Path(__file__).parent.parent / 'files' / 'outp').glob('valid*.o')]
