import pymcnp
from ..... import consts
from ..... import classes


class Test_Dn:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Dn
        EXAMPLES_VALID = [{'source': pymcnp.types.String('model')}]
        EXAMPLES_INVALID = [{'source': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Dn
        EXAMPLES_VALID = [consts.string.inp.data.act.DN]
        EXAMPLES_INVALID = ['hello']


class Test_DnBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.act.DnBuilder
        EXAMPLES_VALID = [{'source': 'model'}, {'source': pymcnp.types.String('model')}]
        EXAMPLES_INVALID = [{'source': None}, {'source': 'hello'}]
