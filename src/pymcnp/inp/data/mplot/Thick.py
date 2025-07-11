import re

from . import _option
from ....utils import types
from ....utils import errors


class Thick(_option.MplotOption):
    """
    Represents INP thick elements.

    Attributes:
        x: Thickness of plot curves.
    """

    _KEYWORD = 'thick'

    _ATTRS = {
        'x': types.Real,
    }

    _REGEX = re.compile(rf'\Athick( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, x: str | int | float | types.Real):
        """
        Initializes ``Thick``.

        Parameters:
            x: Thickness of plot curves.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x

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
            x: Thickness of plot curves.

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

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self._x: types.Real = x
