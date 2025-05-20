import pymcnp
from .... import _utils


class Test_Blocksize:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Blocksize
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.BlocksizeBuilder
        EXAMPLES_VALID = [{'ncy': '3'}, {'ncy': 3}, {'ncy': pymcnp.utils.types.Integer(3)}]
        EXAMPLES_INVALID = [{'ncy': None}]


class Test_Kinetics:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Kinetics
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.KineticsBuilder
        EXAMPLES_VALID = [
            {'setting': 'no'},
            {'setting': pymcnp.utils.types.String('no')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Precursor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Precursor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.PrecursorBuilder
        EXAMPLES_VALID = [
            {'setting': 'no'},
            {'setting': pymcnp.utils.types.String('no')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ksental:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Ksental
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.KsentalBuilder
        EXAMPLES_VALID = [
            {'fileopt': 'mctal'},
            {'fileopt': 'mctal'},
            {'fileopt': pymcnp.utils.types.String('mctal')},
        ]
        EXAMPLES_INVALID = [{'fileopt': None}]


class Test_Fmat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmat
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatBuilder
        EXAMPLES_VALID = [
            {'setting': 'no'},
            {'setting': pymcnp.utils.types.String('no')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Fmatskpt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatskpt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatskptBuilder
        EXAMPLES_VALID = [{'fmat_skip': '1.0'}, {'fmat_skip': 1.0}, {'fmat_skip': _utils.REAL}]
        EXAMPLES_INVALID = [{'fmat_skip': None}]


class Test_Fmatncyc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatncyc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatncycBuilder
        EXAMPLES_VALID = [{'fmat_ncyc': '1.0'}, {'fmat_ncyc': 1.0}, {'fmat_ncyc': _utils.REAL}]
        EXAMPLES_INVALID = [{'fmat_ncyc': None}]


class Test_Fmatspace:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatspace
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatspaceBuilder
        EXAMPLES_VALID = [{'fmat_space': '1.0'}, {'fmat_space': 1.0}, {'fmat_space': _utils.REAL}]
        EXAMPLES_INVALID = [{'fmat_space': None}]


class Test_Fmataccel:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmataccel
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmataccelBuilder
        EXAMPLES_VALID = [
            {'setting': 'no'},
            {'setting': pymcnp.utils.types.String('no')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Fmatreduce:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatreduce
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatreduceBuilder
        EXAMPLES_VALID = [
            {'setting': 'no'},
            {'setting': pymcnp.utils.types.String('no')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Fmatnx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatnx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatnxBuilder
        EXAMPLES_VALID = [{'fmat_nx': '1.0'}, {'fmat_nx': 1.0}, {'fmat_nx': _utils.REAL}]
        EXAMPLES_INVALID = [{'fmat_nx': None}]


class Test_Fmatny:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatny
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatnyBuilder
        EXAMPLES_VALID = [{'fmat_ny': '1.0'}, {'fmat_ny': 1.0}, {'fmat_ny': _utils.REAL}]
        EXAMPLES_INVALID = [{'fmat_ny': None}]


class Test_Fmatnz:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.kopts.Fmatnz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.kopts.FmatnzBuilder
        EXAMPLES_VALID = [{'fmat_nz': '1.0'}, {'fmat_nz': 1.0}, {'fmat_nz': _utils.REAL}]
        EXAMPLES_INVALID = [{'fmat_nz': None}]
