import re

from . import _entry
from ... import types
from ... import errors


class Ring(_entry.FEntry_2):
    """
    Represents INP `ring` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'distance': types.Real,
        'radius': types.Real,
        'ro': types.Integer,
    }

    _REGEX = re.compile(rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, distance: str | int | float | types.Real, radius: str | int | float | types.Real, ro: str | int | types.Integer):
        """
        Initializes `Ring`.

        Parameters:
            distance: Ring position.
            radius: Ring radius.
            ro: Ring radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.distance: types.Real = distance
        self.radius: types.Real = radius
        self.ro: types.Integer = ro

    @property
    def distance(self) -> types.Real:
        """
        Ring position

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._distance

    @distance.setter
    def distance(self, distance: str | int | float | types.Real) -> None:
        """
        Sets `distance`.

        Parameters:
            distance: Ring position.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if distance is not None:
            if isinstance(distance, types.Real):
                distance = distance
            elif isinstance(distance, int) or isinstance(distance, float):
                distance = types.Real(distance)
            elif isinstance(distance, str):
                distance = types.Real.from_mcnp(distance)

        if distance is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, distance)

        self._distance: types.Real = distance

    @property
    def radius(self) -> types.Real:
        """
        Ring radius

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
            radius: Ring radius.

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
    def ro(self) -> types.Integer:
        """
        Ring radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ro

    @ro.setter
    def ro(self, ro: str | int | types.Integer) -> None:
        """
        Sets `ro`.

        Parameters:
            ro: Ring radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ro is not None:
            if isinstance(ro, types.Integer):
                ro = ro
            elif isinstance(ro, int):
                ro = types.Integer(ro)
            elif isinstance(ro, str):
                ro = types.Integer.from_mcnp(ro)

        if ro is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ro)

        self._ro: types.Integer = ro
