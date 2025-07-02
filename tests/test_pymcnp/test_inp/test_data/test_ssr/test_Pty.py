import pymcnp
from ..... import consts
from ..... import classes


class Test_Pty:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ssr.Pty
        EXAMPLES_VALID = [{'particles': [consts.ast.type.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'particles': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ssr.Pty
        EXAMPLES_VALID = [consts.string.inp.data.ssr.PTY]
        EXAMPLES_INVALID = ['hello']


class Test_PtyBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ssr.PtyBuilder
        EXAMPLES_VALID = [{'particles': [consts.string.type.DESIGNATOR]}, {'particles': [consts.ast.type.DESIGNATOR]}]
        EXAMPLES_INVALID = [{'particles': None}]
