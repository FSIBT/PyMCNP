import pymcnp
from ..... import _utils


class Test_Ngroup:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ngroup
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NgroupBuilder
        EXAMPLES_VALID = [{'value': '1'}, {'value': 1}, {'value': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'value': None}]


class Test_Isn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Isn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IsnBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Niso:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Niso
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NisoBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Mt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Mt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.MtBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Iquad:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Iquad
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IquadBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Fmmix:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Fmmix
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.FmmixBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Nosolv:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Nosolv
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NosolvBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Noedit:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Noedit
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NoeditBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Nogeod:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Nogeod
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NogeodBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Nomix:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Nomix
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NomixBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Noasg:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Noasg
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NoasgBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Nomacr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Nomacr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NomacrBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Noslnp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Noslnp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NoslnpBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Noedtt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Noedtt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NoedttBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Noadjm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Noadjm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NoadjmBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Lib:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Lib
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.LibBuilder
        EXAMPLES_VALID = [
            {'setting': 'a'},
            {'setting': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Libname:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Libname
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.LibnameBuilder
        EXAMPLES_VALID = [
            {'setting': 'a'},
            {'setting': pymcnp.utils.types.String('a')},
        ]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Fissneut:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Fissneut
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.FissneutBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Lng:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Lng
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.LngBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Balxs:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Balxs
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.BalxsBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ntichi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ntichi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NtichiBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ievt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ievt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IevtBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Isct:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Isct
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IsctBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ith:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ith
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IthBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Trcor:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Trcor
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.TrcorBuilder
        EXAMPLES_VALID = [{'setting': 'diag'}, {'setting': pymcnp.utils.types.String('diag')}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ibl:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibl
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IblBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ibr:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibr
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IbrBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ibt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IbtBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ibb:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibb
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IbbBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ibfrnt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibfrnt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IbfrntBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ibback:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ibback
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.IbbackBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Epsi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Epsi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.EpsiBuilder
        EXAMPLES_VALID = [{'setting': '1.0'}, {'setting': 1.0}, {'setting': _utils.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Oitm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Oitm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.OitmBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Nosigf:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Nosigf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NosigfBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Srcacc:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Srcacc
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.SrcaccBuilder
        EXAMPLES_VALID = [{'setting': 'no'}, {'setting': pymcnp.utils.types.String('no')}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Diffsol:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Diffsol
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.DiffsolBuilder
        EXAMPLES_VALID = [{'setting': 'a'}, {'setting': pymcnp.utils.types.String('a')}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Tsasn:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Tsasn
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.TsasnBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Tsaepsi:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Tsaepsi
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.TsaepsiBuilder
        EXAMPLES_VALID = [{'setting': '1.0'}, {'setting': 1.0}, {'setting': _utils.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Tsaits:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Tsaits
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.TsaitsBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Tsabeta:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Tsabeta
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.TsabetaBuilder
        EXAMPLES_VALID = [{'setting': '1.0'}, {'setting': 1.0}, {'setting': _utils.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ptconv:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ptconv
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.PtconvBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Norm:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Norm
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.NormBuilder
        EXAMPLES_VALID = [{'setting': '1.0'}, {'setting': 1.0}, {'setting': _utils.REAL}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Xsectp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Xsectp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.XsectpBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Fissrp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Fissrp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.FissrpBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Sourcp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Sourcp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.SourcpBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Angp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Angp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.AngpBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Balp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Balp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.BalpBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Raflux:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Raflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.RafluxBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Rmflux:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Rmflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.RmfluxBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Avatar:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Avatar
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.AvatarBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Asleft:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Asleft
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.AsleftBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Asrite:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Asrite
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.AsriteBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Asbott:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Asbott
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.AsbottBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Astop:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Astop
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.AstopBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Asfrnt:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Asfrnt
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.AsfrntBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Asback:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Asback
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.AsbackBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Massed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Massed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.MassedBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Pted:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Pted
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.PtedBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Zned:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Zned
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.ZnedBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Rzflux:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Rzflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.RzfluxBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Rzmflux:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Rzmflux
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.RzmfluxBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Edoutf:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Edoutf
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.EdoutfBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Byvolp:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Byvolp
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.ByvolpBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Ajed:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Ajed
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.AjedBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]


class Test_Fluxone:
    class Test_FromMcnp(_utils._Test_FromMcnp):
        element = pymcnp.inp.data.dawwg.block.Fluxone
        EXAMPLES_VALID = []
        EXAMPLES_INVALID = []

    class Test_Build(_utils._Test_Build):
        element = pymcnp.inp.data.dawwg.block.FluxoneBuilder
        EXAMPLES_VALID = [{'setting': '1'}, {'setting': 1}, {'setting': _utils.INTEGER}]
        EXAMPLES_INVALID = [{'setting': None}]
