import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Lea(DataOption_, keyword='lea'):
    """
    Represents INP lea elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'ipht': types.Integer,
        'icc': types.Integer,
        'nobalc': types.Integer,
        'nobale': types.Integer,
        'ifbrk': types.Integer,
        'ilvden': types.Integer,
        'ievap': types.Integer,
        'nofis': types.Integer,
    }

    _REGEX = re.compile(
        rf'lea( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})'
    )

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
        Initializes ``Lea``.

        Parameters:
            ipht: Generation of de-excitation photons setting.
            icc: Level of physics for PHT physics setting.
            nobalc: Mass-energy balancing in cascade setting.
            nobale: Mass-energy balancing in evaporation setting.
            ifbrk: Mass-energy balancing in Fermi-breakup setting.
            ilvden: Level-density model setting.
            ievap: Evaporation and fission model setting.
            nofis: Fission setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if ipht is None or ipht.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ipht)
        if icc is None or icc.value not in {0, 1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, icc)
        if nobalc is None or nobalc.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nobalc)
        if nobale is None or nobale.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nobale)
        if ifbrk is None or ifbrk.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ifbrk)
        if ilvden is None or ilvden.value not in {0, 1, -1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ilvden)
        if ievap is None or ievap.value not in {0, 1, -1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ievap)
        if nofis is None or nofis.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nofis)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ipht,
                icc,
                nobalc,
                nobale,
                ifbrk,
                ilvden,
                ievap,
                nofis,
            ]
        )

        self.ipht: typing.Final[types.Integer] = ipht
        self.icc: typing.Final[types.Integer] = icc
        self.nobalc: typing.Final[types.Integer] = nobalc
        self.nobale: typing.Final[types.Integer] = nobale
        self.ifbrk: typing.Final[types.Integer] = ifbrk
        self.ilvden: typing.Final[types.Integer] = ilvden
        self.ievap: typing.Final[types.Integer] = ievap
        self.nofis: typing.Final[types.Integer] = nofis
