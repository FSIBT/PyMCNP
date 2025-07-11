import re

from . import _option
from ....utils import types
from ....utils import errors


class Bcw(_option.SsrOption):
    """
    Represents INP bcw elements.

    Attributes:
        radius: Radius of cylindrical window.
        zb: Bottom of cylindrical window.
        ze: Top of cylindrical window.
    """

    _KEYWORD = 'bcw'

    _ATTRS = {
        'radius': types.Real,
        'zb': types.Real,
        'ze': types.Real,
    }

    _REGEX = re.compile(rf'\Abcw( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, radius: str | int | float | types.Real, zb: str | int | float | types.Real, ze: str | int | float | types.Real):
        """
        Initializes ``Bcw``.

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
        Gets ``radius``.

        Returns:
            ``radius``.
        """

        return self._radius

    @radius.setter
    def radius(self, radius: str | int | float | types.Real) -> None:
        """
        Sets ``radius``.

        Parameters:
            radius: Radius of cylindrical window.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if radius is not None:
            if isinstance(radius, types.Real):
                radius = radius
            elif isinstance(radius, int):
                radius = types.Real(radius)
            elif isinstance(radius, float):
                radius = types.Real(radius)
            elif isinstance(radius, str):
                radius = types.Real.from_mcnp(radius)
            else:
                raise TypeError

        if radius is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, radius)

        self._radius: types.Real = radius

    @property
    def zb(self) -> types.Real:
        """
        Gets ``zb``.

        Returns:
            ``zb``.
        """

        return self._zb

    @zb.setter
    def zb(self, zb: str | int | float | types.Real) -> None:
        """
        Sets ``zb``.

        Parameters:
            zb: Bottom of cylindrical window.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if zb is not None:
            if isinstance(zb, types.Real):
                zb = zb
            elif isinstance(zb, int):
                zb = types.Real(zb)
            elif isinstance(zb, float):
                zb = types.Real(zb)
            elif isinstance(zb, str):
                zb = types.Real.from_mcnp(zb)
            else:
                raise TypeError

        if zb is None or not (zb > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, zb)

        self._zb: types.Real = zb

    @property
    def ze(self) -> types.Real:
        """
        Gets ``ze``.

        Returns:
            ``ze``.
        """

        return self._ze

    @ze.setter
    def ze(self, ze: str | int | float | types.Real) -> None:
        """
        Sets ``ze``.

        Parameters:
            ze: Top of cylindrical window.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ze is not None:
            if isinstance(ze, types.Real):
                ze = ze
            elif isinstance(ze, int):
                ze = types.Real(ze)
            elif isinstance(ze, float):
                ze = types.Real(ze)
            elif isinstance(ze, str):
                ze = types.Real.from_mcnp(ze)
            else:
                raise TypeError

        if ze is None or not (self.zb > 0 and self.zb < ze):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ze)

        self._ze: types.Real = ze
