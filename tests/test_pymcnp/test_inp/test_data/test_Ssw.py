import pymcnp
from .... import consts
from .... import classes


class Test_Ssw:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.Ssw
        EXAMPLES_VALID = [
            {'surfaces': [consts.ast.type.INTEGER], 'cells': [consts.ast.type.INTEGER], 'options': [consts.ast.inp.data.ssw.CEL]},
            {'surfaces': [consts.ast.type.INTEGER], 'cells': None, 'options': [consts.ast.inp.data.ssw.CEL]},
            {'surfaces': [consts.ast.type.INTEGER], 'cells': [consts.ast.type.INTEGER], 'options': None},
        ]
        EXAMPLES_INVALID = [{'surfaces': None, 'cells': [consts.ast.type.INTEGER], 'options': [consts.ast.inp.data.ssw.CEL]}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.Ssw
        EXAMPLES_VALID = [consts.string.inp.data.SSW]
        EXAMPLES_INVALID = ['hello']


class Test_SswBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.SswBuilder
        EXAMPLES_VALID = [
            {'surfaces': [consts.string.type.INTEGER], 'cells': [consts.string.type.INTEGER], 'options': [consts.string.inp.data.ssw.CEL]},
            {'surfaces': [1], 'cells': [1], 'options': [consts.builder.inp.data.ssw.CEL]},
            {'surfaces': [consts.ast.type.INTEGER], 'cells': [consts.ast.type.INTEGER], 'options': [consts.ast.inp.data.ssw.CEL]},
            {'surfaces': [consts.string.type.INTEGER], 'cells': None, 'options': [consts.string.inp.data.ssw.CEL]},
            {'surfaces': [consts.string.type.INTEGER], 'cells': [consts.string.type.INTEGER], 'options': None},
        ]
        EXAMPLES_INVALID = [{'surfaces': None, 'cells': [consts.string.type.INTEGER], 'options': [consts.string.inp.data.ssw.CEL]}]
