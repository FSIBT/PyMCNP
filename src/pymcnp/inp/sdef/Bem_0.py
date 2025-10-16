import re

from . import _option
from ... import types
from ... import errors


class Bem_0(_option.SdefOption):
    """
    Represents INP `bem` elements variation #0.
    """

    _KEYWORD = 'bem'

    _ATTRS = {
        'exn': types.Real,
        'eyn': types.Real,
        'bml': types.Real,
    }

    _REGEX = re.compile(rf'\Abem( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, exn: str | int | float | types.Real, eyn: str | int | float | types.Real, bml: str | int | float | types.Real):
        """
        Initializes `Bem_0`.

        Parameters:
            exn: Normalized beam emittance parameter for x coordinates.
            eyn: Normalized beam emittance parameter for x coordinates.
            bml: Distance from the aperture to the spot.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.exn: types.Real = exn
        self.eyn: types.Real = eyn
        self.bml: types.Real = bml

    @property
    def exn(self) -> types.Real:
        """
        Normalized beam emittance parameter for x coordinates

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._exn

    @exn.setter
    def exn(self, exn: str | int | float | types.Real) -> None:
        """
        Sets `exn`.

        Parameters:
            exn: Normalized beam emittance parameter for x coordinates.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if exn is not None:
            if isinstance(exn, types.Real):
                exn = exn
            elif isinstance(exn, int) or isinstance(exn, float):
                exn = types.Real(exn)
            elif isinstance(exn, str):
                exn = types.Real.from_mcnp(exn)

        if exn is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, exn)

        self._exn: types.Real = exn

    @property
    def eyn(self) -> types.Real:
        """
        Normalized beam emittance parameter for x coordinates

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._eyn

    @eyn.setter
    def eyn(self, eyn: str | int | float | types.Real) -> None:
        """
        Sets `eyn`.

        Parameters:
            eyn: Normalized beam emittance parameter for x coordinates.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if eyn is not None:
            if isinstance(eyn, types.Real):
                eyn = eyn
            elif isinstance(eyn, int) or isinstance(eyn, float):
                eyn = types.Real(eyn)
            elif isinstance(eyn, str):
                eyn = types.Real.from_mcnp(eyn)

        if eyn is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, eyn)

        self._eyn: types.Real = eyn

    @property
    def bml(self) -> types.Real:
        """
        Distance from the aperture to the spot

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._bml

    @bml.setter
    def bml(self, bml: str | int | float | types.Real) -> None:
        """
        Sets `bml`.

        Parameters:
            bml: Distance from the aperture to the spot.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if bml is not None:
            if isinstance(bml, types.Real):
                bml = bml
            elif isinstance(bml, int) or isinstance(bml, float):
                bml = types.Real(bml)
            elif isinstance(bml, str):
                bml = types.Real.from_mcnp(bml)

        if bml is None or not (bml >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bml)

        self._bml: types.Real = bml
