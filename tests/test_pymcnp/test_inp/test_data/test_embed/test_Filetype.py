import pymcnp
from ..... import consts
from ..... import classes


class Test_Filetype:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.data.embed.Filetype
        EXAMPLES_VALID = [{'kind': pymcnp.types.String('ascii')}]
        EXAMPLES_INVALID = [{'kind': None}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.data.embed.Filetype
        EXAMPLES_VALID = [consts.string.inp.data.embed.FILETYPE]
        EXAMPLES_INVALID = ['hello']


class Test_FiletypeBuilder:
    class TestBuild(classes.Test_Build):
        element = pymcnp.inp.data.embed.FiletypeBuilder
        EXAMPLES_VALID = [{'kind': 'ascii'}, {'kind': pymcnp.types.String('ascii')}]
        EXAMPLES_INVALID = [{'kind': None}, {'kind': 'hello'}]
