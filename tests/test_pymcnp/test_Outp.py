import pathlib

import pymcnp
from .. import consts
from .. import classes


class Test_Outp:
    class Test_Init(classes.Test_Init):
        element = pymcnp.Outp
        EXAMPLES_VALID = [
            {
                'header': consts.string.types.STRING,
                'blocks': [consts.string.types.STRING],
            },
        ]
        EXAMPLES_INVALID = [
            {
                'header': None,
                'blocks': [consts.string.types.STRING],
            },
            {
                'header': consts.string.types.STRING,
                'blocks': None,
            },
        ]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.Outp
        EXAMPLES_VALID = [consts.string.OUTP]
        EXAMPLES_INVALID = ['hello']

    class Test_File(classes.Test_File):
        element = pymcnp.Outp
        EXAMPLES_VALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp').glob('valid*.outp'),
        ]
        EXAMPLES_INVALID = [
            *(pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp').glob('invalid*.outp'),
        ]

    class Test_Dataframe(classes.Test_Dataframe):
        element = pymcnp.Outp
        EXAMPLES = [path.read_text() for path in (pathlib.Path(__file__).parent.parent.parent / 'files' / 'outp').glob('valid*.outp')]
