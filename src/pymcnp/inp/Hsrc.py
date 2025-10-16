import re

from . import _card
from .. import types
from .. import errors


class Hsrc(_card.Card):
    """
    Represents INP `hsrc` cards.
    """

    _KEYWORD = 'hsrc'

    _ATTRS = {
        'x_number': types.Integer,
        'x_minimum': types.Real,
        'x_maximum': types.Real,
        'y_number': types.Integer,
        'y_minimum': types.Real,
        'y_maximum': types.Real,
        'z_number': types.Integer,
        'z_minimum': types.Real,
        'z_maximum': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ahsrc( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        x_number: str | int | types.Integer,
        x_minimum: str | int | float | types.Real,
        x_maximum: str | int | float | types.Real,
        y_number: str | int | types.Integer,
        y_minimum: str | int | float | types.Real,
        y_maximum: str | int | float | types.Real,
        z_number: str | int | types.Integer,
        z_minimum: str | int | float | types.Real,
        z_maximum: str | int | float | types.Real,
    ):
        """
        Initializes `Hsrc`.

        Parameters:
            x_number: Number of mesh intervals in x direction.
            x_minimum: Minimum x-value for mesh.
            x_maximum: Maximum x-value for mesh.
            y_number: Number of mesh intervals in y direction.
            y_minimum: Minimum y-value for mesh.
            y_maximum: Maximum y-value for mesh.
            z_number: Number of mesh intervals in z direction.
            z_minimum: Minimum z-value for mesh.
            z_maximum: Maximum z-value for mesh.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.x_number: types.Integer = x_number
        self.x_minimum: types.Real = x_minimum
        self.x_maximum: types.Real = x_maximum
        self.y_number: types.Integer = y_number
        self.y_minimum: types.Real = y_minimum
        self.y_maximum: types.Real = y_maximum
        self.z_number: types.Integer = z_number
        self.z_minimum: types.Real = z_minimum
        self.z_maximum: types.Real = z_maximum

    @property
    def x_number(self) -> types.Integer:
        """
        Number of mesh intervals in x direction

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x_number

    @x_number.setter
    def x_number(self, x_number: str | int | types.Integer) -> None:
        """
        Sets `x_number`.

        Parameters:
            x_number: Number of mesh intervals in x direction.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x_number is not None:
            if isinstance(x_number, types.Integer):
                x_number = x_number
            elif isinstance(x_number, int):
                x_number = types.Integer(x_number)
            elif isinstance(x_number, str):
                x_number = types.Integer.from_mcnp(x_number)

        if x_number is None or not (x_number > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, x_number)

        self._x_number: types.Integer = x_number

    @property
    def x_minimum(self) -> types.Real:
        """
        Minimum x-value for mesh

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x_minimum

    @x_minimum.setter
    def x_minimum(self, x_minimum: str | int | float | types.Real) -> None:
        """
        Sets `x_minimum`.

        Parameters:
            x_minimum: Minimum x-value for mesh.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x_minimum is not None:
            if isinstance(x_minimum, types.Real):
                x_minimum = x_minimum
            elif isinstance(x_minimum, int) or isinstance(x_minimum, float):
                x_minimum = types.Real(x_minimum)
            elif isinstance(x_minimum, str):
                x_minimum = types.Real.from_mcnp(x_minimum)

        if x_minimum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, x_minimum)

        self._x_minimum: types.Real = x_minimum

    @property
    def x_maximum(self) -> types.Real:
        """
        Maximum x-value for mesh

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x_maximum

    @x_maximum.setter
    def x_maximum(self, x_maximum: str | int | float | types.Real) -> None:
        """
        Sets `x_maximum`.

        Parameters:
            x_maximum: Maximum x-value for mesh.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if x_maximum is not None:
            if isinstance(x_maximum, types.Real):
                x_maximum = x_maximum
            elif isinstance(x_maximum, int) or isinstance(x_maximum, float):
                x_maximum = types.Real(x_maximum)
            elif isinstance(x_maximum, str):
                x_maximum = types.Real.from_mcnp(x_maximum)

        if x_maximum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, x_maximum)

        self._x_maximum: types.Real = x_maximum

    @property
    def y_number(self) -> types.Integer:
        """
        Number of mesh intervals in y direction

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._y_number

    @y_number.setter
    def y_number(self, y_number: str | int | types.Integer) -> None:
        """
        Sets `y_number`.

        Parameters:
            y_number: Number of mesh intervals in y direction.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if y_number is not None:
            if isinstance(y_number, types.Integer):
                y_number = y_number
            elif isinstance(y_number, int):
                y_number = types.Integer(y_number)
            elif isinstance(y_number, str):
                y_number = types.Integer.from_mcnp(y_number)

        if y_number is None or not (y_number > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, y_number)

        self._y_number: types.Integer = y_number

    @property
    def y_minimum(self) -> types.Real:
        """
        Minimum y-value for mesh

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._y_minimum

    @y_minimum.setter
    def y_minimum(self, y_minimum: str | int | float | types.Real) -> None:
        """
        Sets `y_minimum`.

        Parameters:
            y_minimum: Minimum y-value for mesh.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if y_minimum is not None:
            if isinstance(y_minimum, types.Real):
                y_minimum = y_minimum
            elif isinstance(y_minimum, int) or isinstance(y_minimum, float):
                y_minimum = types.Real(y_minimum)
            elif isinstance(y_minimum, str):
                y_minimum = types.Real.from_mcnp(y_minimum)

        if y_minimum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, y_minimum)

        self._y_minimum: types.Real = y_minimum

    @property
    def y_maximum(self) -> types.Real:
        """
        Maximum y-value for mesh

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._y_maximum

    @y_maximum.setter
    def y_maximum(self, y_maximum: str | int | float | types.Real) -> None:
        """
        Sets `y_maximum`.

        Parameters:
            y_maximum: Maximum y-value for mesh.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if y_maximum is not None:
            if isinstance(y_maximum, types.Real):
                y_maximum = y_maximum
            elif isinstance(y_maximum, int) or isinstance(y_maximum, float):
                y_maximum = types.Real(y_maximum)
            elif isinstance(y_maximum, str):
                y_maximum = types.Real.from_mcnp(y_maximum)

        if y_maximum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, y_maximum)

        self._y_maximum: types.Real = y_maximum

    @property
    def z_number(self) -> types.Integer:
        """
        Number of mesh intervals in z direction

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._z_number

    @z_number.setter
    def z_number(self, z_number: str | int | types.Integer) -> None:
        """
        Sets `z_number`.

        Parameters:
            z_number: Number of mesh intervals in z direction.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if z_number is not None:
            if isinstance(z_number, types.Integer):
                z_number = z_number
            elif isinstance(z_number, int):
                z_number = types.Integer(z_number)
            elif isinstance(z_number, str):
                z_number = types.Integer.from_mcnp(z_number)

        if z_number is None or not (z_number > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, z_number)

        self._z_number: types.Integer = z_number

    @property
    def z_minimum(self) -> types.Real:
        """
        Minimum z-value for mesh

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._z_minimum

    @z_minimum.setter
    def z_minimum(self, z_minimum: str | int | float | types.Real) -> None:
        """
        Sets `z_minimum`.

        Parameters:
            z_minimum: Minimum z-value for mesh.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if z_minimum is not None:
            if isinstance(z_minimum, types.Real):
                z_minimum = z_minimum
            elif isinstance(z_minimum, int) or isinstance(z_minimum, float):
                z_minimum = types.Real(z_minimum)
            elif isinstance(z_minimum, str):
                z_minimum = types.Real.from_mcnp(z_minimum)

        if z_minimum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, z_minimum)

        self._z_minimum: types.Real = z_minimum

    @property
    def z_maximum(self) -> types.Real:
        """
        Maximum z-value for mesh

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._z_maximum

    @z_maximum.setter
    def z_maximum(self, z_maximum: str | int | float | types.Real) -> None:
        """
        Sets `z_maximum`.

        Parameters:
            z_maximum: Maximum z-value for mesh.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if z_maximum is not None:
            if isinstance(z_maximum, types.Real):
                z_maximum = z_maximum
            elif isinstance(z_maximum, int) or isinstance(z_maximum, float):
                z_maximum = types.Real(z_maximum)
            elif isinstance(z_maximum, str):
                z_maximum = types.Real.from_mcnp(z_maximum)

        if z_maximum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, z_maximum)

        self._z_maximum: types.Real = z_maximum
