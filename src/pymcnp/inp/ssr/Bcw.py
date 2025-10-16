import re

from . import _option
from ... import types
from ... import errors


class Bcw(_option.SsrOption):
    """
    Represents INP `bcw` elements.
    """

    _KEYWORD = 'bcw'

    _ATTRS = {
        'radius': types.Real,
        'zb': types.Real,
        'ze': types.Real,
    }

    _REGEX = re.compile(rf'\Abcw( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, radius: str | int | float | types.Real, zb: str | int | float | types.Real, ze: str | int | float | types.Real):
        """
        Initializes `Bcw`.

        Parameters:
            radius: Radius of cylindrical window.
            zb: Bottom of cylindrical window.
            ze: Top of cylindrical window.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.radius: types.Real = radius
        self.zb: types.Real = zb
        self.ze: types.Real = ze

    @property
    def radius(self) -> types.Real:
        """
        Radius of cylindrical window

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._radius

    @radius.setter
    def radius(self, radius: str | int | float | types.Real) -> None:
        """
        Sets `radius`.

        Parameters:
            radius: Radius of cylindrical window.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if radius is not None:
            if isinstance(radius, types.Real):
                radius = radius
            elif isinstance(radius, int) or isinstance(radius, float):
                radius = types.Real(radius)
            elif isinstance(radius, str):
                radius = types.Real.from_mcnp(radius)

        if radius is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, radius)

        self._radius: types.Real = radius

    @property
    def zb(self) -> types.Real:
        """
        Bottom of cylindrical window

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._zb

    @zb.setter
    def zb(self, zb: str | int | float | types.Real) -> None:
        """
        Sets `zb`.

        Parameters:
            zb: Bottom of cylindrical window.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if zb is not None:
            if isinstance(zb, types.Real):
                zb = zb
            elif isinstance(zb, int) or isinstance(zb, float):
                zb = types.Real(zb)
            elif isinstance(zb, str):
                zb = types.Real.from_mcnp(zb)

        if zb is None or not (zb > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zb)

        self._zb: types.Real = zb

    @property
    def ze(self) -> types.Real:
        """
        Top of cylindrical window

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ze

    @ze.setter
    def ze(self, ze: str | int | float | types.Real) -> None:
        """
        Sets `ze`.

        Parameters:
            ze: Top of cylindrical window.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ze is not None:
            if isinstance(ze, types.Real):
                ze = ze
            elif isinstance(ze, int) or isinstance(ze, float):
                ze = types.Real(ze)
            elif isinstance(ze, str):
                ze = types.Real.from_mcnp(ze)

        if ze is None or not (self.zb > 0 and self.zb < ze):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ze)

        self._ze: types.Real = ze
