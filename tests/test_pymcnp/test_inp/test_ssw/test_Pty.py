import pymcnp
from .... import consts
from .... import classes


class Test_Pty:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.ssw.Pty
        EXAMPLES_VALID = [{'tracks': [consts.string.types.DESIGNATOR]}, {'tracks': [consts.ast.types.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'tracks': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.ssw.Pty
        EXAMPLES_VALID = [consts.string.inp.ssw.PTY]
        EXAMPLES_INVALID = ['hello']
