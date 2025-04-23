import pymcnp
import _utils


class Test_Cell:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.Cell
        EXAMPLES_VALID = [
            '3 0 -1 2 -4 $ definition of cell 3',
            '5 0 #3',
            '5 0 #(-1 2 -4)',
            '5 0 (+1 : -2 : +4)',
            '2 3 -3.7 -1 IMP:N=2 IMP:P=4',
            '10 16 -4.2 1 -2 3 IMP:N=4 IMP:P=8 EXT:N=-0.4',
            '1 0 -17',
            '1 0 1 -2 -3 4 -5 6 fill=1',
            '2 0 -7 1 -3 8 u=1 fill=2 lat=1',
            '3 0 -11 u=-2',
            '4 0 11 u=2',
            '5 0 -1:2:3:-4:5:-6',
        ]
        EXAMPLES_INVALID = []


class Test_CellImp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Imp
        EXAMPLES_VALID = [
            'imp:n,p=0.5',
            'imp:n=1.5',
            'imp:n,#=-0.5',
        ]
        EXAMPLES_INVALID = []


class Test_CellVol:
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


class Test_CellPwt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Pwt
        EXAMPLES_VALID = [
            'pwt=0.5',
            'pwt=1.5',
            'pwt=-0.5',
        ]
        EXAMPLES_INVALID = []


class Test_CellExt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Ext
        EXAMPLES_VALID = [
            'ext:n,p=0.5',
            'ext:n=0.9',
            'ext:n,#=-0.5',
        ]
        EXAMPLES_INVALID = []


class Test_CellFcl:
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


class Test_CellWwn:
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


class Test_CellDxc:
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


class Test_CellNonu:
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


class Test_CellPd:
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


class Test_CellTmp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Tmp
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


class Test_CellU:
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


class Test_CellTrcl_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_0
        EXAMPLES_VALID = [
            'trcl=1',
            'trcl=67',
            'trcl=999',
        ]
        EXAMPLES_INVALID = [
            'trcl=-1000',
            'trcl=1000',
            'trcl=2343',
        ]


class Test_CellTrcl_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellTrcl_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellTrcl_3:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_3
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellTrcl_4:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_4
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellTrcl_5:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Trcl_5
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellLat:
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


class Test_CellFill_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_0
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


class Test_CellFill_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellFill_2:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_2
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellFill_3:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_3
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellFill_4:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_4
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellFill_5:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_5
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellFill_6:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Fill_6
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellElpt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Elpt
        EXAMPLES_VALID = [
            'elpt:n,p=-234.05434',
            'elpt:n=345034950',
            'elpt:n,#=34534.3453',
        ]
        EXAMPLES_INVALID = []


class Test_CellTmp_0:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Tmp_0
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellTmp_1:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.cell.Tmp_1
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []


class Test_CellCosy:
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


class Test_CellBflcl:
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


class Test_CellUnc:
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
