import pymcnp
from ..... import consts
from ..... import classes


class Test_Event:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.ptrac.Event
        EXAMPLES_VALID = [{'settings': [consts.ast.type.STRING]}]
        EXAMPLES_INVALID = [{'settings': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.ptrac.Event
        EXAMPLES_VALID = [consts.string.inp.data.ptrac.EVENT]
        EXAMPLES_INVALID = ['hello']


class Test_EventBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.ptrac.EventBuilder
        EXAMPLES_VALID = [{'settings': [consts.string.type.STRING]}, {'settings': [consts.ast.type.STRING]}]
        EXAMPLES_INVALID = [{'settings': None}]
