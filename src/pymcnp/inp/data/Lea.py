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
        rf'\Alea( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})( {types.Integer._REGEX.pattern})\Z'
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

        self.ipht: typing.Final[types.Integer] = ipht
        self.icc: typing.Final[types.Integer] = icc
        self.nobalc: typing.Final[types.Integer] = nobalc
        self.nobale: typing.Final[types.Integer] = nobale
        self.ifbrk: typing.Final[types.Integer] = ifbrk
        self.ilvden: typing.Final[types.Integer] = ilvden
        self.ievap: typing.Final[types.Integer] = ievap
        self.nofis: typing.Final[types.Integer] = nofis


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

    ipht: str | int | types.Integer
    icc: str | int | types.Integer
    nobalc: str | int | types.Integer
    nobale: str | int | types.Integer
    ifbrk: str | int | types.Integer
    ilvden: str | int | types.Integer
    ievap: str | int | types.Integer
    nofis: str | int | types.Integer

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
            ipht = types.Integer(self.ipht)
        elif isinstance(self.ipht, str):
            ipht = types.Integer.from_mcnp(self.ipht)

        icc = self.icc
        if isinstance(self.icc, types.Integer):
            icc = self.icc
        elif isinstance(self.icc, int):
            icc = types.Integer(self.icc)
        elif isinstance(self.icc, str):
            icc = types.Integer.from_mcnp(self.icc)

        nobalc = self.nobalc
        if isinstance(self.nobalc, types.Integer):
            nobalc = self.nobalc
        elif isinstance(self.nobalc, int):
            nobalc = types.Integer(self.nobalc)
        elif isinstance(self.nobalc, str):
            nobalc = types.Integer.from_mcnp(self.nobalc)

        nobale = self.nobale
        if isinstance(self.nobale, types.Integer):
            nobale = self.nobale
        elif isinstance(self.nobale, int):
            nobale = types.Integer(self.nobale)
        elif isinstance(self.nobale, str):
            nobale = types.Integer.from_mcnp(self.nobale)

        ifbrk = self.ifbrk
        if isinstance(self.ifbrk, types.Integer):
            ifbrk = self.ifbrk
        elif isinstance(self.ifbrk, int):
            ifbrk = types.Integer(self.ifbrk)
        elif isinstance(self.ifbrk, str):
            ifbrk = types.Integer.from_mcnp(self.ifbrk)

        ilvden = self.ilvden
        if isinstance(self.ilvden, types.Integer):
            ilvden = self.ilvden
        elif isinstance(self.ilvden, int):
            ilvden = types.Integer(self.ilvden)
        elif isinstance(self.ilvden, str):
            ilvden = types.Integer.from_mcnp(self.ilvden)

        ievap = self.ievap
        if isinstance(self.ievap, types.Integer):
            ievap = self.ievap
        elif isinstance(self.ievap, int):
            ievap = types.Integer(self.ievap)
        elif isinstance(self.ievap, str):
            ievap = types.Integer.from_mcnp(self.ievap)

        nofis = self.nofis
        if isinstance(self.nofis, types.Integer):
            nofis = self.nofis
        elif isinstance(self.nofis, int):
            nofis = types.Integer(self.nofis)
        elif isinstance(self.nofis, str):
            nofis = types.Integer.from_mcnp(self.nofis)

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
