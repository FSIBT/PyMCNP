import re

from . import _option
from ....utils import types
from ....utils import errors


class Subtitle(_option.MplotOption):
    """
    Represents INP subtitle elements.

    Attributes:
        x: x-coordinate of location.
        y: y-coordinate of location.
        aa: Line to substitute.
    """

    _KEYWORD = 'subtitle'

    _ATTRS = {
        'x': types.Integer,
        'y': types.Integer,
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Asubtitle( {types.Integer._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( \"{types.String._REGEX.pattern[2:-2]}\")\Z')

    def __init__(self, x: str | int | types.Integer, y: str | int | types.Integer, aa: str | types.String):
        """
        Initializes ``Subtitle``.

        Parameters:
            x: x-coordinate of location.
            y: y-coordinate of location.
            aa: Line to substitute.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Integer = x
        self.y: types.Integer = y
        self.aa: types.String = aa

    @property
    def x(self) -> types.Integer:
        """
        Gets ``x``.

        Returns:
            ``x``.
        """

        return self._x

    @x.setter
    def x(self, x: str | int | types.Integer) -> None:
        """
        Sets ``x``.

        Parameters:
            x: x-coordinate of location.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.Integer):
                x = x
            elif isinstance(x, int):
                x = types.Integer(x)
            elif isinstance(x, str):
                x = types.Integer.from_mcnp(x)
            else:
                raise TypeError

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self._x: types.Integer = x

    @property
    def y(self) -> types.Integer:
        """
        Gets ``y``.

        Returns:
            ``y``.
        """

        return self._y

    @y.setter
    def y(self, y: str | int | types.Integer) -> None:
        """
        Sets ``y``.

        Parameters:
            y: y-coordinate of location.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y is not None:
            if isinstance(y, types.Integer):
                y = y
            elif isinstance(y, int):
                y = types.Integer(y)
            elif isinstance(y, str):
                y = types.Integer.from_mcnp(y)
            else:
                raise TypeError

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)

        self._y: types.Integer = y

    @property
    def aa(self) -> types.String:
        """
        Gets ``aa``.

        Returns:
            ``aa``.
        """

        return self._aa

    @aa.setter
    def aa(self, aa: str | types.String) -> None:
        """
        Sets ``aa``.

        Parameters:
            aa: Line to substitute.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if aa is not None:
            if isinstance(aa, types.String):
                aa = aa
            elif isinstance(aa, str):
                aa = types.String.from_mcnp(aa)
            else:
                raise TypeError

        if aa is None or not (len(aa) <= 40):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self._aa: types.String = aa
