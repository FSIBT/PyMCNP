import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Lea(DataOption):
    """
    Represents INP lea elements.

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
            InpError: SEMANTICS_OPTION.
        """

        if ipht is None or ipht.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ipht)
        if icc is None or icc.value not in {0, 1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, icc)
        if nobalc is None or nobalc.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nobalc)
        if nobale is None or nobale.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nobale)
        if ifbrk is None or ifbrk.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ifbrk)
        if ilvden is None or ilvden.value not in {0, 1, -1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ilvden)
        if ievap is None or ievap.value not in {0, 1, -1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ievap)
        if nofis is None or nofis.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nofis)

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


@dataclasses.dataclass
class LeaBuilder:
    """
    Builds ``Lea``.

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

    ipht: str | int | types.IntegerOrJump
    icc: str | int | types.IntegerOrJump
    nobalc: str | int | types.IntegerOrJump
    nobale: str | int | types.IntegerOrJump
    ifbrk: str | int | types.IntegerOrJump
    ilvden: str | int | types.IntegerOrJump
    ievap: str | int | types.IntegerOrJump
    nofis: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``LeaBuilder`` into ``Lea``.

        Returns:
            ``Lea`` for ``LeaBuilder``.
        """

        ipht = self.ipht
        if isinstance(self.ipht, types.Integer):
            ipht = self.ipht
        elif isinstance(self.ipht, int):
            ipht = types.IntegerOrJump(self.ipht)
        elif isinstance(self.ipht, str):
            ipht = types.IntegerOrJump.from_mcnp(self.ipht)

        icc = self.icc
        if isinstance(self.icc, types.Integer):
            icc = self.icc
        elif isinstance(self.icc, int):
            icc = types.IntegerOrJump(self.icc)
        elif isinstance(self.icc, str):
            icc = types.IntegerOrJump.from_mcnp(self.icc)

        nobalc = self.nobalc
        if isinstance(self.nobalc, types.Integer):
            nobalc = self.nobalc
        elif isinstance(self.nobalc, int):
            nobalc = types.IntegerOrJump(self.nobalc)
        elif isinstance(self.nobalc, str):
            nobalc = types.IntegerOrJump.from_mcnp(self.nobalc)

        nobale = self.nobale
        if isinstance(self.nobale, types.Integer):
            nobale = self.nobale
        elif isinstance(self.nobale, int):
            nobale = types.IntegerOrJump(self.nobale)
        elif isinstance(self.nobale, str):
            nobale = types.IntegerOrJump.from_mcnp(self.nobale)

        ifbrk = self.ifbrk
        if isinstance(self.ifbrk, types.Integer):
            ifbrk = self.ifbrk
        elif isinstance(self.ifbrk, int):
            ifbrk = types.IntegerOrJump(self.ifbrk)
        elif isinstance(self.ifbrk, str):
            ifbrk = types.IntegerOrJump.from_mcnp(self.ifbrk)

        ilvden = self.ilvden
        if isinstance(self.ilvden, types.Integer):
            ilvden = self.ilvden
        elif isinstance(self.ilvden, int):
            ilvden = types.IntegerOrJump(self.ilvden)
        elif isinstance(self.ilvden, str):
            ilvden = types.IntegerOrJump.from_mcnp(self.ilvden)

        ievap = self.ievap
        if isinstance(self.ievap, types.Integer):
            ievap = self.ievap
        elif isinstance(self.ievap, int):
            ievap = types.IntegerOrJump(self.ievap)
        elif isinstance(self.ievap, str):
            ievap = types.IntegerOrJump.from_mcnp(self.ievap)

        nofis = self.nofis
        if isinstance(self.nofis, types.Integer):
            nofis = self.nofis
        elif isinstance(self.nofis, int):
            nofis = types.IntegerOrJump(self.nofis)
        elif isinstance(self.nofis, str):
            nofis = types.IntegerOrJump.from_mcnp(self.nofis)

        return Lea(
            ipht=ipht,
            icc=icc,
            nobalc=nobalc,
            nobale=nobale,
            ifbrk=ifbrk,
            ilvden=ilvden,
            ievap=ievap,
            nofis=nofis,
        )
