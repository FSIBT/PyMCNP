import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Lea(_option.DataOption_, keyword='lea'):
    """
    Represents INP data card lea options.

    Attributes:
        ipht: Generation of de-excitation photons setting.
        icc: Level of physics for PHT physics setting.
        nobalc: Mass-energy balancing in cascade setting.
        nobale: Mass-energy balancing in evaporation setting.
        ifbrk: Mass-energy balancing in Fermi-breakup setting.
        ilvden: Level-density model setting.
        ievap: Evaporation and fission model setting.
        nofis: Fission setting.
    """

    _REGEX = re.compile(r'\Alea( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        ipht: types.Integer,
        icc: types.Integer,
        nobalc: types.Integer,
        nobale: types.Integer,
        ifbrk: types.Integer,
        ilvden: types.Integer,
        ievap: types.Integer,
        nofis: types.Integer,
    ):
        """
        Initializes ``DataOption_Lea``.

        Parameters:
            ipht: Generation of de-excitation photons setting.
            icc: Level of physics for PHT physics setting.
            nobalc: Mass-energy balancing in cascade setting.
            nobale: Mass-energy balancing in evaporation setting.
            ifbrk: Mass-energy balancing in Fermi-breakup setting.
            ilvden: Level-density model setting.
            ievap: Evaporation and fission model setting.
            nofis: Fission setting.

        Returns:
            ``DataOption_Lea``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if ipht is None or ipht.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ipht)
        if icc is None or icc.value not in {0, 1, 2, 3, 4}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, icc)
        if nobalc is None or nobalc.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, nobalc)
        if nobale is None or nobale.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, nobale)
        if ifbrk is None or ifbrk.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ifbrk)
        if ilvden is None or ilvden.value not in {0, 1, -1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ilvden)
        if ievap is None or ievap.value not in {0, 1, -1, 2}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, ievap)
        if nofis is None or nofis.value not in {0, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, nofis)

        self.value: typing.Final[tuple[any]] = types._Tuple(
            [ipht, icc, nobalc, nobale, ifbrk, ilvden, ievap, nofis]
        )
        self.ipht: typing.Final[types.Integer] = ipht
        self.icc: typing.Final[types.Integer] = icc
        self.nobalc: typing.Final[types.Integer] = nobalc
        self.nobale: typing.Final[types.Integer] = nobale
        self.ifbrk: typing.Final[types.Integer] = ifbrk
        self.ilvden: typing.Final[types.Integer] = ilvden
        self.ievap: typing.Final[types.Integer] = ievap
        self.nofis: typing.Final[types.Integer] = nofis

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Lea`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Lea``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Lea._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        ipht = types.Integer.from_mcnp(tokens[1])
        icc = types.Integer.from_mcnp(tokens[2])
        nobalc = types.Integer.from_mcnp(tokens[3])
        nobale = types.Integer.from_mcnp(tokens[4])
        ifbrk = types.Integer.from_mcnp(tokens[5])
        ilvden = types.Integer.from_mcnp(tokens[6])
        ievap = types.Integer.from_mcnp(tokens[7])
        nofis = types.Integer.from_mcnp(tokens[8])

        return DataOption_Lea(ipht, icc, nobalc, nobale, ifbrk, ilvden, ievap, nofis)
