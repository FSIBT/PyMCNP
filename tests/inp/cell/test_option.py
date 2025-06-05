import pymcnp
from ... import _utils


class Test_Imp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Imp
        EXAMPLES_VALID = [
            'imp:n,p=0.5',
            'imp:n=1.5',
            'imp:n,#=-0.5',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.ImpBuilder
        EXAMPLES_VALID = [
            {'designator': 'n', 'importance': '0.1'},
            {'designator': 'n', 'importance': 0.1},
            {'designator': _utils.DESIGNATOR, 'importance': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'designator': None, 'importance': '0.1'},
            {'designator': 'n', 'importance': None},
        ]


class Test_Vol:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Vol
        EXAMPLES_VALID = [
            'vol=0.5',
            'vol=1.5',
            'vol=0.0',
        ]
        EXAMPLES_INVALID = [
            'vol=-22',
            'vol=-1',
            'vol=-32423',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.VolBuilder
        EXAMPLES_VALID = [
            {'volume': '0.1'},
            {'volume': 0.1},
            {'volume': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'volume': None},
        ]


class Test_Pwt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Pwt
        EXAMPLES_VALID = [
            'pwt=0.5',
            'pwt=1.5',
            'pwt=-0.5',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.PwtBuilder
        EXAMPLES_VALID = [
            {'weight': '0.1'},
            {'weight': 0.1},
            {'weight': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'weight': None},
        ]


class Test_Ext:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Ext
        EXAMPLES_VALID = [
            'ext:n,p=0.5',
            'ext:n=0.9',
            'ext:n,#=-0.5',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.ExtBuilder
        EXAMPLES_VALID = [
            {'designator': 'n', 'stretch': '1'},
            {'designator': 'n', 'stretch': _utils.STRING},
            {'designator': _utils.DESIGNATOR, 'stretch': '1'},
            {
                'designator': _utils.DESIGNATOR,
                'stretch': _utils.STRING,
            },
        ]
        EXAMPLES_INVALID = [
            {'designator': None, 'stretch': '1'},
            {'designator': 'n', 'stretch': None},
        ]


class Test_Fcl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fcl
        EXAMPLES_VALID = [
            'fcl:n,p=0.5',
            'fcl:n=0.9',
            'fcl:n,#=-0.5',
        ]
        EXAMPLES_INVALID = [
            'fcl:n,p=2.51',
            'fcl:n=3.94',
            'fcl:n,#=-1.3',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FclBuilder
        EXAMPLES_VALID = [
            {'designator': 'n', 'control': '0.1'},
            {'designator': 'n', 'control': 0.1},
            {'designator': _utils.DESIGNATOR, 'control': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'designator': None, 'control': '0.1'},
            {'designator': 'n', 'control': None},
        ]


class Test_Wwn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Wwn
        EXAMPLES_VALID = [
            'wwn3:n,p=1',
            'wwn4:e=0',
            'wwn6:#=-1',
        ]
        EXAMPLES_INVALID = [
            'wwn4:_=-2',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.WwnBuilder
        EXAMPLES_VALID = [
            {'suffix': '1', 'designator': 'n', 'bound': '1.1'},
            {'suffix': 1, 'designator': 'n', 'bound': 1.1},
            {'suffix': _utils.INTEGER, 'designator': _utils.DESIGNATOR, 'bound': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'designator': 'n', 'bound': '1.1'},
            {'suffix': '1', 'designator': None, 'bound': '1.1'},
            {'suffix': '1', 'designator': 'n', 'bound': None},
        ]


class Test_Dxc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Dxc
        EXAMPLES_VALID = [
            'dxc3:n,p=0.5',
            'dxc8:n=0.9',
            'dxc2:n,#=0.0',
        ]
        EXAMPLES_INVALID = [
            'dxc2:n=-1.0',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.DxcBuilder
        EXAMPLES_VALID = [
            {'suffix': '2', 'designator': 'n', 'probability': '0.5'},
            {'suffix': 2, 'designator': 'n', 'probability': 0.5},
            {'suffix': _utils.INTEGER, 'designator': _utils.DESIGNATOR, 'probability': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {
                'suffix': None,
                'designator': 'n',
                'probability': '0.5',
            },
            {
                'suffix': '2',
                'designator': None,
                'probability': '0.5',
            },
            {
                'suffix': '2',
                'designator': 'n',
                'probability': None,
            },
        ]


class Test_Nonu:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Nonu
        EXAMPLES_VALID = [
            'nonu=0',
            'nonu=1',
            'nonu=2',
        ]
        EXAMPLES_INVALID = [
            'nonu=-1',
            'nonu=3',
            'nonu=100',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.NonuBuilder
        EXAMPLES_VALID = [
            {'setting': '1'},
            {'setting': 1},
            {'setting': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'setting': None},
        ]


class Test_Pd:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Pd
        EXAMPLES_VALID = [
            'pd5=0',
            'pd7=0.5',
            'pd3=1',
        ]
        EXAMPLES_INVALID = [
            'pd1=-1',
            'pd3=2',
            'pd5=100',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.PdBuilder
        EXAMPLES_VALID = [
            {'suffix': '1', 'probability': '0.5'},
            {'suffix': 1, 'probability': 0.5},
            {'suffix': _utils.INTEGER, 'probability': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'probability': '0.5'},
            {'suffix': '1', 'probability': None},
        ]


class Test_U:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.U
        EXAMPLES_VALID = [
            'u=-99999999',
            'u=99999999',
            'u=0',
            'u=1',
            'u=-1',
        ]
        EXAMPLES_INVALID = [
            'u=-100000000',
            'u=100000000',
            'u=100000432',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.UBuilder
        EXAMPLES_VALID = [
            {'number': '1'},
            {'number': 1},
            {'number': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'number': None},
        ]


class Test_Trcl_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_0
        EXAMPLES_VALID = [
            'trcl=1',
            'trcl=67',
            'trcl=999',
            # 3.3
            'trcl=0',
        ]
        EXAMPLES_INVALID = [
            'trcl=-1000',
            'trcl=1000',
            'trcl=2343',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_0
        EXAMPLES_VALID = [
            {'transformation': '1'},
            {'transformation': 1},
            {'transformation': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'transformation': None},
        ]


class Test_Trcl_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_1
        EXAMPLES_VALID = [
            'TRCL 0 0 0 1 0 0 0 1 0 0 0 1 1',
        ]
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_1
        EXAMPLES_VALID = [
            {'transformation': '1 1 1 2 2 2 3 3 3 4 4 4'},
            {'transformation': _utils.TRANSFORMATION_0},
        ]
        EXAMPLES_INVALID = [
            {'transformation': None},
        ]


class Test_Trcl_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_2
        EXAMPLES_VALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_2
        EXAMPLES_VALID = [
            {'transformation': '1 1 1 2 2 2 3 3 3'},
            {'transformation': _utils.TRANSFORMATION_1},
        ]
        EXAMPLES_INVALID = [
            {'transformation': None},
        ]


class Test_Trcl_3:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_3
        EXAMPLES_VALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_3
        EXAMPLES_VALID = [
            {'transformation': '1 1 1 2 2 2 3 3'},
            {'transformation': _utils.TRANSFORMATION_2},
        ]
        EXAMPLES_INVALID = [
            {'transformation': None},
        ]


class Test_Trcl_4:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_4
        EXAMPLES_VALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_4
        EXAMPLES_VALID = [
            {'transformation': '1 1 1 2 2 2'},
            {'transformation': _utils.TRANSFORMATION_3},
        ]
        EXAMPLES_INVALID = [
            {'transformation': None},
        ]


class Test_Trcl_5:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_5
        EXAMPLES_VALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TrclBuilder_5
        EXAMPLES_VALID = [
            {'transformation': '1 1 1'},
            {'transformation': _utils.TRANSFORMATION_4},
        ]
        EXAMPLES_INVALID = [
            {'transformation': None},
        ]


class Test_Lat:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Lat
        EXAMPLES_VALID = [
            'lat=1',
            'lat=2',
        ]
        EXAMPLES_INVALID = [
            'lat=-1',
            'lat=9',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.LatBuilder
        EXAMPLES_VALID = [
            {'shape': '2'},
            {'shape': 2},
            {'shape': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'shape': None},
        ]


class Test_Fill_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_0
        EXAMPLES_VALID = [
            'FILL=0:2 1:2 0:1 4 4 2 $ i=0,1,2 for j=1 & k=0\n     0 4 0 $ i=0,1,2 for j=2 & k=0\n     0 3 3 $ i=0,1,2 for j=1 & k=1\n     4 4 0 $ i=0,1,2 for j=2 & k=1',
        ]
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FillBuilder_0
        EXAMPLES_VALID = [
            {
                'i': '2:3',
                'j': '2:3',
                'k': '2:3',
                'universes': ['3'],
            },
            {
                'i': '2:3',
                'j': '2:3',
                'k': '2:3',
                'universes': ['3'],
                'm': '5',
            },
            {
                'i': '2:3',
                'j': '2:3',
                'k': '2:3',
                'universes': [3],
                'm': 5,
            },
            {
                'i': _utils.INDEX,
                'j': _utils.INDEX,
                'k': _utils.INDEX,
                'universes': [_utils.INTEGER],
                'm': _utils.INTEGER,
            },
        ]
        EXAMPLES_INVALID = [
            {
                'i': None,
                'j': '2:3',
                'k': '2:3',
                'universes': ['3'],
            },
            {
                'i': '2:3',
                'j': None,
                'k': '2:3',
                'universes': ['3'],
            },
            {
                'i': '2:3',
                'j': '2:3',
                'k': None,
                'universes': ['3'],
            },
            {
                'i': '2:3',
                'j': '2:3',
                'k': '2:3',
                'universes': None,
            },
        ]


class Test_Fill_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_1
        EXAMPLES_VALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FillBuilder_1
        EXAMPLES_VALID = [
            {'universe': '3', 'transformation': '1 1 1 2 2 2 3 3 3 4 4 4'},
            {'universe': 3, 'transformation': None},
            {'universe': _utils.INTEGER, 'transformation': _utils.TRANSFORMATION_0},
        ]
        EXAMPLES_INVALID = [
            {'universe': None, 'transformation': None},
        ]


class Test_Fill_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_2
        EXAMPLES_VALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FillBuilder_2
        EXAMPLES_VALID = [
            {'universe': '3', 'transformation': None},
            {'universe': 3, 'transformation': '1 1 1 2 2 2 3 3 3'},
            {'universe': _utils.INTEGER, 'transformation': _utils.TRANSFORMATION_1},
        ]
        EXAMPLES_INVALID = [
            {'universe': None},
        ]


class Test_Fill_3:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_3
        EXAMPLES_VALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FillBuilder_3
        EXAMPLES_VALID = [
            {'universe': '3'},
            {'universe': 3, 'transformation': '1 1 1 2 2 2 3 3'},
            {'universe': _utils.INTEGER, 'transformation': _utils.TRANSFORMATION_2},
        ]
        EXAMPLES_INVALID = [
            {'universe': None},
        ]


class Test_Fill_4:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_4
        EXAMPLES_VALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FillBuilder_4
        EXAMPLES_VALID = [
            {'universe': '3'},
            {'universe': 3, 'transformation': '1 1 1 2 2 2'},
            {'universe': _utils.INTEGER, 'transformation': _utils.TRANSFORMATION_3},
        ]
        EXAMPLES_INVALID = [
            {'universe': None},
        ]


class Test_Fill_5:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_5
        EXAMPLES_VALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FillBuilder_5
        EXAMPLES_VALID = [
            {'universe': '3'},
            {'universe': 3, 'transformation': '1 1 1'},
            {'universe': _utils.INTEGER, 'transformation': _utils.TRANSFORMATION_4},
        ]
        EXAMPLES_INVALID = [
            {'universe': None},
        ]


class Test_Fill_6:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_6
        EXAMPLES_VALID = [
            'fill=0',
            'fill=1',
            'fill=0 1',
            'fill=1 0',
            'fill=0 0',
            'fill=1 1',
        ]
        EXAMPLES_INVALID = [
            'fill=-1',
            'fill=-1 1',
            'fill=1 -1',
            'fill=1 91232',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.FillBuilder_6
        EXAMPLES_VALID = [
            {'universe': '3', 'transformation': None},
            {'universe': '3', 'transformation': '4'},
            {'universe': 3, 'transformation': 3},
            {'universe': _utils.INTEGER, 'transformation': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'universe': None, 'transformation': None},
        ]


class Test_Elpt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Elpt
        EXAMPLES_VALID = [
            'elpt:n,p=-234.05434',
            'elpt:n=345034950',
            'elpt:n,#=34534.3453',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.ElptBuilder
        EXAMPLES_VALID = [
            {'designator': 'n', 'cutoff': '2.1'},
            {'designator': 'n', 'cutoff': 2.1},
            {'designator': _utils.DESIGNATOR, 'cutoff': _utils.REAL},
        ]
        EXAMPLES_INVALID = [
            {'designator': None, 'cutoff': '2.1'},
            {'designator': 'n', 'cutoff': None},
        ]


class Test_Tmp_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Tmp_0
        EXAMPLES_VALID = [
            'tmp1=4.26',
            'tmp5=3.14',
            'tmp7=0.24',
            'tmp3=9.43',
        ]
        EXAMPLES_INVALID = [
            'tmp1=-0.53',
            'tmp2-0.0',
            'tmp5=-1.43',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TmpBuilder_0
        EXAMPLES_VALID = [
            {'suffix': '1', 'temperature': ['10']},
            {'suffix': 1, 'temperature': [11.2]},
            {'suffix': _utils.INTEGER, 'temperature': [_utils.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'suffix': None, 'temperature': ['10', 11.2, _utils.REAL]},
            {'suffix': '1', 'temperature': None},
        ]


class Test_Tmp_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Tmp_1
        EXAMPLES_VALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.TmpBuilder_1
        EXAMPLES_VALID = [
            {'temperature': ['10', 11.2, _utils.REAL]},
        ]
        EXAMPLES_INVALID = [
            {'temperature': None},
        ]


class Test_Cosy:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Cosy
        EXAMPLES_VALID = [
            'cosy=1',
            'cosy=2',
            'cosy=3',
            'cosy=4',
            'cosy=5',
            'cosy=6',
        ]
        EXAMPLES_INVALID = [
            'cosy=0',
            'cosy=100000000',
            'cosy=-1',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.CosyBuilder
        EXAMPLES_VALID = [
            {'number': '1'},
            {'number': 1},
            {'number': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'number': None},
        ]


class Test_Bflcl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Bflcl
        EXAMPLES_VALID = [
            'bflcl=0',
            'bflcl=4',
            'bflcl=10',
        ]
        EXAMPLES_INVALID = [
            'bflcl=-1',
            'bflcl=-345',
            'bflcl=-1000',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.BflclBuilder
        EXAMPLES_VALID = [
            {'number': '0'},
            {'number': 0},
            {'number': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'number': None},
        ]


class Test_Unc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Unc
        EXAMPLES_VALID = [
            'unc:p=1',
            'unc:e=0',
        ]
        EXAMPLES_INVALID = [
            'unc:n,#=-1',
            'unc:@,#=345',
            'unc:e=-1000',
            'unc:p,_=2',
        ]

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.cell.UncBuilder
        EXAMPLES_VALID = [
            {'designator': 'n', 'setting': '0'},
            {'designator': 0, 'setting': 0},
            {'designator': _utils.DESIGNATOR, 'setting': _utils.INTEGER},
        ]
        EXAMPLES_INVALID = [
            {'designator': None, 'setting': 0},
            {'designator': 'n', 'setting': None},
        ]
