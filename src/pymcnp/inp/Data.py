import re
import typing

from . import data
from ._card import Card
from ..utils import errors
from ..utils import _parser


class Data(Card):
    """
    Represents INP data elements.

    Attributes:
        option: data option.
    """

    _ATTRS = {'option': data.DataOption}

    _REGEX = re.compile(rf'\A({data.DataOption._REGEX.pattern[2:-2]})\Z')

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

        source = f'{self.option}'
        source, comments = _parser.preprocess_inp(source)
        source = _parser.postprocess_inp(source)

        return source


'''
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
        | data.CBuilder
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
        | data.TfBuilder_0
        | data.TfBuilder_1
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

        option = self.option
        if isinstance(self.option, data.DataOption):
            option = self.option
        elif isinstance(self.option, str):
            option = data.DataOption.from_mcnp(self.option)
        elif isinstance(self.option, data.DataOptionBuilder):
            option = self.option.build()

        return Data(option=option)

    @staticmethod
    def unbuild(ast: Data):
        """
        Unbuilds ``Data`` into ``DataBuilder``

        Returns:
            ``DataBuilder`` for ``Data``.
        """

        return DataBuilder(option=copy.deepcopy(ast.option))
'''
