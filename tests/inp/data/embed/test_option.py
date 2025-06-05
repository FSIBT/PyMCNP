import pymcnp
from .... import _utils


class Test_Background:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Background
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.BackgroundBuilder
        EXAMPLES_VALID = [{'number': '1'}, {'number': 1}, {'number': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'number': None}]


class Test_Meshgeo:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Meshgeo
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.MeshgeoBuilder
        EXAMPLES_VALID = [{'form': 'abaqus'}, {'form': pymcnp.utils.types.String('abaqus')}]
        EXAMPLES_INVALID = [{'form': None}]


class Test_Mgeoin:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Mgeoin
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.MgeoinBuilder
        EXAMPLES_VALID = [
            {'filename': 'a'},
            {'filename': 'a'},
            {'filename': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = [{'filename': None}]


class Test_Meeout:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Meeout
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.MeeoutBuilder
        EXAMPLES_VALID = [
            {'filename': 'a'},
            {'filename': 'a'},
            {'filename': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = [{'filename': None}]


class Test_Meein:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Meein
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.MeeinBuilder
        EXAMPLES_VALID = [
            {'filename': 'a'},
            {'filename': 'a'},
            {'filename': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = [{'filename': None}]


class Test_Calcvols:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Calcvols
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.CalcvolsBuilder
        EXAMPLES_VALID = [{'setting': 'yes'}, {'setting': pymcnp.utils.types.String('yes')}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Debug:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Debug
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.DebugBuilder
        EXAMPLES_VALID = [
            {'parameter': 'echomesh'},
            {'parameter': pymcnp.utils.types.String('echomesh')},
        ]
        EXAMPLES_INVALID = [{'parameter': None}]


class Test_Filetype:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Filetype
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.FiletypeBuilder
        EXAMPLES_VALID = [{'kind': 'ascii'}, {'kind': pymcnp.utils.types.String('ascii')}]
        EXAMPLES_INVALID = [{'kind': None}]


class Test_Gmvfile:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Gmvfile
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.GmvfileBuilder
        EXAMPLES_VALID = [{'filename': 'a'}, {'filename': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'filename': None}]


class Test_Length:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Length
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.LengthBuilder
        EXAMPLES_VALID = [{'factor': '1.0'}, {'factor': 1.0}, {'factor': _utils.REAL}]
        EXAMPLES_INVALID = [{'factor': None}]


class Test_Mcnpumfile:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.embed.Mcnpumfile
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.embed.McnpumfileBuilder
        EXAMPLES_VALID = [
            {'filename': 'a'},
            {'filename': 'a'},
            {'filename': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = [{'filename': None}]
