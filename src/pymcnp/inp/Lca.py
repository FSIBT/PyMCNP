import re

from . import _card
from .. import types
from .. import errors


class Lca(_card.Card):
    """
    Represents INP `lca` cards.
    """

    _KEYWORD = 'lca'

    _ATTRS = {
        'ielas': types.Integer,
        'ipreg': types.Integer,
        'iexisa': types.Integer,
        'ichoic': types.Integer,
        'jcoul': types.Integer,
        'nexite': types.Integer,
        'npidk': types.Integer,
        'noact': types.Integer,
        'icem': types.Integer,
        'ilaq': types.Integer,
        'nevtype': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Alca( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        ielas: str | int | types.Integer = None,
        ipreg: str | int | types.Integer = None,
        iexisa: str | int | types.Integer = None,
        ichoic: str | int | types.Integer = None,
        jcoul: str | int | types.Integer = None,
        nexite: str | int | types.Integer = None,
        npidk: str | int | types.Integer = None,
        noact: str | int | types.Integer = None,
        icem: str | int | types.Integer = None,
        ilaq: str | int | types.Integer = None,
        nevtype: str | int | types.Integer = None,
    ):
        """
        Initializes `Lca`.

        Parameters:
            ielas: Elastic scattering controls.
            ipreg: pre-equilibrium model.
            iexisa: Model choice controls.
            ichoic: ISABEL intranuclear cascade model control.
            jcoul: Coulomb barrier for incident charged particle controls.
            nexite: Subtract nuclear recoil energy to get excitation energy.
            npidk: Cutoff interact/terminate control.
            noact: Particle transport settings.
            icem: Choose alternative physics model.
            ilaq: Choose light ion and nucleon physics modules.
            nevtype: Choose number of evaporation particles for GEM2.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.ielas: types.Integer = ielas
        self.ipreg: types.Integer = ipreg
        self.iexisa: types.Integer = iexisa
        self.ichoic: types.Integer = ichoic
        self.jcoul: types.Integer = jcoul
        self.nexite: types.Integer = nexite
        self.npidk: types.Integer = npidk
        self.noact: types.Integer = noact
        self.icem: types.Integer = icem
        self.ilaq: types.Integer = ilaq
        self.nevtype: types.Integer = nevtype

    @property
    def ielas(self) -> types.Integer:
        """
        Elastic scattering controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ielas

    @ielas.setter
    def ielas(self, ielas: str | int | types.Integer) -> None:
        """
        Sets `ielas`.

        Parameters:
            ielas: Elastic scattering controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ielas is not None:
            if isinstance(ielas, types.Integer):
                ielas = ielas
            elif isinstance(ielas, int):
                ielas = types.Integer(ielas)
            elif isinstance(ielas, str):
                ielas = types.Integer.from_mcnp(ielas)

        if ielas is not None and not (isinstance(ielas.value, types.Jump) or ielas == 0 or ielas == 1 or ielas == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ielas)

        self._ielas: types.Integer = ielas

    @property
    def ipreg(self) -> types.Integer:
        """
        Pre-equilibrium model

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ipreg

    @ipreg.setter
    def ipreg(self, ipreg: str | int | types.Integer) -> None:
        """
        Sets `ipreg`.

        Parameters:
            ipreg: pre-equilibrium model.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ipreg is not None:
            if isinstance(ipreg, types.Integer):
                ipreg = ipreg
            elif isinstance(ipreg, int):
                ipreg = types.Integer(ipreg)
            elif isinstance(ipreg, str):
                ipreg = types.Integer.from_mcnp(ipreg)

        if ipreg is not None and not (isinstance(ipreg.value, types.Jump) or ipreg == 0 or ipreg == 1 or ipreg == 2 or ipreg == 3):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ipreg)

        self._ipreg: types.Integer = ipreg

    @property
    def iexisa(self) -> types.Integer:
        """
        Model choice controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._iexisa

    @iexisa.setter
    def iexisa(self, iexisa: str | int | types.Integer) -> None:
        """
        Sets `iexisa`.

        Parameters:
            iexisa: Model choice controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if iexisa is not None:
            if isinstance(iexisa, types.Integer):
                iexisa = iexisa
            elif isinstance(iexisa, int):
                iexisa = types.Integer(iexisa)
            elif isinstance(iexisa, str):
                iexisa = types.Integer.from_mcnp(iexisa)

        if iexisa is not None and not (isinstance(iexisa.value, types.Jump) or iexisa == 0 or iexisa == 1 or iexisa == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, iexisa)

        self._iexisa: types.Integer = iexisa

    @property
    def ichoic(self) -> types.Integer:
        """
        ISABEL intranuclear cascade model control

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ichoic

    @ichoic.setter
    def ichoic(self, ichoic: str | int | types.Integer) -> None:
        """
        Sets `ichoic`.

        Parameters:
            ichoic: ISABEL intranuclear cascade model control.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ichoic is not None:
            if isinstance(ichoic, types.Integer):
                ichoic = ichoic
            elif isinstance(ichoic, int):
                ichoic = types.Integer(ichoic)
            elif isinstance(ichoic, str):
                ichoic = types.Integer.from_mcnp(ichoic)

        self._ichoic: types.Integer = ichoic

    @property
    def jcoul(self) -> types.Integer:
        """
        Coulomb barrier for incident charged particle controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._jcoul

    @jcoul.setter
    def jcoul(self, jcoul: str | int | types.Integer) -> None:
        """
        Sets `jcoul`.

        Parameters:
            jcoul: Coulomb barrier for incident charged particle controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if jcoul is not None:
            if isinstance(jcoul, types.Integer):
                jcoul = jcoul
            elif isinstance(jcoul, int):
                jcoul = types.Integer(jcoul)
            elif isinstance(jcoul, str):
                jcoul = types.Integer.from_mcnp(jcoul)

        if jcoul is not None and not (isinstance(jcoul.value, types.Jump) or jcoul == 0 or jcoul == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, jcoul)

        self._jcoul: types.Integer = jcoul

    @property
    def nexite(self) -> types.Integer:
        """
        Subtract nuclear recoil energy to get excitation energy

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nexite

    @nexite.setter
    def nexite(self, nexite: str | int | types.Integer) -> None:
        """
        Sets `nexite`.

        Parameters:
            nexite: Subtract nuclear recoil energy to get excitation energy.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nexite is not None:
            if isinstance(nexite, types.Integer):
                nexite = nexite
            elif isinstance(nexite, int):
                nexite = types.Integer(nexite)
            elif isinstance(nexite, str):
                nexite = types.Integer.from_mcnp(nexite)

        if nexite is not None and not (isinstance(nexite.value, types.Jump) or nexite == 0 or nexite == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, nexite)

        self._nexite: types.Integer = nexite

    @property
    def npidk(self) -> types.Integer:
        """
        Cutoff interact/terminate control

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._npidk

    @npidk.setter
    def npidk(self, npidk: str | int | types.Integer) -> None:
        """
        Sets `npidk`.

        Parameters:
            npidk: Cutoff interact/terminate control.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if npidk is not None:
            if isinstance(npidk, types.Integer):
                npidk = npidk
            elif isinstance(npidk, int):
                npidk = types.Integer(npidk)
            elif isinstance(npidk, str):
                npidk = types.Integer.from_mcnp(npidk)

        if npidk is not None and not (isinstance(npidk.value, types.Jump) or npidk == 0 or npidk == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, npidk)

        self._npidk: types.Integer = npidk

    @property
    def noact(self) -> types.Integer:
        """
        Particle transport settings

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._noact

    @noact.setter
    def noact(self, noact: str | int | types.Integer) -> None:
        """
        Sets `noact`.

        Parameters:
            noact: Particle transport settings.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if noact is not None:
            if isinstance(noact, types.Integer):
                noact = noact
            elif isinstance(noact, int):
                noact = types.Integer(noact)
            elif isinstance(noact, str):
                noact = types.Integer.from_mcnp(noact)

        if noact is not None and not (isinstance(noact.value, types.Jump) or noact == -2 or noact == -1 or noact == 0 or noact == 1 or noact == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, noact)

        self._noact: types.Integer = noact

    @property
    def icem(self) -> types.Integer:
        """
        Choose alternative physics model

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._icem

    @icem.setter
    def icem(self, icem: str | int | types.Integer) -> None:
        """
        Sets `icem`.

        Parameters:
            icem: Choose alternative physics model.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if icem is not None:
            if isinstance(icem, types.Integer):
                icem = icem
            elif isinstance(icem, int):
                icem = types.Integer(icem)
            elif isinstance(icem, str):
                icem = types.Integer.from_mcnp(icem)

        if icem is not None and not (isinstance(icem.value, types.Jump) or icem == 0 or icem == 1 or icem == 2):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, icem)

        self._icem: types.Integer = icem

    @property
    def ilaq(self) -> types.Integer:
        """
        Choose light ion and nucleon physics modules

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ilaq

    @ilaq.setter
    def ilaq(self, ilaq: str | int | types.Integer) -> None:
        """
        Sets `ilaq`.

        Parameters:
            ilaq: Choose light ion and nucleon physics modules.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ilaq is not None:
            if isinstance(ilaq, types.Integer):
                ilaq = ilaq
            elif isinstance(ilaq, int):
                ilaq = types.Integer(ilaq)
            elif isinstance(ilaq, str):
                ilaq = types.Integer.from_mcnp(ilaq)

        if ilaq is not None and not (isinstance(ilaq.value, types.Jump) or ilaq == 0 or ilaq == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ilaq)

        self._ilaq: types.Integer = ilaq

    @property
    def nevtype(self) -> types.Integer:
        """
        Choose number of evaporation particles for GEM2

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nevtype

    @nevtype.setter
    def nevtype(self, nevtype: str | int | types.Integer) -> None:
        """
        Sets `nevtype`.

        Parameters:
            nevtype: Choose number of evaporation particles for GEM2.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nevtype is not None:
            if isinstance(nevtype, types.Integer):
                nevtype = nevtype
            elif isinstance(nevtype, int):
                nevtype = types.Integer(nevtype)
            elif isinstance(nevtype, str):
                nevtype = types.Integer.from_mcnp(nevtype)

        self._nevtype: types.Integer = nevtype
