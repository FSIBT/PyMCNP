import re

from . import _option
from ... import types


class Spline(_option.MplotOption):
    """
    Represents INP `spline` elements.
    """

    _KEYWORD = 'spline'

    _ATTRS = {
        'x': types.Real,
    }

    _REGEX = re.compile(rf'\Aspline( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)

    def __init__(self, x: str | int | float | types.Real = None):
        """
        Initializes `Spline`.

        Parameters:
            x: Tension of rational splines.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x

    @property
    def x(self) -> types.Real:
        """
        Tension of rational splines

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x

    @x.setter
    def x(self, x: str | int | float | types.Real) -> None:
        """
        Sets `x`.

        Parameters:
            x: Tension of rational splines.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.Real):
                x = x
            elif isinstance(x, int) or isinstance(x, float):
                x = types.Real(x)
            elif isinstance(x, str):
                x = types.Real.from_mcnp(x)

        self._x: types.Real = x
