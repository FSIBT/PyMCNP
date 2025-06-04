import pymcnp
from ... import _utils


class Test_P_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.P_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.P_0
        EXAMPLES = [
            'p 0 0 0 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.PBuilder_0
        EXAMPLES_VALID = [
            {'a': '0.1', 'b': '0.1', 'c': '0.1', 'd': '0.1'},
            {'a': 0.1, 'b': 0.1, 'c': 0.1, 'd': 0.1},
            {'a': _utils.REAL, 'b': _utils.REAL, 'c': _utils.REAL, 'd': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'a': None, 'b': '0.1', 'c': '0.1', 'd': '0.1'},
            {'a': '0.1', 'b': None, 'c': '0.1', 'd': '0.1'},
            {'a': '0.1', 'b': '0.1', 'c': None, 'd': '0.1'},
            {'a': '0.1', 'b': '0.1', 'c': '0.1', 'd': None},
        ]


class Test_P_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.P_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.P_1
        EXAMPLES = [
            'p 1 0 0 2 0 0 3 0 0',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.PBuilder_1
        EXAMPLES_VALID = [
            {
                'x1': '0.1',
                'y1': '0.1',
                'z1': '0.1',
                'x2': '0.1',
                'y2': '0.1',
                'z2': '0.1',
                'x3': '0.1',
                'y3': '0.1',
                'z3': '0.1',
            },
            {
                'x1': 0.1,
                'y1': 0.1,
                'z1': 0.1,
                'x2': 0.1,
                'y2': 0.1,
                'z2': 0.1,
                'x3': 0.1,
                'y3': 0.1,
                'z3': 0.1,
            },
            {
                'x1': _utils.REAL,
                'y1': _utils.REAL,
                'z1': _utils.REAL,
                'x2': _utils.REAL,
                'y2': _utils.REAL,
                'z2': _utils.REAL,
                'x3': _utils.REAL,
                'y3': _utils.REAL,
                'z3': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'x1': None,
                'y1': '0.1',
                'z1': '0.1',
                'x2': '0.1',
                'y2': '0.1',
                'z2': '0.1',
                'x3': '0.1',
                'y3': '0.1',
                'z3': '0.1',
            },
            {
                'x1': '0.1',
                'y1': None,
                'z1': '0.1',
                'x2': '0.1',
                'y2': '0.1',
                'z2': '0.1',
                'x3': '0.1',
                'y3': '0.1',
                'z3': '0.1',
            },
            {
                'x1': '0.1',
                'y1': '0.1',
                'z1': None,
                'x2': '0.1',
                'y2': '0.1',
                'z2': '0.1',
                'x3': '0.1',
                'y3': '0.1',
                'z3': '0.1',
            },
            {
                'x1': '0.1',
                'y1': '0.1',
                'z1': '0.1',
                'x2': None,
                'y2': '0.1',
                'z2': '0.1',
                'x3': '0.1',
                'y3': '0.1',
                'z3': '0.1',
            },
            {
                'x1': '0.1',
                'y1': '0.1',
                'z1': '0.1',
                'x2': '0.1',
                'y2': None,
                'z2': '0.1',
                'x3': '0.1',
                'y3': '0.1',
                'z3': '0.1',
            },
            {
                'x1': '0.1',
                'y1': '0.1',
                'z1': '0.1',
                'x2': '0.1',
                'y2': '0.1',
                'z2': None,
                'x3': '0.1',
                'y3': '0.1',
                'z3': '0.1',
            },
            {
                'x1': '0.1',
                'y1': '0.1',
                'z1': '0.1',
                'x2': '0.1',
                'y2': '0.1',
                'z2': '0.1',
                'x3': None,
                'y3': '0.1',
                'z3': '0.1',
            },
            {
                'x1': '0.1',
                'y1': '0.1',
                'z1': '0.1',
                'x2': '0.1',
                'y2': '0.1',
                'z2': '0.1',
                'x3': '0.1',
                'y3': None,
                'z3': '0.1',
            },
            {
                'x1': '0.1',
                'y1': '0.1',
                'z1': '0.1',
                'x2': '0.1',
                'y2': '0.1',
                'z2': '0.1',
                'x3': '0.1',
                'y3': '0.1',
                'z3': None,
            },
        ]


class Test_Px:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Px
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Px
        EXAMPLES = [
            'px 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.PxBuilder
        EXAMPLES_VALID = [
            {'d': '0.1'},
            {'d': 0.1},
            {'d': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'d': None},
        ]


class Test_Py:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Py
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Py
        EXAMPLES = [
            'py 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.PyBuilder
        EXAMPLES_VALID = [
            {'d': '0.1'},
            {'d': 0.1},
            {'d': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'d': None},
        ]


class Test_Pz:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Pz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Pz
        EXAMPLES = [
            'pz 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.PzBuilder
        EXAMPLES_VALID = [
            {'d': '0.1'},
            {'d': 0.1},
            {'d': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'d': None},
        ]


class Test_So:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.So
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.So
        EXAMPLES = [
            'so 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SoBuilder
        EXAMPLES_VALID = [
            {'r': '0.1'},
            {'r': 0.1},
            {'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'r': None},
        ]


class Test_S:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.S
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.S
        EXAMPLES = [
            's 0 0 0 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'r': '0.1'},
            {'x': 0.1, 'y': 0.1, 'z': 0.1, 'r': 0.1},
            {'x': _utils.REAL, 'y': _utils.REAL, 'z': _utils.REAL, 'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '0.1', 'z': '0.1', 'r': '0.1'},
            {'x': '0.1', 'y': None, 'z': '0.1', 'r': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': None, 'r': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'r': None},
        ]


class Test_Sx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Sx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Sx
        EXAMPLES = [
            'sx 3 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SxBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 'r': '0.1'},
            {'x': 0.1, 'r': 0.1},
            {'x': _utils.REAL, 'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'r': '0.1'},
            {'x': '0.1', 'r': None},
        ]


class Test_Sy:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Sy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Sy
        EXAMPLES = [
            'sy 3 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SyBuilder
        EXAMPLES_VALID = [
            {'y': '0.1', 'r': '0.1'},
            {'y': 0.1, 'r': 0.1},
            {'y': _utils.REAL, 'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'y': None, 'r': '0.1'},
            {'y': '0.1', 'r': None},
        ]


class Test_Sz:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Sz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Sz
        EXAMPLES = [
            'sz 3 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SzBuilder
        EXAMPLES_VALID = [
            {'z': '0.1', 'r': '0.1'},
            {'z': 0.1, 'r': 0.1},
            {'z': _utils.REAL, 'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'z': None, 'r': '0.1'},
            {'z': '0.1', 'r': None},
        ]


class Test_C_x:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.C_x
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.C_x
        EXAMPLES = [
            'c/x 1 4 3',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.C_xBuilder
        EXAMPLES_VALID = [
            {'y': '0.1', 'z': '0.1', 'r': '0.1'},
            {'y': 0.1, 'z': 0.1, 'r': 0.1},
            {'y': _utils.REAL, 'z': _utils.REAL, 'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'y': None, 'z': '0.1', 'r': '0.1'},
            {'y': '0.1', 'z': None, 'r': '0.1'},
            {'y': '0.1', 'z': '0.1', 'r': None},
        ]


class Test_C_y:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.C_y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.C_y
        EXAMPLES = [
            'c/y 1 4 3',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.C_yBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 'z': '0.1', 'r': '0.1'},
            {'x': 0.1, 'z': 0.1, 'r': 0.1},
            {'x': _utils.REAL, 'z': _utils.REAL, 'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'z': '0.1', 'r': '0.1'},
            {'x': '0.1', 'z': None, 'r': '0.1'},
            {'x': '0.1', 'z': '0.1', 'r': None},
        ]


class Test_C_z:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.C_z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.C_z
        EXAMPLES = [
            'c/z 1 4 3',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.C_zBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 'y': '0.1', 'r': '0.1'},
            {'x': 0.1, 'y': 0.1, 'r': 0.1},
            {'x': _utils.REAL, 'y': _utils.REAL, 'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '0.1', 'r': '0.1'},
            {'x': '0.1', 'y': None, 'r': '0.1'},
            {'x': '0.1', 'y': '0.1', 'r': None},
        ]


class Test_Cx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Cx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Cx
        EXAMPLES = [
            'cx 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.CxBuilder
        EXAMPLES_VALID = [
            {'r': '0.1'},
            {'r': 0.1},
            {'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'r': None},
        ]


class Test_Cy:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Cy
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Cy
        EXAMPLES = [
            'cy 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.CyBuilder
        EXAMPLES_VALID = [
            {'r': '0.1'},
            {'r': 0.1},
            {'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'r': None},
        ]


class Test_Cz:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Cz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Cz
        EXAMPLES = [
            'cz 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.CzBuilder
        EXAMPLES_VALID = [
            {'r': '0.1'},
            {'r': 0.1},
            {'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'r': None},
        ]


class Test_K_x:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.K_x
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.K_x
        EXAMPLES = ['k/x 1 2 3 4 5']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.K_xBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': 0.1, 'y': 0.1, 'z': 0.1, 't_squared': 0.1, 'plusminus_1': 0.1},
            {
                'x': _utils.REAL,
                'y': _utils.REAL,
                'z': _utils.REAL,
                't_squared': _utils.REAL,
                'plusminus_1': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '0.1', 'z': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': None, 'z': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': None, 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 't_squared': None, 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 't_squared': '0.1', 'plusminus_1': None},
        ]


class Test_K_y:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.K_y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.K_y
        EXAMPLES = ['k/y 1 2 3 4 5']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.K_yBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': 0.1, 'y': 0.1, 'z': 0.1, 't_squared': 0.1, 'plusminus_1': 0.1},
            {
                'x': _utils.REAL,
                'y': _utils.REAL,
                'z': _utils.REAL,
                't_squared': _utils.REAL,
                'plusminus_1': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '0.1', 'z': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': None, 'z': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': None, 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 't_squared': None, 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 't_squared': '0.1', 'plusminus_1': None},
        ]


class Test_K_z:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.K_z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.K_z
        EXAMPLES = ['k/z 1 2 3 4 5']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.K_zBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': 0.1, 'y': 0.1, 'z': 0.1, 't_squared': 0.1, 'plusminus_1': 0.1},
            {
                'x': _utils.REAL,
                'y': _utils.REAL,
                'z': _utils.REAL,
                't_squared': _utils.REAL,
                'plusminus_1': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '0.1', 'z': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': None, 'z': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': None, 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 't_squared': None, 'plusminus_1': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 't_squared': '0.1', 'plusminus_1': None},
        ]


class Test_Kx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Kx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Kx
        EXAMPLES = ['kx 1 2 3']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.KxBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': 0.1, 't_squared': 0.1, 'plusminus_1': 0.1},
            {'x': _utils.REAL, 't_squared': _utils.REAL, 'plusminus_1': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'x': None, 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'x': '0.1', 't_squared': None, 'plusminus_1': '0.1'},
            {'x': '0.1', 't_squared': '0.1', 'plusminus_1': None},
        ]


class Test_Ky:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Ky
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Ky
        EXAMPLES = ['ky 1 2 3']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.KyBuilder
        EXAMPLES_VALID = [
            {'y': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'y': 0.1, 't_squared': 0.1, 'plusminus_1': 0.1},
            {'y': _utils.REAL, 't_squared': _utils.REAL, 'plusminus_1': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'y': None, 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'y': '0.1', 't_squared': None, 'plusminus_1': '0.1'},
            {'y': '0.1', 't_squared': '0.1', 'plusminus_1': None},
        ]


class Test_Kz:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Kz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Kz
        EXAMPLES = ['kz 1 2 3']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.KzBuilder
        EXAMPLES_VALID = [
            {'z': '0.1', 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'z': 0.1, 't_squared': 0.1, 'plusminus_1': 0.1},
            {'z': _utils.REAL, 't_squared': _utils.REAL, 'plusminus_1': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'z': None, 't_squared': '0.1', 'plusminus_1': '0.1'},
            {'z': '0.1', 't_squared': None, 'plusminus_1': '0.1'},
            {'z': '0.1', 't_squared': '0.1', 'plusminus_1': None},
        ]


class Test_Sq:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Sq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SqBuilder
        EXAMPLES_VALID = [
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'x': '0.1',
                'y': '0.1',
                'z': '0.1',
            },
            {
                'a': 0.1,
                'b': 0.1,
                'c': 0.1,
                'd': 0.1,
                'e': 0.1,
                'f': 0.1,
                'g': 0.1,
                'x': 0.1,
                'y': 0.1,
                'z': 0.1,
            },
            {
                'a': _utils.REAL,
                'b': _utils.REAL,
                'c': _utils.REAL,
                'd': _utils.REAL,
                'e': _utils.REAL,
                'f': _utils.REAL,
                'g': _utils.REAL,
                'x': _utils.REAL,
                'y': _utils.REAL,
                'z': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'a': None,
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'x': '0.1',
                'y': '0.1',
                'z': '0.1',
            },
            {
                'a': '0.1',
                'b': None,
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'x': '0.1',
                'y': '0.1',
                'z': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': None,
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'x': '0.1',
                'y': '0.1',
                'z': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': None,
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'x': '0.1',
                'y': '0.1',
                'z': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': None,
                'f': '0.1',
                'g': '0.1',
                'x': '0.1',
                'y': '0.1',
                'z': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': None,
                'g': '0.1',
                'x': '0.1',
                'y': '0.1',
                'z': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': None,
                'x': '0.1',
                'y': '0.1',
                'z': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'x': None,
                'y': '0.1',
                'z': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'x': '0.1',
                'y': None,
                'z': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'x': '0.1',
                'y': '0.1',
                'z': None,
            },
        ]


class Test_Gq:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Gq
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.GqBuilder
        EXAMPLES_VALID = [
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'h': '0.1',
                'j': '0.1',
                'k': '0.1',
            },
            {
                'a': 0.1,
                'b': 0.1,
                'c': 0.1,
                'd': 0.1,
                'e': 0.1,
                'f': 0.1,
                'g': 0.1,
                'h': 0.1,
                'j': 0.1,
                'k': 0.1,
            },
            {
                'a': _utils.REAL,
                'b': _utils.REAL,
                'c': _utils.REAL,
                'd': _utils.REAL,
                'e': _utils.REAL,
                'f': _utils.REAL,
                'g': _utils.REAL,
                'h': _utils.REAL,
                'j': _utils.REAL,
                'k': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'a': None,
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'h': '0.1',
                'j': '0.1',
                'k': '0.1',
            },
            {
                'a': '0.1',
                'b': None,
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'h': '0.1',
                'j': '0.1',
                'k': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': None,
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'h': '0.1',
                'j': '0.1',
                'k': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': None,
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'h': '0.1',
                'j': '0.1',
                'k': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': None,
                'f': '0.1',
                'g': '0.1',
                'h': '0.1',
                'j': '0.1',
                'k': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': None,
                'g': '0.1',
                'h': '0.1',
                'j': '0.1',
                'k': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': None,
                'h': '0.1',
                'j': '0.1',
                'k': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'h': None,
                'j': '0.1',
                'k': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'h': '0.1',
                'j': None,
                'k': '0.1',
            },
            {
                'a': '0.1',
                'b': '0.1',
                'c': '0.1',
                'd': '0.1',
                'e': '0.1',
                'f': '0.1',
                'g': '0.1',
                'h': '0.1',
                'j': '0.1',
                'k': None,
            },
        ]


class Test_Tx:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Tx
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Tx
        EXAMPLES = ['tx 1 2 3 4 5 6']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.TxBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': 0.1, 'y': 0.1, 'z': 0.1, 'a': 0.1, 'b': 0.1, 'c': 0.1},
            {
                'x': _utils.REAL,
                'y': _utils.REAL,
                'z': _utils.REAL,
                'a': _utils.REAL,
                'b': _utils.REAL,
                'c': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': None, 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': None, 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': None, 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': None, 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': None},
        ]


class Test_Ty:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Ty
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Ty
        EXAMPLES = ['ty 1 2 3 4 5 6']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.TyBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': 0.1, 'y': 0.1, 'z': 0.1, 'a': 0.1, 'b': 0.1, 'c': 0.1},
            {
                'x': _utils.REAL,
                'y': _utils.REAL,
                'z': _utils.REAL,
                'a': _utils.REAL,
                'b': _utils.REAL,
                'c': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': None, 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': None, 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': None, 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': None, 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': None},
        ]


class Test_Tz:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Tz
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Tz
        EXAMPLES = ['tz 1 2 3 4 5 6']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.TzBuilder
        EXAMPLES_VALID = [
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': 0.1, 'y': 0.1, 'z': 0.1, 'a': 0.1, 'b': 0.1, 'c': 0.1},
            {
                'x': _utils.REAL,
                'y': _utils.REAL,
                'z': _utils.REAL,
                'a': _utils.REAL,
                'b': _utils.REAL,
                'c': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {'x': None, 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': None, 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': None, 'a': '0.1', 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': None, 'b': '0.1', 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': None, 'c': '0.1'},
            {'x': '0.1', 'y': '0.1', 'z': '0.1', 'a': '0.1', 'b': '0.1', 'c': None},
        ]


class Test_X:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.X
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.XBuilder
        EXAMPLES_VALID = [
            {'x1': '0.1', 'r1': '0.1', 'x2': '0.1', 'r2': '0.1', 'x3': '0.1', 'r3': '0.1'},
            {'x1': '0.1', 'r1': '0.1', 'x2': None, 'r2': '0.1', 'x3': '0.1', 'r3': '0.1'},
            {'x1': '0.1', 'r1': '0.1', 'x2': '0.1', 'r2': None, 'x3': '0.1', 'r3': '0.1'},
            {'x1': '0.1', 'r1': '0.1', 'x2': '0.1', 'r2': '0.1', 'x3': None, 'r3': '0.1'},
            {'x1': '0.1', 'r1': '0.1', 'x2': '0.1', 'r2': '0.1', 'x3': '0.1', 'r3': None},
            {'x1': 0.1, 'r1': 0.1, 'x2': 0.1, 'r2': 0.1, 'x3': 0.1, 'r3': 0.1},
            {
                'x1': _utils.REAL,
                'r1': _utils.REAL,
                'x2': _utils.REAL,
                'r2': _utils.REAL,
                'x3': _utils.REAL,
                'r3': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {'x1': None, 'r1': '0.1', 'x2': '0.1', 'r2': '0.1', 'x3': '0.1', 'r3': '0.1'},
            {'x1': '0.1', 'r1': None, 'x2': '0.1', 'r2': '0.1', 'x3': '0.1', 'r3': '0.1'},
        ]


class Test_Y:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Y
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.YBuilder
        EXAMPLES_VALID = [
            {'y1': '0.1', 'r1': '0.1', 'y2': '0.1', 'r2': '0.1', 'y3': '0.1', 'r3': '0.1'},
            {'y1': '0.1', 'r1': '0.1', 'y2': None, 'r2': '0.1', 'y3': '0.1', 'r3': '0.1'},
            {'y1': '0.1', 'r1': '0.1', 'y2': '0.1', 'r2': None, 'y3': '0.1', 'r3': '0.1'},
            {'y1': '0.1', 'r1': '0.1', 'y2': '0.1', 'r2': '0.1', 'y3': None, 'r3': '0.1'},
            {'y1': '0.1', 'r1': '0.1', 'y2': '0.1', 'r2': '0.1', 'y3': '0.1', 'r3': None},
            {'y1': 0.1, 'r1': 0.1, 'y2': 0.1, 'r2': 0.1, 'y3': 0.1, 'r3': 0.1},
            {
                'y1': _utils.REAL,
                'r1': _utils.REAL,
                'y2': _utils.REAL,
                'r2': _utils.REAL,
                'y3': _utils.REAL,
                'r3': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {'y1': None, 'r1': '0.1', 'y2': '0.1', 'r2': '0.1', 'y3': '0.1', 'r3': '0.1'},
            {'y1': '0.1', 'r1': None, 'y2': '0.1', 'r2': '0.1', 'y3': '0.1', 'r3': '0.1'},
        ]


class Test_Z:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Z
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.ZBuilder
        EXAMPLES_VALID = [
            {'z1': '0.1', 'r1': '0.1', 'z2': '0.1', 'r2': '0.1', 'z3': '0.1', 'r3': '0.1'},
            {'z1': '0.1', 'r1': '0.1', 'z2': None, 'r2': '0.1', 'z3': '0.1', 'r3': '0.1'},
            {'z1': '0.1', 'r1': '0.1', 'z2': '0.1', 'r2': None, 'z3': '0.1', 'r3': '0.1'},
            {'z1': '0.1', 'r1': '0.1', 'z2': '0.1', 'r2': '0.1', 'z3': None, 'r3': '0.1'},
            {'z1': '0.1', 'r1': '0.1', 'z2': '0.1', 'r2': '0.1', 'z3': '0.1', 'r3': None},
            {'z1': 0.1, 'r1': 0.1, 'z2': 0.1, 'r2': 0.1, 'z3': 0.1, 'r3': 0.1},
            {
                'z1': _utils.REAL,
                'r1': _utils.REAL,
                'z2': _utils.REAL,
                'r2': _utils.REAL,
                'z3': _utils.REAL,
                'r3': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {'z1': None, 'r1': '0.1', 'z2': '0.1', 'r2': '0.1', 'z3': '0.1', 'r3': '0.1'},
            {'z1': '0.1', 'r1': None, 'z2': '0.1', 'r2': '0.1', 'z3': '0.1', 'r3': '0.1'},
        ]


class Test_Box:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Box
        EXAMPLES_VALID = [
            'BOX -1 -1 -1 2 0 0 0 2 0 0 0 2',
        ]
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Box
        EXAMPLES = [
            'box 0 0 0 1 0 0 0 1 0 0 0 1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.BoxBuilder
        EXAMPLES_VALID = [
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': 0.1,
                'vy': 0.1,
                'vz': 0.1,
                'a1x': 0.1,
                'a1y': 0.1,
                'a1z': 0.1,
                'a2x': 0.1,
                'a2y': 0.1,
                'a2z': 0.1,
                'a3x': 0.1,
                'a3y': 0.1,
                'a3z': 0.1,
            },
            {
                'vx': _utils.REAL,
                'vy': _utils.REAL,
                'vz': _utils.REAL,
                'a1x': _utils.REAL,
                'a1y': _utils.REAL,
                'a1z': _utils.REAL,
                'a2x': _utils.REAL,
                'a2y': _utils.REAL,
                'a2z': _utils.REAL,
                'a3x': _utils.REAL,
                'a3y': _utils.REAL,
                'a3z': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'vx': None,
                'vy': '0.1',
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': None,
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': None,
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'a1x': None,
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': None,
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': None,
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': None,
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': None,
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': None,
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': None,
                'a3y': '0.1',
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': None,
                'a3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'a1x': '0.1',
                'a1y': '0.1',
                'a1z': '0.1',
                'a2x': '0.1',
                'a2y': '0.1',
                'a2z': '0.1',
                'a3x': '0.1',
                'a3y': '0.1',
                'a3z': None,
            },
        ]


class Test_Rpp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Rpp
        EXAMPLES_VALID = [
            'RPP -1 1 -1 1 -1 1',
            'RPP -1 1 -1 1',
        ]
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Rpp
        EXAMPLES = ['rpp 1 2 3 4 5 6']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.RppBuilder
        EXAMPLES_VALID = [
            {
                'xmin': '0.1',
                'xmax': '0.1',
                'ymin': '0.1',
                'ymax': '0.1',
                'zmin': '0.1',
                'zmax': '0.1',
            },
            {
                'xmin': '0.1',
                'xmax': '0.1',
                'ymin': '0.1',
                'ymax': '0.1',
                'zmin': None,
                'zmax': '0.1',
            },
            {
                'xmin': '0.1',
                'xmax': '0.1',
                'ymin': '0.1',
                'ymax': '0.1',
                'zmin': '0.1',
                'zmax': None,
            },
            {'xmin': 0.1, 'xmax': 0.1, 'ymin': 0.1, 'ymax': 0.1, 'zmin': 0.1, 'zmax': 0.1},
            {
                'xmin': _utils.REAL,
                'xmax': _utils.REAL,
                'ymin': _utils.REAL,
                'ymax': _utils.REAL,
                'zmin': _utils.REAL,
                'zmax': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'xmin': None,
                'xmax': '0.1',
                'ymin': '0.1',
                'ymax': '0.1',
                'zmin': '0.1',
                'zmax': '0.1',
            },
            {
                'xmin': '0.1',
                'xmax': None,
                'ymin': '0.1',
                'ymax': '0.1',
                'zmin': '0.1',
                'zmax': '0.1',
            },
            {
                'xmin': '0.1',
                'xmax': '0.1',
                'ymin': None,
                'ymax': '0.1',
                'zmin': '0.1',
                'zmax': '0.1',
            },
            {
                'xmin': '0.1',
                'xmax': '0.1',
                'ymin': '0.1',
                'ymax': None,
                'zmin': '0.1',
                'zmax': '0.1',
            },
        ]


class Test_Sph:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Sph
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Sph
        EXAMPLES = ['sph 1 2 3 4']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.SphBuilder
        EXAMPLES_VALID = [
            {'vx': '0.1', 'vy': '0.1', 'vz': '0.1', 'r': '0.1'},
            {'vx': 0.1, 'vy': 0.1, 'vz': 0.1, 'r': 0.1},
            {'vx': _utils.REAL, 'vy': _utils.REAL, 'vz': _utils.REAL, 'r': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'vx': None, 'vy': '0.1', 'vz': '0.1', 'r': '0.1'},
            {'vx': '0.1', 'vy': None, 'vz': '0.1', 'r': '0.1'},
            {'vx': '0.1', 'vy': '0.1', 'vz': None, 'r': '0.1'},
            {'vx': '0.1', 'vy': '0.1', 'vz': '0.1', 'r': None},
        ]


class Test_Rcc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Rcc
        EXAMPLES_VALID = [
            'RCC 0 -5 0 0 10 0 4',
        ]
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Rcc
        EXAMPLES = ['rcc 1 2 3 4 5 6 7']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.RccBuilder
        EXAMPLES_VALID = [
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r': '0.1',
            },
            {'vx': 0.1, 'vy': 0.1, 'vz': 0.1, 'hx': 0.1, 'hy': 0.1, 'hz': 0.1, 'r': 0.1},
            {
                'vx': _utils.REAL,
                'vy': _utils.REAL,
                'vz': _utils.REAL,
                'hx': _utils.REAL,
                'hy': _utils.REAL,
                'hz': _utils.REAL,
                'r': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'vx': None,
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r': '0.1',
            },
            {
                'vx': '0.1',
                'vy': None,
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': None,
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': None,
                'hy': '0.1',
                'hz': '0.1',
                'r': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': None,
                'hz': '0.1',
                'r': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': None,
                'r': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r': None,
            },
        ]


class Test_Rhp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Rhp
        EXAMPLES_VALID = [
            'RHP 0 0 -4 0 0 8 0 2 0',
        ]
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Rhp
        EXAMPLES = ['rhp 1 2 3 4 5 6 7 8 9 2 3 4 5 6 7']

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.RhpBuilder
        EXAMPLES_VALID = [
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': None,
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': None,
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': None,
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': None,
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': None,
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': None,
            },
            {
                'vx': 0.1,
                'vy': 0.1,
                'vz': 0.1,
                'hx': 0.1,
                'hy': 0.1,
                'hz': 0.1,
                'r1': 0.1,
                'r2': 0.1,
                'r3': 0.1,
                's1': 0.1,
                's2': 0.1,
                's3': 0.1,
                't1': 0.1,
                't2': 0.1,
                't3': 0.1,
            },
            {
                'vx': _utils.REAL,
                'vy': _utils.REAL,
                'vz': _utils.REAL,
                'hx': _utils.REAL,
                'hy': _utils.REAL,
                'hz': _utils.REAL,
                'r1': _utils.REAL,
                'r2': _utils.REAL,
                'r3': _utils.REAL,
                's1': _utils.REAL,
                's2': _utils.REAL,
                's3': _utils.REAL,
                't1': _utils.REAL,
                't2': _utils.REAL,
                't3': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': None,
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': None,
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': None,
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': None,
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': None,
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': None,
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': None,
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': None,
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': None,
                'r1': '0.1',
                'r2': '0.1',
                'r3': '0.1',
                's1': '0.1',
                's2': '0.1',
                's3': '0.1',
                't1': '0.1',
                't2': '0.1',
                't3': '0.1',
            },
        ]


class Test_Rec:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Rec
        EXAMPLES_VALID = [
            'REC 0 -5 0 0 10 0 4 0 0 2',
        ]
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Rec
        EXAMPLES = [
            'rec 1 2 3 4 5 6 7 8 9 1 2 3',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.RecBuilder
        EXAMPLES_VALID = [
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': None,
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': None,
            },
            {
                'vx': 0.1,
                'vy': 0.1,
                'vz': 0.1,
                'hx': 0.1,
                'hy': 0.1,
                'hz': 0.1,
                'v1x': 0.1,
                'v1y': 0.1,
                'v1z': 0.1,
                'v2x': 0.1,
                'v2y': 0.1,
                'v2z': 0.1,
            },
            {
                'vx': _utils.REAL,
                'vy': _utils.REAL,
                'vz': _utils.REAL,
                'hx': _utils.REAL,
                'hy': _utils.REAL,
                'hz': _utils.REAL,
                'v1x': _utils.REAL,
                'v1y': _utils.REAL,
                'v1z': _utils.REAL,
                'v2x': _utils.REAL,
                'v2y': _utils.REAL,
                'v2z': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'vx': None,
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': None,
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': None,
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': None,
                'hy': '0.1',
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': None,
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': None,
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'v1x': None,
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': None,
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': None,
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': None,
                'v2y': '0.1',
                'v2z': '0.1',
            },
        ]


class Test_Trc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Trc
        EXAMPLES_VALID = [
            'TRC -5 0 0 10 0 0 4 2',
        ]
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Trc
        EXAMPLES = [
            'trc 1 2 3 4 5 6 7 8',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.TrcBuilder
        EXAMPLES_VALID = [
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
            },
            {
                'vx': 0.1,
                'vy': 0.1,
                'vz': 0.1,
                'hx': 0.1,
                'hy': 0.1,
                'hz': 0.1,
                'r1': 0.1,
                'r2': 0.1,
            },
            {
                'vx': _utils.REAL,
                'vy': _utils.REAL,
                'vz': _utils.REAL,
                'hx': _utils.REAL,
                'hy': _utils.REAL,
                'hz': _utils.REAL,
                'r1': _utils.REAL,
                'r2': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'vx': None,
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
            },
            {
                'vx': '0.1',
                'vy': None,
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': None,
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': None,
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': None,
                'hz': '0.1',
                'r1': '0.1',
                'r2': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': None,
                'r1': '0.1',
                'r2': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': None,
                'r2': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'r1': '0.1',
                'r2': None,
            },
        ]


class Test_Ell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Ell
        EXAMPLES_VALID = [
            'ELL 0. 0. -2.236068 0. 0. 2.236068 3.',
            'ELL 0. 0. 0. 0. 0. 3. -2',
        ]
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Ell
        EXAMPLES = [
            'ell 1 2 3 4 5 6 7',
            'ell 1 2 3 4 5 6 -7',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.EllBuilder
        EXAMPLES_VALID = [
            {
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'rm': '0.1',
            },
            {'v1x': 0.1, 'v1y': 0.1, 'v1z': 0.1, 'v2x': 0.1, 'v2y': 0.1, 'v2z': 0.1, 'rm': 0.1},
            {
                'v1x': _utils.REAL,
                'v1y': _utils.REAL,
                'v1z': _utils.REAL,
                'v2x': _utils.REAL,
                'v2y': _utils.REAL,
                'v2z': _utils.REAL,
                'rm': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'v1x': None,
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'rm': '0.1',
            },
            {
                'v1x': '0.1',
                'v1y': None,
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'rm': '0.1',
            },
            {
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': None,
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'rm': '0.1',
            },
            {
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': None,
                'v2y': '0.1',
                'v2z': '0.1',
                'rm': '0.1',
            },
            {
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': None,
                'v2z': '0.1',
                'rm': '0.1',
            },
            {
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': None,
                'rm': '0.1',
            },
            {
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'rm': None,
            },
        ]


class Test_Wed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Wed
        EXAMPLES_VALID = [
            'WED 0 0 -6 4 0 0 0 3 0 0 0 12',
        ]
        EXAMPLES_INVALID = []

    class Test_Draw(_utils._Test_Draw):
        element = pymcnp.inp.surface.Wed
        EXAMPLES = [
            'wed 1 2 3 4 5 6 7 8 9 1 2 3',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.WedBuilder
        EXAMPLES_VALID = [
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': 0.1,
                'vy': 0.1,
                'vz': 0.1,
                'v1x': 0.1,
                'v1y': 0.1,
                'v1z': 0.1,
                'v2x': 0.1,
                'v2y': 0.1,
                'v2z': 0.1,
                'v3x': 0.1,
                'v3y': 0.1,
                'v3z': 0.1,
            },
            {
                'vx': _utils.REAL,
                'vy': _utils.REAL,
                'vz': _utils.REAL,
                'v1x': _utils.REAL,
                'v1y': _utils.REAL,
                'v1z': _utils.REAL,
                'v2x': _utils.REAL,
                'v2y': _utils.REAL,
                'v2z': _utils.REAL,
                'v3x': _utils.REAL,
                'v3y': _utils.REAL,
                'v3z': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'vx': None,
                'vy': '0.1',
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': None,
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': None,
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'v1x': None,
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': None,
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': None,
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': None,
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': None,
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': None,
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': None,
                'v3y': '0.1',
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': None,
                'v3z': '0.1',
            },
            {
                'vx': '0.1',
                'vy': '0.1',
                'vz': '0.1',
                'v1x': '0.1',
                'v1y': '0.1',
                'v1z': '0.1',
                'v2x': '0.1',
                'v2y': '0.1',
                'v2z': '0.1',
                'v3x': '0.1',
                'v3y': '0.1',
                'v3z': None,
            },
        ]


class Test_Arb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.surface.Arb
        EXAMPLES_VALID = [
            'ARB -5 -10 -5 -5 -10 5 5 -10 -5 5 -10 5 &\n     0 12 0 0 0 0 0 0 0 0 0 0 &\n     1234 1250 1350 2450 3450 0',
        ]
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.surface.ArbBuilder
        EXAMPLES_VALID = [
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': 0.1,
                'ay': 0.1,
                'az': 0.1,
                'bx': 0.1,
                'by': 0.1,
                'bz': 0.1,
                'cx': 0.1,
                'cy': 0.1,
                'cz': 0.1,
                'dx': 0.1,
                'dy': 0.1,
                'dz': 0.1,
                'ex': 0.1,
                'ey': 0.1,
                'ez': 0.1,
                'fx': 0.1,
                'fy': 0.1,
                'fz': 0.1,
                'gx': 0.1,
                'gy': 0.1,
                'gz': 0.1,
                'hx': 0.1,
                'hy': 0.1,
                'hz': 0.1,
                'n1': 0.1,
                'n2': 0.1,
                'n3': 0.1,
                'n4': 0.1,
                'n5': 0.1,
                'n6': 0.1,
            },
            {
                'ax': _utils.REAL,
                'ay': _utils.REAL,
                'az': _utils.REAL,
                'bx': _utils.REAL,
                'by': _utils.REAL,
                'bz': _utils.REAL,
                'cx': _utils.REAL,
                'cy': _utils.REAL,
                'cz': _utils.REAL,
                'dx': _utils.REAL,
                'dy': _utils.REAL,
                'dz': _utils.REAL,
                'ex': _utils.REAL,
                'ey': _utils.REAL,
                'ez': _utils.REAL,
                'fx': _utils.REAL,
                'fy': _utils.REAL,
                'fz': _utils.REAL,
                'gx': _utils.REAL,
                'gy': _utils.REAL,
                'gz': _utils.REAL,
                'hx': _utils.REAL,
                'hy': _utils.REAL,
                'hz': _utils.REAL,
                'n1': _utils.REAL,
                'n2': _utils.REAL,
                'n3': _utils.REAL,
                'n4': _utils.REAL,
                'n5': _utils.REAL,
                'n6': _utils.REAL,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'ax': None,
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': None,
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': None,
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': None,
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': None,
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': None,
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': None,
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': None,
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': None,
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': None,
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': None,
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': None,
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': None,
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': None,
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': None,
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': None,
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': None,
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': None,
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': None,
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': None,
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': None,
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': None,
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': None,
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': None,
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': None,
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': None,
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': None,
                'n4': '0.1',
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': None,
                'n5': '0.1',
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': None,
                'n6': '0.1',
            },
            {
                'ax': '0.1',
                'ay': '0.1',
                'az': '0.1',
                'bx': '0.1',
                'by': '0.1',
                'bz': '0.1',
                'cx': '0.1',
                'cy': '0.1',
                'cz': '0.1',
                'dx': '0.1',
                'dy': '0.1',
                'dz': '0.1',
                'ex': '0.1',
                'ey': '0.1',
                'ez': '0.1',
                'fx': '0.1',
                'fy': '0.1',
                'fz': '0.1',
                'gx': '0.1',
                'gy': '0.1',
                'gz': '0.1',
                'hx': '0.1',
                'hy': '0.1',
                'hz': '0.1',
                'n1': '0.1',
                'n2': '0.1',
                'n3': '0.1',
                'n4': '0.1',
                'n5': '0.1',
                'n6': None,
            },
        ]
