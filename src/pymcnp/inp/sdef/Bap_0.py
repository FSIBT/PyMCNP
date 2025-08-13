import re

from . import _option
from ... import types
from ... import errors


class Bap_0(_option.SdefOption):
    """
    Represents INP `bap` elements variation #0.
    """

    _KEYWORD = 'bap'

    _ATTRS = {
        'ba1': types.Real,
        'ba2': types.Real,
        'u': types.Real,
    }

    _REGEX = re.compile(rf'\Abap( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, ba1: str | int | float | types.Real, ba2: str | int | float | types.Real, u: str | int | float | types.Real):
        """
        Initializes `Bap_0`.

        Parameters:
            ba1: Beam aperture half-width in the x transverse direction.
            ba2: Beam aperture half-width in the y transverse direction.
            u: Unused, arrbirary value.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.ba1: types.Real = ba1
        self.ba2: types.Real = ba2
        self.u: types.Real = u

    @property
    def ba1(self) -> types.Real:
        """
        Beam aperture half-width in the x transverse direction

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ba1

    @ba1.setter
    def ba1(self, ba1: str | int | float | types.Real) -> None:
        """
        Sets `ba1`.

        Parameters:
            ba1: Beam aperture half-width in the x transverse direction.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ba1 is not None:
            if isinstance(ba1, types.Real):
                ba1 = ba1
            elif isinstance(ba1, int) or isinstance(ba1, float):
                ba1 = types.Real(ba1)
            elif isinstance(ba1, str):
                ba1 = types.Real.from_mcnp(ba1)

        if ba1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ba1)

        self._ba1: types.Real = ba1

    @property
    def ba2(self) -> types.Real:
        """
        Beam aperture half-width in the y transverse direction

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ba2

    @ba2.setter
    def ba2(self, ba2: str | int | float | types.Real) -> None:
        """
        Sets `ba2`.

        Parameters:
            ba2: Beam aperture half-width in the y transverse direction.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ba2 is not None:
            if isinstance(ba2, types.Real):
                ba2 = ba2
            elif isinstance(ba2, int) or isinstance(ba2, float):
                ba2 = types.Real(ba2)
            elif isinstance(ba2, str):
                ba2 = types.Real.from_mcnp(ba2)

        if ba2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ba2)

        self._ba2: types.Real = ba2

    @property
    def u(self) -> types.Real:
        """
        Unused, arrbirary value

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._u

    @u.setter
    def u(self, u: str | int | float | types.Real) -> None:
        """
        Sets `u`.

        Parameters:
            u: Unused, arrbirary value.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if u is not None:
            if isinstance(u, types.Real):
                u = u
            elif isinstance(u, int) or isinstance(u, float):
                u = types.Real(u)
            elif isinstance(u, str):
                u = types.Real.from_mcnp(u)

        if u is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, u)

        self._u: types.Real = u
