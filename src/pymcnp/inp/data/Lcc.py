import re

from . import _option
from ...utils import types
from ...utils import errors


class Lcc(_option.DataOption):
    """
    Represents INP lcc elements.

    Attributes:
        stincl: Rescaling factor of the cascade duration.
        v0incl: Potential depth.
        xfoisaincl: Maximum impact parameter for Pauli blocking.
        npaulincl: Pauli blocking parameter setting.
        nosurfincl: Difuse nuclear surface based on Wood-Saxon density setting.
        ecutincl: Bertini model energy below this energy.
        ebankincl: INCL bank particles below this energy.
        ebankabia: ABLA bank particles below this energy.
    """

    _KEYWORD = 'lcc'

    _ATTRS = {
        'stincl': types.Real,
        'v0incl': types.Real,
        'xfoisaincl': types.Real,
        'npaulincl': types.Integer,
        'nosurfincl': types.Integer,
        'ecutincl': types.Real,
        'ebankincl': types.Real,
        'ebankabia': types.Real,
    }

    _REGEX = re.compile(
        rf'\Alcc( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        stincl: str | int | float | types.Real = None,
        v0incl: str | int | float | types.Real = None,
        xfoisaincl: str | int | float | types.Real = None,
        npaulincl: str | int | types.Integer = None,
        nosurfincl: str | int | types.Integer = None,
        ecutincl: str | int | float | types.Real = None,
        ebankincl: str | int | float | types.Real = None,
        ebankabia: str | int | float | types.Real = None,
    ):
        """
        Initializes ``Lcc``.

        Parameters:
            stincl: Rescaling factor of the cascade duration.
            v0incl: Potential depth.
            xfoisaincl: Maximum impact parameter for Pauli blocking.
            npaulincl: Pauli blocking parameter setting.
            nosurfincl: Difuse nuclear surface based on Wood-Saxon density setting.
            ecutincl: Bertini model energy below this energy.
            ebankincl: INCL bank particles below this energy.
            ebankabia: ABLA bank particles below this energy.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.stincl: types.Real = stincl
        self.v0incl: types.Real = v0incl
        self.xfoisaincl: types.Real = xfoisaincl
        self.npaulincl: types.Integer = npaulincl
        self.nosurfincl: types.Integer = nosurfincl
        self.ecutincl: types.Real = ecutincl
        self.ebankincl: types.Real = ebankincl
        self.ebankabia: types.Real = ebankabia

    @property
    def stincl(self) -> types.Real:
        """
        Gets ``stincl``.

        Returns:
            ``stincl``.
        """

        return self._stincl

    @stincl.setter
    def stincl(self, stincl: str | int | float | types.Real) -> None:
        """
        Sets ``stincl``.

        Parameters:
            stincl: Rescaling factor of the cascade duration.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if stincl is not None:
            if isinstance(stincl, types.Real):
                stincl = stincl
            elif isinstance(stincl, int):
                stincl = types.Real(stincl)
            elif isinstance(stincl, float):
                stincl = types.Real(stincl)
            elif isinstance(stincl, str):
                stincl = types.Real.from_mcnp(stincl)
            else:
                raise TypeError

        self._stincl: types.Real = stincl

    @property
    def v0incl(self) -> types.Real:
        """
        Gets ``v0incl``.

        Returns:
            ``v0incl``.
        """

        return self._v0incl

    @v0incl.setter
    def v0incl(self, v0incl: str | int | float | types.Real) -> None:
        """
        Sets ``v0incl``.

        Parameters:
            v0incl: Potential depth.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v0incl is not None:
            if isinstance(v0incl, types.Real):
                v0incl = v0incl
            elif isinstance(v0incl, int):
                v0incl = types.Real(v0incl)
            elif isinstance(v0incl, float):
                v0incl = types.Real(v0incl)
            elif isinstance(v0incl, str):
                v0incl = types.Real.from_mcnp(v0incl)
            else:
                raise TypeError

        self._v0incl: types.Real = v0incl

    @property
    def xfoisaincl(self) -> types.Real:
        """
        Gets ``xfoisaincl``.

        Returns:
            ``xfoisaincl``.
        """

        return self._xfoisaincl

    @xfoisaincl.setter
    def xfoisaincl(self, xfoisaincl: str | int | float | types.Real) -> None:
        """
        Sets ``xfoisaincl``.

        Parameters:
            xfoisaincl: Maximum impact parameter for Pauli blocking.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if xfoisaincl is not None:
            if isinstance(xfoisaincl, types.Real):
                xfoisaincl = xfoisaincl
            elif isinstance(xfoisaincl, int):
                xfoisaincl = types.Real(xfoisaincl)
            elif isinstance(xfoisaincl, float):
                xfoisaincl = types.Real(xfoisaincl)
            elif isinstance(xfoisaincl, str):
                xfoisaincl = types.Real.from_mcnp(xfoisaincl)
            else:
                raise TypeError

        self._xfoisaincl: types.Real = xfoisaincl

    @property
    def npaulincl(self) -> types.Integer:
        """
        Gets ``npaulincl``.

        Returns:
            ``npaulincl``.
        """

        return self._npaulincl

    @npaulincl.setter
    def npaulincl(self, npaulincl: str | int | types.Integer) -> None:
        """
        Sets ``npaulincl``.

        Parameters:
            npaulincl: Pauli blocking parameter setting.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if npaulincl is not None:
            if isinstance(npaulincl, types.Integer):
                npaulincl = npaulincl
            elif isinstance(npaulincl, int):
                npaulincl = types.Integer(npaulincl)
            elif isinstance(npaulincl, str):
                npaulincl = types.Integer.from_mcnp(npaulincl)
            else:
                raise TypeError

        if npaulincl is not None and not (npaulincl == 0 or npaulincl == -1 or npaulincl == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, npaulincl)

        self._npaulincl: types.Integer = npaulincl

    @property
    def nosurfincl(self) -> types.Integer:
        """
        Gets ``nosurfincl``.

        Returns:
            ``nosurfincl``.
        """

        return self._nosurfincl

    @nosurfincl.setter
    def nosurfincl(self, nosurfincl: str | int | types.Integer) -> None:
        """
        Sets ``nosurfincl``.

        Parameters:
            nosurfincl: Difuse nuclear surface based on Wood-Saxon density setting.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if nosurfincl is not None:
            if isinstance(nosurfincl, types.Integer):
                nosurfincl = nosurfincl
            elif isinstance(nosurfincl, int):
                nosurfincl = types.Integer(nosurfincl)
            elif isinstance(nosurfincl, str):
                nosurfincl = types.Integer.from_mcnp(nosurfincl)
            else:
                raise TypeError

        if nosurfincl is not None and nosurfincl not in {-2, -1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, nosurfincl)

        self._nosurfincl: types.Integer = nosurfincl

    @property
    def ecutincl(self) -> types.Real:
        """
        Gets ``ecutincl``.

        Returns:
            ``ecutincl``.
        """

        return self._ecutincl

    @ecutincl.setter
    def ecutincl(self, ecutincl: str | int | float | types.Real) -> None:
        """
        Sets ``ecutincl``.

        Parameters:
            ecutincl: Bertini model energy below this energy.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ecutincl is not None:
            if isinstance(ecutincl, types.Real):
                ecutincl = ecutincl
            elif isinstance(ecutincl, int):
                ecutincl = types.Real(ecutincl)
            elif isinstance(ecutincl, float):
                ecutincl = types.Real(ecutincl)
            elif isinstance(ecutincl, str):
                ecutincl = types.Real.from_mcnp(ecutincl)
            else:
                raise TypeError

        self._ecutincl: types.Real = ecutincl

    @property
    def ebankincl(self) -> types.Real:
        """
        Gets ``ebankincl``.

        Returns:
            ``ebankincl``.
        """

        return self._ebankincl

    @ebankincl.setter
    def ebankincl(self, ebankincl: str | int | float | types.Real) -> None:
        """
        Sets ``ebankincl``.

        Parameters:
            ebankincl: INCL bank particles below this energy.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ebankincl is not None:
            if isinstance(ebankincl, types.Real):
                ebankincl = ebankincl
            elif isinstance(ebankincl, int):
                ebankincl = types.Real(ebankincl)
            elif isinstance(ebankincl, float):
                ebankincl = types.Real(ebankincl)
            elif isinstance(ebankincl, str):
                ebankincl = types.Real.from_mcnp(ebankincl)
            else:
                raise TypeError

        self._ebankincl: types.Real = ebankincl

    @property
    def ebankabia(self) -> types.Real:
        """
        Gets ``ebankabia``.

        Returns:
            ``ebankabia``.
        """

        return self._ebankabia

    @ebankabia.setter
    def ebankabia(self, ebankabia: str | int | float | types.Real) -> None:
        """
        Sets ``ebankabia``.

        Parameters:
            ebankabia: ABLA bank particles below this energy.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ebankabia is not None:
            if isinstance(ebankabia, types.Real):
                ebankabia = ebankabia
            elif isinstance(ebankabia, int):
                ebankabia = types.Real(ebankabia)
            elif isinstance(ebankabia, float):
                ebankabia = types.Real(ebankabia)
            elif isinstance(ebankabia, str):
                ebankabia = types.Real.from_mcnp(ebankabia)
            else:
                raise TypeError

        self._ebankabia: types.Real = ebankabia
