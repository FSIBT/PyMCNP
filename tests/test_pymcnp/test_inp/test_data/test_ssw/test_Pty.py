import pymcnp
from ..... import consts
from ..... import classes


class Test_Pty:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssw.Pty
        EXAMPLES_VALID = [{'tracks': [consts.ast.type.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'tracks': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssw.Pty
        EXAMPLES_VALID = [consts.string.inp.data.ssw.PTY]
        EXAMPLES_INVALID = ['hello']


class Test_PtyBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ssw.PtyBuilder
        EXAMPLES_VALID = [{'tracks': [consts.string.type.DESIGNATOR]}, {'tracks': [consts.ast.type.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'tracks': None}]
