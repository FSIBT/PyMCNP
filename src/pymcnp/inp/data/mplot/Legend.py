import re

from . import _option
from ....utils import types


class Legend(_option.MplotOption):
    """
    Represents INP legend elements.

    Attributes:
        x: Label x-location.
        y: Label x-location.
    """

    _KEYWORD = 'legend'

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
    }

    _REGEX = re.compile(rf'\Alegend( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, x: str | int | float | types.Real = None, y: str | int | float | types.Real = None):
        """
        Initializes ``Legend``.

        Parameters:
            x: Label x-location.
            y: Label x-location.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x
        self.y: types.Real = y

    @property
    def x(self) -> types.Real:
        """
        Gets ``x``.

        Returns:
            ``x``.
        """

        return self._x

    @x.setter
    def x(self, x: str | int | float | types.Real) -> None:
        """
        Sets ``x``.

        Parameters:
            x: Label x-location.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.Real):
                x = x
            elif isinstance(x, int):
                x = types.Real(x)
            elif isinstance(x, float):
                x = types.Real(x)
            elif isinstance(x, str):
                x = types.Real.from_mcnp(x)
            else:
                raise TypeError

        self._x: types.Real = x

    @property
    def y(self) -> types.Real:
        """
        Gets ``y``.

        Returns:
            ``y``.
        """

        return self._y

    @y.setter
    def y(self, y: str | int | float | types.Real) -> None:
        """
        Sets ``y``.

        Parameters:
            y: Label x-location.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y is not None:
            if isinstance(y, types.Real):
                y = y
            elif isinstance(y, int):
                y = types.Real(y)
            elif isinstance(y, float):
                y = types.Real(y)
            elif isinstance(y, str):
                y = types.Real.from_mcnp(y)
            else:
                raise TypeError

        self._y: types.Real = y
