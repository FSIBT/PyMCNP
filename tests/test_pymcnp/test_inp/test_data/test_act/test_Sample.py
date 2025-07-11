import pymcnp
from ..... import consts
from ..... import classes


class Test_Sample:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.act.Sample
        EXAMPLES_VALID = [{'setting': 'correlate'}, {'setting': pymcnp.types.String('correlate')}]
        EXAMPLES_INVALID = [{'setting': None}, {'setting': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.act.Sample
        EXAMPLES_VALID = [consts.string.inp.data.act.SAMPLE]
        EXAMPLES_INVALID = ['hello']
