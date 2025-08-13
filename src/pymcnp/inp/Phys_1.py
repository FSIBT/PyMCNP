import re

from . import _card
from .. import types
from .. import errors


class Phys_1(_card.Card):
    """
    Represents INP `phys` elements variation #1.
    """

    _KEYWORD = 'phys:p'

    _ATTRS = {
        'emcpf': types.Real,
        'ides': types.Integer,
        'nocoh': types.Integer,
        'ispn': types.Integer,
        'nodop': types.Integer,
        'fism': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Aphys:p( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        emcpf: str | int | float | types.Real = None,
        ides: str | int | types.Integer = None,
        nocoh: str | int | types.Integer = None,
        ispn: str | int | types.Integer = None,
        nodop: str | int | types.Integer = None,
        fism: str | int | types.Integer = None,
    ):
        """
        Initializes `Phys_1`.

        Parameters:
            emcpf: Upper energy limit for photon treatment.
            ides: Generation of elections by photon controls.
            nocoh: Coherent Thomson scattering controls.
            ispn: Photonuclear particle production controls.
            nodop: Photon Doppler energy broadening controls.
            fism: Selection of photofission method controls.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.emcpf: types.Real = emcpf
        self.ides: types.Integer = ides
        self.nocoh: types.Integer = nocoh
        self.ispn: types.Integer = ispn
        self.nodop: types.Integer = nodop
        self.fism: types.Integer = fism

    @property
    def emcpf(self) -> types.Real:
        """
        Upper energy limit for photon treatment

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._emcpf

    @emcpf.setter
    def emcpf(self, emcpf: str | int | float | types.Real) -> None:
        """
        Sets `emcpf`.

        Parameters:
            emcpf: Upper energy limit for photon treatment.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if emcpf is not None:
            if isinstance(emcpf, types.Real):
                emcpf = emcpf
            elif isinstance(emcpf, int) or isinstance(emcpf, float):
                emcpf = types.Real(emcpf)
            elif isinstance(emcpf, str):
                emcpf = types.Real.from_mcnp(emcpf)

        self._emcpf: types.Real = emcpf

    @property
    def ides(self) -> types.Integer:
        """
        Generation of elections by photon controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ides

    @ides.setter
    def ides(self, ides: str | int | types.Integer) -> None:
        """
        Sets `ides`.

        Parameters:
            ides: Generation of elections by photon controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ides is not None:
            if isinstance(ides, types.Integer):
                ides = ides
            elif isinstance(ides, int):
                ides = types.Integer(ides)
            elif isinstance(ides, str):
                ides = types.Integer.from_mcnp(ides)

        if ides is not None and not (isinstance(ides.value, types.Jump) or ides in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ides)

        self._ides: types.Integer = ides

    @property
    def nocoh(self) -> types.Integer:
        """
        Coherent Thomson scattering controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nocoh

    @nocoh.setter
    def nocoh(self, nocoh: str | int | types.Integer) -> None:
        """
        Sets `nocoh`.

        Parameters:
            nocoh: Coherent Thomson scattering controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nocoh is not None:
            if isinstance(nocoh, types.Integer):
                nocoh = nocoh
            elif isinstance(nocoh, int):
                nocoh = types.Integer(nocoh)
            elif isinstance(nocoh, str):
                nocoh = types.Integer.from_mcnp(nocoh)

        if nocoh is not None and not (isinstance(nocoh.value, types.Jump) or nocoh in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, nocoh)

        self._nocoh: types.Integer = nocoh

    @property
    def ispn(self) -> types.Integer:
        """
        Photonuclear particle production controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ispn

    @ispn.setter
    def ispn(self, ispn: str | int | types.Integer) -> None:
        """
        Sets `ispn`.

        Parameters:
            ispn: Photonuclear particle production controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ispn is not None:
            if isinstance(ispn, types.Integer):
                ispn = ispn
            elif isinstance(ispn, int):
                ispn = types.Integer(ispn)
            elif isinstance(ispn, str):
                ispn = types.Integer.from_mcnp(ispn)

        if ispn is not None and not (isinstance(ispn.value, types.Jump) or ispn in {-1, 0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, ispn)

        self._ispn: types.Integer = ispn

    @property
    def nodop(self) -> types.Integer:
        """
        Photon Doppler energy broadening controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._nodop

    @nodop.setter
    def nodop(self, nodop: str | int | types.Integer) -> None:
        """
        Sets `nodop`.

        Parameters:
            nodop: Photon Doppler energy broadening controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if nodop is not None:
            if isinstance(nodop, types.Integer):
                nodop = nodop
            elif isinstance(nodop, int):
                nodop = types.Integer(nodop)
            elif isinstance(nodop, str):
                nodop = types.Integer.from_mcnp(nodop)

        if nodop is not None and not (isinstance(nodop.value, types.Jump) or nodop in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, nodop)

        self._nodop: types.Integer = nodop

    @property
    def fism(self) -> types.Integer:
        """
        Selection of photofission method controls

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._fism

    @fism.setter
    def fism(self, fism: str | int | types.Integer) -> None:
        """
        Sets `fism`.

        Parameters:
            fism: Selection of photofission method controls.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if fism is not None:
            if isinstance(fism, types.Integer):
                fism = fism
            elif isinstance(fism, int):
                fism = types.Integer(fism)
            elif isinstance(fism, str):
                fism = types.Integer.from_mcnp(fism)

        self._fism: types.Integer = fism
