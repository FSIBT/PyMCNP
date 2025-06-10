import pymcnp
from .... import _utils


class Test_Meshgeo:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Meshgeo
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.MeshgeoBuilder
        EXAMPLES_VALID = [{'form': 'lnk3dnt'}, {'form': pymcnp.utils.types.String('lnk3dnt')}]
        EXAMPLES_INVALID = [{'form': None}, {'form': 'hello'}]
