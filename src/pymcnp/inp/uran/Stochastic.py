import re

from . import _entry
from ... import types
from ... import errors


class Stochastic(_entry.UranEntry):
    """
    Represents INP `stochastic` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'universe': types.Integer,
        'maximum_x': types.Real,
        'maximum_y': types.Real,
        'maximum_z': types.Real,
    }

    _REGEX = re.compile(rf'\A({types.Integer._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, universe: str | int | types.Integer, maximum_x: str | int | float | types.Real, maximum_y: str | int | float | types.Real, maximum_z: str | int | float | types.Real):
        """
        Initializes `Stochastic`.

        Parameters:
            universe: Universe number.
            maximum_x: Maximum x displacement.
            maximum_y: Maximum y displacement.
            maximum_z: Maximum z displacement.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.universe: types.Integer = universe
        self.maximum_x: types.Real = maximum_x
        self.maximum_y: types.Real = maximum_y
        self.maximum_z: types.Real = maximum_z

    @property
    def universe(self) -> types.Integer:
        """
        Universe number

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._universe

    @universe.setter
    def universe(self, universe: str | int | types.Integer) -> None:
        """
        Sets `universe`.

        Parameters:
            universe: Universe number.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if universe is not None:
            if isinstance(universe, types.Integer):
                universe = universe
            elif isinstance(universe, int):
                universe = types.Integer(universe)
            elif isinstance(universe, str):
                universe = types.Integer.from_mcnp(universe)

        if universe is None or not (0 <= universe.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, universe)

        self._universe: types.Integer = universe

    @property
    def maximum_x(self) -> types.Real:
        """
        Maximum x displacement

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._maximum_x

    @maximum_x.setter
    def maximum_x(self, maximum_x: str | int | float | types.Real) -> None:
        """
        Sets `maximum_x`.

        Parameters:
            maximum_x: Maximum x displacement.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if maximum_x is not None:
            if isinstance(maximum_x, types.Real):
                maximum_x = maximum_x
            elif isinstance(maximum_x, int) or isinstance(maximum_x, float):
                maximum_x = types.Real(maximum_x)
            elif isinstance(maximum_x, str):
                maximum_x = types.Real.from_mcnp(maximum_x)

        if maximum_x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, maximum_x)

        self._maximum_x: types.Real = maximum_x

    @property
    def maximum_y(self) -> types.Real:
        """
        Maximum y displacement

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._maximum_y

    @maximum_y.setter
    def maximum_y(self, maximum_y: str | int | float | types.Real) -> None:
        """
        Sets `maximum_y`.

        Parameters:
            maximum_y: Maximum y displacement.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if maximum_y is not None:
            if isinstance(maximum_y, types.Real):
                maximum_y = maximum_y
            elif isinstance(maximum_y, int) or isinstance(maximum_y, float):
                maximum_y = types.Real(maximum_y)
            elif isinstance(maximum_y, str):
                maximum_y = types.Real.from_mcnp(maximum_y)

        if maximum_y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, maximum_y)

        self._maximum_y: types.Real = maximum_y

    @property
    def maximum_z(self) -> types.Real:
        """
        Maximum z displacement

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._maximum_z

    @maximum_z.setter
    def maximum_z(self, maximum_z: str | int | float | types.Real) -> None:
        """
        Sets `maximum_z`.

        Parameters:
            maximum_z: Maximum z displacement.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if maximum_z is not None:
            if isinstance(maximum_z, types.Real):
                maximum_z = maximum_z
            elif isinstance(maximum_z, int) or isinstance(maximum_z, float):
                maximum_z = types.Real(maximum_z)
            elif isinstance(maximum_z, str):
                maximum_z = types.Real.from_mcnp(maximum_z)

        if maximum_z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, maximum_z)

        self._maximum_z: types.Real = maximum_z
