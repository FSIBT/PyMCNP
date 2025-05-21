import re
import typing
import dataclasses

from . import data
from ._card import Card
from ..utils import types
from ..utils import errors
from ..utils import _parser


class Data(Card):
    """
    Represents INP data elements.

    Attributes:
        InpError: SEMANTICS_CARD.
    """

    _ATTRS = {'option': data.DataOption}

    _REGEX = re.compile(rf'\A({data.DataOption._REGEX.pattern})\Z')

    def __init__(self, option: data.DataOption):
        """
        Initializes ``Data``.

        Parameters:
            option: data option.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        if option is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, option)

        self.option: typing.Final[data.DataOption] = option

    def to_mcnp(self):
        """
        Generates INP from ``Data``.

        Returns:
            INP data card.
        """

        return _parser.postprocess_continuation_line(str(self.option))


@dataclasses.dataclass
class DataBuilder:
    """
    Builds ``Data``.

    Attributes:
        option: INP data option.
    """

    option: (
        str
        | data.DataOption
        | data.VolBuilder
        | data.AreaBuilder
        | data.TrBuilder_0
        | data.TrBuilder_1
        | data.TrBuilder_2
        | data.TrBuilder_3
        | data.TrBuilder_4
        | data.UBuilder
        | data.LatBuilder
        | data.FillBuilder
        | data.UranBuilder
        | data.DmBuilder
        | data.DawwgBuilder
        | data.EmbedBuilder
        | data.EmbeeBuilder
        | data.EmbebBuilder
        | data.EmbemBuilder
        | data.EmbtbBuilder
        | data.EmbtmBuilder
        | data.EmbdbBuilder
        | data.EmbdfBuilder
        | data.MBuilder_0
        | data.MBuilder_1
        | data.MtBuilder
        | data.MxBuilder
        | data.OtfdbBuilder
        | data.TotnuBuilder
        | data.NonuBuilder
        | data.AwtabBuilder
        | data.XsBuilder
        | data.VoidBuilder
        | data.MgoptBuilder
        | data.DrxsBuilder
        | data.ModeBuilder
        | data.PhysBuilder_0
        | data.PhysBuilder_1
        | data.PhysBuilder_2
        | data.PhysBuilder_3
        | data.PhysBuilder_4
        | data.ActBuilder
        | data.CutBuilder
        | data.ElptBuilder
        | data.ThtmeBuilder
        | data.MphysBuilder
        | data.LcaBuilder
        | data.LcbBuilder
        | data.LccBuilder
        | data.LeaBuilder
        | data.LebBuilder
        | data.FmultBuilder
        | data.TroptBuilder
        | data.UncBuilder
        | data.CosypBuilder
        | data.CosyBuilder
        | data.BfldBuilder
        | data.BflclBuilder
        | data.SdefBuilder
        | data.SiBuilder_0
        | data.SiBuilder_1
        | data.SpBuilder_0
        | data.SpBuilder_1
        | data.SbBuilder_0
        | data.SbBuilder_1
        | data.DsBuilder_0
        | data.DsBuilder_1
        | data.DsBuilder_2
        | data.ScBuilder
        | data.SswBuilder
        | data.SsrBuilder
        | data.KcodeBuilder
        | data.KsrcBuilder
        | data.KoptsBuilder
        | data.HsrcBuilder
        | data.FBuilder_0
        | data.FBuilder_1
        | data.FBuilder_2
        | data.FipBuilder
        | data.FirBuilder
        | data.FicBuilder
        | data.FBuilder_3
        | data.FcBuilder
        | data.EBuilder
        | data.TBuilder_0
        | data.TBuilder_1
        | data.CBuilder_0
        | data.CBuilder_1
        | data.FqBuilder
        | data.FmBuilder
        | data.DeBuilder
        | data.DfBuilder_0
        | data.DfBuilder_1
        | data.EmBuilder
        | data.TmBuilder
        | data.CmBuilder
        | data.CfBuilder
        | data.SfBuilder
        | data.FsBuilder
        | data.SdBuilder
        | data.FuBuilder
        | data.FtBuilder
        | data.NotrnBuilder
        | data.PertBuilder
        | data.KpertBuilder
        | data.KsenBuilder
        | data.FmeshBuilder
        | data.SpdtlBuilder
        | data.ImpBuilder
        | data.VarBuilder
        | data.WweBuilder
        | data.WwtBuilder
        | data.WwnBuilder
        | data.WwpBuilder
        | data.WwgBuilder
        | data.WwgeBuilder
        | data.WwgtBuilder
        | data.MeshBuilder
        | data.EspltBuilder
        | data.TspltBuilder
        | data.ExtBuilder
        | data.FclBuilder
        | data.DxtBuilder
        | data.DdBuilder
        | data.PdBuilder
        | data.DxcBuilder
        | data.BbremBuilder
        | data.PikmtBuilder
        | data.PwtBuilder
        | data.NpsBuilder
        | data.CtmeBuilder
        | data.StopBuilder
        | data.PrintBuilder
        | data.TalnpBuilder
        | data.PrdmpBuilder
        | data.PtracBuilder
        | data.HistpBuilder
        | data.RandBuilder
        | data.DbcnBuilder
        | data.LostBuilder
        | data.IdumBuilder
        | data.RdumBuilder
        | data.ZaBuilder
        | data.ZbBuilder
        | data.ZcBuilder
        | data.ZdBuilder
        | data.FilesBuilder
    )

    def build(self):
        """
        Builds ``DataBuilder`` into ``Data``.

        Returns:
            ``Data`` for ``DataBuilder``.
        """

        if isinstance(self.option, str):
            option = types.Data.from_mcnp(self.option)
        elif isinstance(self.option, data.DataOption):
            option = self.option
        else:
            option = self.option.build()

        return Data(option=option)

    @staticmethod
    def unbuild(ast: Data):
        """
        Unbuilds ``Data`` into ``DataBuilder``

        Returns:
            ``DataBuilder`` for ``Data``.
        """

        if isinstance(ast.option, data.Vol):
            option = data.VolBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Area):
            option = data.AreaBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Tr_0):
            option = data.TrBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.Tr_1):
            option = data.TrBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.Tr_2):
            option = data.TrBuilder_2.unbuild(ast.option)
        elif isinstance(ast.option, data.Tr_3):
            option = data.TrBuilder_3.unbuild(ast.option)
        elif isinstance(ast.option, data.Tr_4):
            option = data.TrBuilder_4.unbuild(ast.option)
        elif isinstance(ast.option, data.U):
            option = data.UBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Lat):
            option = data.LatBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Fill):
            option = data.FillBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Uran):
            option = data.UranBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Dm):
            option = data.DmBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Dawwg):
            option = data.DawwgBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Embed):
            option = data.EmbedBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Embee):
            option = data.EmbeeBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Embeb):
            option = data.EmbebBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Embem):
            option = data.EmbemBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Embtb):
            option = data.EmbtbBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Embtm):
            option = data.EmbtmBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Embdb):
            option = data.EmbdbBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Embdf):
            option = data.EmbdfBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.M_0):
            option = data.MBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.M_1):
            option = data.MBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.Mt):
            option = data.MtBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Mx):
            option = data.MxBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Otfdb):
            option = data.OtfdbBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Totnu):
            option = data.TotnuBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Nonu):
            option = data.NonuBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Awtab):
            option = data.AwtabBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Xs):
            option = data.XsBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Void):
            option = data.VoidBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Mgopt):
            option = data.MgoptBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Drxs):
            option = data.DrxsBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Mode):
            option = data.ModeBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Phys_0):
            option = data.PhysBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.Phys_1):
            option = data.PhysBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.Phys_2):
            option = data.PhysBuilder_2.unbuild(ast.option)
        elif isinstance(ast.option, data.Phys_3):
            option = data.PhysBuilder_3.unbuild(ast.option)
        elif isinstance(ast.option, data.Phys_4):
            option = data.PhysBuilder_4.unbuild(ast.option)
        elif isinstance(ast.option, data.Act):
            option = data.ActBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Cut):
            option = data.CutBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Elpt):
            option = data.ElptBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Thtme):
            option = data.ThtmeBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Mphys):
            option = data.MphysBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Lca):
            option = data.LcaBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Lcb):
            option = data.LcbBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Lcc):
            option = data.LccBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Lea):
            option = data.LeaBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Leb):
            option = data.LebBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Fmult):
            option = data.FmultBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Tropt):
            option = data.TroptBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Unc):
            option = data.UncBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Cosyp):
            option = data.CosypBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Cosy):
            option = data.CosyBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Bfld):
            option = data.BfldBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Bflcl):
            option = data.BflclBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Sdef):
            option = data.SdefBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Si_0):
            option = data.SiBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.Si_1):
            option = data.SiBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.Sp_0):
            option = data.SpBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.Sp_1):
            option = data.SpBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.Sb_0):
            option = data.SbBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.Sb_1):
            option = data.SbBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.Ds_0):
            option = data.DsBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.Ds_1):
            option = data.DsBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.Ds_2):
            option = data.DsBuilder_2.unbuild(ast.option)
        elif isinstance(ast.option, data.Sc):
            option = data.ScBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Ssw):
            option = data.SswBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Ssr):
            option = data.SsrBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Kcode):
            option = data.KcodeBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Ksrc):
            option = data.KsrcBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Kopts):
            option = data.KoptsBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Hsrc):
            option = data.HsrcBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.F_0):
            option = data.FBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.F_1):
            option = data.FBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.F_2):
            option = data.FBuilder_2.unbuild(ast.option)
        elif isinstance(ast.option, data.Fip):
            option = data.FipBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Fir):
            option = data.FirBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Fic):
            option = data.FicBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.F_3):
            option = data.FBuilder_3.unbuild(ast.option)
        elif isinstance(ast.option, data.Fc):
            option = data.FcBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.E):
            option = data.EBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.T_0):
            option = data.TBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.T_1):
            option = data.TBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.C_0):
            option = data.CBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.C_1):
            option = data.CBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.Fq):
            option = data.FqBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Fm):
            option = data.FmBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.De):
            option = data.DeBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Df_0):
            option = data.DfBuilder_0.unbuild(ast.option)
        elif isinstance(ast.option, data.Df_1):
            option = data.DfBuilder_1.unbuild(ast.option)
        elif isinstance(ast.option, data.Em):
            option = data.EmBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Tm):
            option = data.TmBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Cm):
            option = data.CmBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Cf):
            option = data.CfBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Sf):
            option = data.SfBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Fs):
            option = data.FsBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Sd):
            option = data.SdBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Fu):
            option = data.FuBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Ft):
            option = data.FtBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Notrn):
            option = data.NotrnBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Pert):
            option = data.PertBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Kpert):
            option = data.KpertBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Ksen):
            option = data.KsenBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Fmesh):
            option = data.FmeshBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Spdtl):
            option = data.SpdtlBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Imp):
            option = data.ImpBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Var):
            option = data.VarBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Wwe):
            option = data.WweBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Wwt):
            option = data.WwtBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Wwn):
            option = data.WwnBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Wwp):
            option = data.WwpBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Wwg):
            option = data.WwgBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Wwge):
            option = data.WwgeBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Wwgt):
            option = data.WwgtBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Mesh):
            option = data.MeshBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Esplt):
            option = data.EspltBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Tsplt):
            option = data.TspltBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Ext):
            option = data.ExtBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Fcl):
            option = data.FclBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Dxt):
            option = data.DxtBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Dd):
            option = data.DdBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Pd):
            option = data.PdBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Dxc):
            option = data.DxcBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Bbrem):
            option = data.BbremBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Pikmt):
            option = data.PikmtBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Pwt):
            option = data.PwtBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Nps):
            option = data.NpsBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Ctme):
            option = data.CtmeBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Stop):
            option = data.StopBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Print):
            option = data.PrintBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Talnp):
            option = data.TalnpBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Prdmp):
            option = data.PrdmpBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Ptrac):
            option = data.PtracBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Histp):
            option = data.HistpBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Rand):
            option = data.RandBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Dbcn):
            option = data.DbcnBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Lost):
            option = data.LostBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Idum):
            option = data.IdumBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Rdum):
            option = data.RdumBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Za):
            option = data.ZaBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Zb):
            option = data.ZbBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Zc):
            option = data.ZcBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Zd):
            option = data.ZdBuilder.unbuild(ast.option)
        elif isinstance(ast.option, data.Files):
            option = data.FilesBuilder.unbuild(ast.option)

        return DataBuilder(option=option)
