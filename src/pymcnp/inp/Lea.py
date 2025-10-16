import re

from . import _card
from .. import types
from .. import errors


class Lea(_card.Card):
    """
    Represents INP `lea` cards.
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
        rf'\Alea( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        ipht: str | int | types.Integer = None,
        icc: str | int | types.Integer = None,
        nobalc: str | int | types.Integer = None,
        nobale: str | int | types.Integer = None,
        ifbrk: str | int | types.Integer = None,
        ilvden: str | int | types.Integer = None,
        ievap: str | int | types.Integer = None,
        nofis: str | int | types.Integer = None,
    ):
        """
        Initializes `Lea`.

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
            InpError: SEMANTICS_CARD.
        """

        self.ipht: types.Integer = ipht
        self.icc: types.Integer = icc
        self.nobalc: types.Integer = nobalc
        self.nobale: types.Integer = nobale
        self.ifbrk: types.Integer = ifbrk
        self.ilvden: types.Integer = ilvden
        self.ievap: types.Integer = ievap
        self.nofis: types.Integer = nofis

    @property
    def ipht(self) -> types.Integer:
        """
        Generation of de-excitation photons setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ipht

    @ipht.setter
    def ipht(self, ipht: str | int | types.Integer) -> None:
        """
        Sets `ipht`.

        Parameters:
            ipht: Generation of de-excitation photons setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ipht is not None:
            if isinstance(ipht, types.Integer):
                ipht = ipht
            elif isinstance(ipht, int):
                ipht = types.Integer(ipht)
            elif isinstance(ipht, str):
                ipht = types.Integer.from_mcnp(ipht)

        if ipht is not None and not (isinstance(ipht.value, types.Jump) or ipht in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ipht)

        self._ipht: types.Integer = ipht

    @property
    def icc(self) -> types.Integer:
        """
        Level of physics for PHT physics setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._icc

    @icc.setter
    def icc(self, icc: str | int | types.Integer) -> None:
        """
        Sets `icc`.

        Parameters:
            icc: Level of physics for PHT physics setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if icc is not None:
            if isinstance(icc, types.Integer):
                icc = icc
            elif isinstance(icc, int):
                icc = types.Integer(icc)
            elif isinstance(icc, str):
                icc = types.Integer.from_mcnp(icc)

        if icc is not None and not (isinstance(icc.value, types.Jump) or icc in {0, 1, 2, 3, 4}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, icc)

        self._icc: types.Integer = icc

    @property
    def nobalc(self) -> types.Integer:
        """
        Mass-energy balancing in cascade setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nobalc

    @nobalc.setter
    def nobalc(self, nobalc: str | int | types.Integer) -> None:
        """
        Sets `nobalc`.

        Parameters:
            nobalc: Mass-energy balancing in cascade setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nobalc is not None:
            if isinstance(nobalc, types.Integer):
                nobalc = nobalc
            elif isinstance(nobalc, int):
                nobalc = types.Integer(nobalc)
            elif isinstance(nobalc, str):
                nobalc = types.Integer.from_mcnp(nobalc)

        if nobalc is not None and not (isinstance(nobalc.value, types.Jump) or nobalc in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, nobalc)

        self._nobalc: types.Integer = nobalc

    @property
    def nobale(self) -> types.Integer:
        """
        Mass-energy balancing in evaporation setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nobale

    @nobale.setter
    def nobale(self, nobale: str | int | types.Integer) -> None:
        """
        Sets `nobale`.

        Parameters:
            nobale: Mass-energy balancing in evaporation setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nobale is not None:
            if isinstance(nobale, types.Integer):
                nobale = nobale
            elif isinstance(nobale, int):
                nobale = types.Integer(nobale)
            elif isinstance(nobale, str):
                nobale = types.Integer.from_mcnp(nobale)

        if nobale is not None and not (isinstance(nobale.value, types.Jump) or nobale in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, nobale)

        self._nobale: types.Integer = nobale

    @property
    def ifbrk(self) -> types.Integer:
        """
        Mass-energy balancing in Fermi-breakup setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ifbrk

    @ifbrk.setter
    def ifbrk(self, ifbrk: str | int | types.Integer) -> None:
        """
        Sets `ifbrk`.

        Parameters:
            ifbrk: Mass-energy balancing in Fermi-breakup setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ifbrk is not None:
            if isinstance(ifbrk, types.Integer):
                ifbrk = ifbrk
            elif isinstance(ifbrk, int):
                ifbrk = types.Integer(ifbrk)
            elif isinstance(ifbrk, str):
                ifbrk = types.Integer.from_mcnp(ifbrk)

        if ifbrk is not None and not (isinstance(ifbrk.value, types.Jump) or ifbrk in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ifbrk)

        self._ifbrk: types.Integer = ifbrk

    @property
    def ilvden(self) -> types.Integer:
        """
        Level-density model setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ilvden

    @ilvden.setter
    def ilvden(self, ilvden: str | int | types.Integer) -> None:
        """
        Sets `ilvden`.

        Parameters:
            ilvden: Level-density model setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ilvden is not None:
            if isinstance(ilvden, types.Integer):
                ilvden = ilvden
            elif isinstance(ilvden, int):
                ilvden = types.Integer(ilvden)
            elif isinstance(ilvden, str):
                ilvden = types.Integer.from_mcnp(ilvden)

        if ilvden is not None and not (isinstance(ilvden.value, types.Jump) or ilvden in {0, 1, -1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ilvden)

        self._ilvden: types.Integer = ilvden

    @property
    def ievap(self) -> types.Integer:
        """
        Evaporation and fission model setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ievap

    @ievap.setter
    def ievap(self, ievap: str | int | types.Integer) -> None:
        """
        Sets `ievap`.

        Parameters:
            ievap: Evaporation and fission model setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ievap is not None:
            if isinstance(ievap, types.Integer):
                ievap = ievap
            elif isinstance(ievap, int):
                ievap = types.Integer(ievap)
            elif isinstance(ievap, str):
                ievap = types.Integer.from_mcnp(ievap)

        if ievap is not None and not (isinstance(ievap.value, types.Jump) or ievap in {0, 1, -1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ievap)

        self._ievap: types.Integer = ievap

    @property
    def nofis(self) -> types.Integer:
        """
        Fission setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nofis

    @nofis.setter
    def nofis(self, nofis: str | int | types.Integer) -> None:
        """
        Sets `nofis`.

        Parameters:
            nofis: Fission setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nofis is not None:
            if isinstance(nofis, types.Integer):
                nofis = nofis
            elif isinstance(nofis, int):
                nofis = types.Integer(nofis)
            elif isinstance(nofis, str):
                nofis = types.Integer.from_mcnp(nofis)

        if nofis is not None and not (isinstance(nofis.value, types.Jump) or nofis in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, nofis)

        self._nofis: types.Integer = nofis
