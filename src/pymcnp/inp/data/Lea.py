import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Lea(_option.DataOption):
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

    _KEYWORD = 'lea'

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
        rf'\Alea( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        ipht: types.Integer = None,
        icc: types.Integer = None,
        nobalc: types.Integer = None,
        nobale: types.Integer = None,
        ifbrk: types.Integer = None,
        ilvden: types.Integer = None,
        ievap: types.Integer = None,
        nofis: types.Integer = None,
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

        if ipht is not None and not (isinstance(ipht.value, types.Jump) or ipht in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ipht)
        if icc is not None and not (isinstance(icc.value, types.Jump) or icc in {0, 1, 2, 3, 4}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, icc)
        if nobalc is not None and not (isinstance(nobalc.value, types.Jump) or nobalc in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nobalc)
        if nobale is not None and not (isinstance(nobale.value, types.Jump) or nobale in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nobale)
        if ifbrk is not None and not (isinstance(ifbrk.value, types.Jump) or ifbrk in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ifbrk)
        if ilvden is not None and not (isinstance(ilvden.value, types.Jump) or ilvden in {0, 1, -1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ilvden)
        if ievap is not None and not (isinstance(ievap.value, types.Jump) or ievap in {0, 1, -1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ievap)
        if nofis is not None and not (isinstance(nofis.value, types.Jump) or nofis in {0, 1}):
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
class LeaBuilder(_option.DataOptionBuilder):
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

    ipht: str | int | types.Integer = None
    icc: str | int | types.Integer = None
    nobalc: str | int | types.Integer = None
    nobale: str | int | types.Integer = None
    ifbrk: str | int | types.Integer = None
    ilvden: str | int | types.Integer = None
    ievap: str | int | types.Integer = None
    nofis: str | int | types.Integer = None

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

    @staticmethod
    def unbuild(ast: Lea):
        """
        Unbuilds ``Lea`` into ``LeaBuilder``

        Returns:
            ``LeaBuilder`` for ``Lea``.
        """

        return LeaBuilder(
            ipht=copy.deepcopy(ast.ipht),
            icc=copy.deepcopy(ast.icc),
            nobalc=copy.deepcopy(ast.nobalc),
            nobale=copy.deepcopy(ast.nobale),
            ifbrk=copy.deepcopy(ast.ifbrk),
            ilvden=copy.deepcopy(ast.ilvden),
            ievap=copy.deepcopy(ast.ievap),
            nofis=copy.deepcopy(ast.nofis),
        )
