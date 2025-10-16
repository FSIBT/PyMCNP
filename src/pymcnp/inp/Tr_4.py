import re

from . import _card
from .. import types
from .. import errors


class Tr_4(_card.Card):
    """
    Represents INP `tr` elements variation #4.
    """

    _KEYWORD = 'tr'

    _ATTRS = {
        'prefix': types.String,
        'suffix': types.Integer,
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        'system': types.Integer,
    }

    _REGEX = re.compile(
        rf'\A([*])?tr(\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE
    )

    def __init__(
        self,
        suffix: str | int | types.Integer,
        x: str | int | float | types.Real,
        y: str | int | float | types.Real,
        z: str | int | float | types.Real,
        prefix: str | types.String = None,
        system: str | int | types.Integer = None,
    ):
        """
        Initializes `Tr_4`.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            x: Displacement vector x component.
            y: Displacement vector y component.
            z: Displacement vector z component.
            system: Coordinate system setting.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.prefix: types.String = prefix
        self.suffix: types.Integer = suffix
        self.x: types.Real = x
        self.y: types.Real = y
        self.z: types.Real = z
        self.system: types.Integer = system

    @property
    def prefix(self) -> types.String:
        """
        Star prefix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets `prefix`.

        Parameters:
            prefix: Star prefix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)

        if prefix is not None and prefix.value.lower() not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, prefix)

        self._prefix: types.String = prefix

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None or not (suffix >= 1 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def x(self) -> types.Real:
        """
        Displacement vector x component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x

    @x.setter
    def x(self, x: str | int | float | types.Real) -> None:
        """
        Sets `x`.

        Parameters:
            x: Displacement vector x component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.Real):
                x = x
            elif isinstance(x, int) or isinstance(x, float):
                x = types.Real(x)
            elif isinstance(x, str):
                x = types.Real.from_mcnp(x)

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, x)

        self._x: types.Real = x

    @property
    def y(self) -> types.Real:
        """
        Displacement vector y component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._y

    @y.setter
    def y(self, y: str | int | float | types.Real) -> None:
        """
        Sets `y`.

        Parameters:
            y: Displacement vector y component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if y is not None:
            if isinstance(y, types.Real):
                y = y
            elif isinstance(y, int) or isinstance(y, float):
                y = types.Real(y)
            elif isinstance(y, str):
                y = types.Real.from_mcnp(y)

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, y)

        self._y: types.Real = y

    @property
    def z(self) -> types.Real:
        """
        Displacement vector z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._z

    @z.setter
    def z(self, z: str | int | float | types.Real) -> None:
        """
        Sets `z`.

        Parameters:
            z: Displacement vector z component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if z is not None:
            if isinstance(z, types.Real):
                z = z
            elif isinstance(z, int) or isinstance(z, float):
                z = types.Real(z)
            elif isinstance(z, str):
                z = types.Real.from_mcnp(z)

        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, z)

        self._z: types.Real = z

    @property
    def system(self) -> types.Integer:
        """
        Coordinate system setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._system

    @system.setter
    def system(self, system: str | int | types.Integer) -> None:
        """
        Sets `system`.

        Parameters:
            system: Coordinate system setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if system is not None:
            if isinstance(system, types.Integer):
                system = system
            elif isinstance(system, int):
                system = types.Integer(system)
            elif isinstance(system, str):
                system = types.Integer.from_mcnp(system)

        if system is not None and not (system == -1 or system == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, system)

        self._system: types.Integer = system
