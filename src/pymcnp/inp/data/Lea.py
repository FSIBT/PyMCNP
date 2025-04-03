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
        'ipht': types.IntegerOrJump,
        'icc': types.IntegerOrJump,
        'nobalc': types.IntegerOrJump,
        'nobale': types.IntegerOrJump,
        'ifbrk': types.IntegerOrJump,
        'ilvden': types.IntegerOrJump,
        'ievap': types.IntegerOrJump,
        'nofis': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Alea( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        ipht: types.IntegerOrJump,
        icc: types.IntegerOrJump,
        nobalc: types.IntegerOrJump,
        nobale: types.IntegerOrJump,
        ifbrk: types.IntegerOrJump,
        ilvden: types.IntegerOrJump,
        ievap: types.IntegerOrJump,
        nofis: types.IntegerOrJump,
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

        self.ipht: typing.Final[types.IntegerOrJump] = ipht
        self.icc: typing.Final[types.IntegerOrJump] = icc
        self.nobalc: typing.Final[types.IntegerOrJump] = nobalc
        self.nobale: typing.Final[types.IntegerOrJump] = nobale
        self.ifbrk: typing.Final[types.IntegerOrJump] = ifbrk
        self.ilvden: typing.Final[types.IntegerOrJump] = ilvden
        self.ievap: typing.Final[types.IntegerOrJump] = ievap
        self.nofis: typing.Final[types.IntegerOrJump] = nofis
