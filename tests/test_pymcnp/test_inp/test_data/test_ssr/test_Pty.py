import pymcnp
from ..... import consts
from ..... import classes


class Test_Pty:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Pty
        EXAMPLES_VALID = [{'particles': [consts.string.types.DESIGNATOR]}, {'particles': [consts.ast.types.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'particles': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Pty
        EXAMPLES_VALID = [consts.string.inp.data.ssr.PTY]
        EXAMPLES_INVALID = ['hello']
