import pymcnp
from .... import consts
from .... import classes


class Test_Ssw:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ssw
        EXAMPLES_VALID = [
            {'surfaces': [consts.string.types.INTEGER], 'cells': [consts.string.types.INTEGER], 'options': [consts.string.inp.data.ssw.CEL]},
            {'surfaces': [1], 'cells': [1], 'options': [consts.ast.inp.data.ssw.CEL]},
            {'surfaces': [consts.ast.types.INTEGER], 'cells': [consts.ast.types.INTEGER], 'options': [consts.ast.inp.data.ssw.CEL]},
            {'surfaces': [consts.string.types.INTEGER], 'cells': None, 'options': [consts.string.inp.data.ssw.CEL]},
            {'surfaces': [consts.string.types.INTEGER], 'cells': [consts.string.types.INTEGER], 'options': None},
        ]
        EXAMPLES_INVALID = [{'surfaces': None, 'cells': [consts.string.types.INTEGER], 'options': [consts.string.inp.data.ssw.CEL]}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ssw
        EXAMPLES_VALID = [consts.string.inp.data.SSW]
        EXAMPLES_INVALID = ['hello']
