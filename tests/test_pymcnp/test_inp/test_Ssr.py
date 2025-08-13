import pymcnp
from ... import consts
from ... import classes


class Test_Ssr:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.Ssr
        EXAMPLES_VALID = [{'options': [consts.string.inp.ssr.AXS]}, {'options': [consts.ast.inp.ssr.AXS]}, {'options': [consts.ast.inp.ssr.AXS]}, {'options': None}]
        EXAMPLES_INVALID = []

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.Ssr
        EXAMPLES_VALID = [consts.string.inp.SSR]
        EXAMPLES_INVALID = ['hello']
