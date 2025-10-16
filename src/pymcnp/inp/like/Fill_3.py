import re

from . import _option
from ... import types
from ... import errors


class Fill_3(_option.LikeOption):
    """
    Represents INP `fill` elements variation #3.
    """

    _KEYWORD = 'fill'

    _ATTRS = {
        'prefix': types.String,
        'universe': types.Integer,
        'transformation': types.Transformation_2,
    }

    _REGEX = re.compile(rf'\A([*])?fill( {types.Integer._REGEX.pattern[2:-2]})( {types.Transformation_2._REGEX.pattern[2:-2]}| [(]{types.Transformation_2._REGEX.pattern[2:-2]}[)])?\Z', re.IGNORECASE)

    def __init__(self, universe: str | int | types.Integer, prefix: str | types.String = None, transformation: str | types.Transformation_2 = None):
        """
        Initializes `Fill_3`.

        Parameters:
            prefix: Star prefix.
            universe: Cell fill universe number.
            transformation: Cell fill transformation.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.prefix: types.String = prefix
        self.universe: types.Integer = universe
        self.transformation: types.Transformation_2 = transformation

    @property
    def prefix(self) -> types.String:
        """
        Gets `prefix`.

        Returns:
            `prefix`.
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets `prefix`.

        Parameters:
            prefix: Star prefix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)

        if prefix is not None and prefix.value.lower() not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)

        self._prefix: types.String = prefix

    @property
    def universe(self) -> types.Integer:
        """
        Gets `universe`.

        Returns:
            `universe`.
        """

        return self._universe

    @universe.setter
    def universe(self, universe: str | int | types.Integer) -> None:
        """
        Sets `universe`.

        Parameters:
            universe: Cell fill universe number.

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

        if universe is None or not (universe == 10000000000 or (universe >= 0 and universe <= 99_999_999)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, universe)

        self._universe: types.Integer = universe

    @property
    def transformation(self) -> types.Transformation_2:
        """
        Gets `transformation`.

        Returns:
            `transformation`.
        """

        return self._transformation

    @transformation.setter
    def transformation(self, transformation: str | types.Transformation_2) -> None:
        """
        Sets `transformation`.

        Parameters:
            transformation: Cell fill transformation.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if transformation is not None:
            if isinstance(transformation, types.Transformation_2):
                transformation = transformation
            elif isinstance(transformation, str):
                transformation = types.Transformation_2.from_mcnp(transformation)

        self._transformation: types.Transformation_2 = transformation
