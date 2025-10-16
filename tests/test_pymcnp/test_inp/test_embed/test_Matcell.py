import pymcnp
from .... import consts
from .... import classes


class Test_Matcell:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embed.Matcell
        EXAMPLES_VALID = [{'pairs': [consts.string.inp.embed.matcell.ENTRY]}, {'pairs': [consts.ast.inp.embed.matcell.ENTRY]}]
        EXAMPLES_INVALID = [{'pairs': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embed.Matcell
        EXAMPLES_VALID = [consts.string.inp.embed.MATCELL]
        EXAMPLES_INVALID = ['hello']
