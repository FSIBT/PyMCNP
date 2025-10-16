import pymcnp
from .... import consts
from .... import classes


class Test_Meshgeo:
    class Test_Init(classes.Test_Init):
        element = pymcnp.inp.embed.Meshgeo
        EXAMPLES_VALID = [{'form': 'lnk3dnt'}, {'form': pymcnp.types.String('lnk3dnt')}]
        EXAMPLES_INVALID = [{'form': None}, {'form': 'hello'}]

    class Test_Mcnp(classes.Test_Mcnp):
        element = pymcnp.inp.embed.Meshgeo
        EXAMPLES_VALID = [consts.string.inp.embed.MESHGEO]
        EXAMPLES_INVALID = ['hello']
