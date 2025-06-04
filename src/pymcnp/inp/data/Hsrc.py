import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Hsrc(DataOption):
    """
    Represents INP hsrc elements.

    Attributes:
        x_number: Number of mesh intervals in x direction.
        x_minimum: Minimum x-value for mesh.
        x_maximum: Maximum x-value for mesh.
        y_number: Number of mesh intervals in y direction.
        y_minimum: Minimum y-value for mesh.
        y_maximum: Maximum y-value for mesh.
        z_number: Number of mesh intervals in z direction.
        z_minimum: Minimum z-value for mesh.
        z_maximum: Maximum z-value for mesh.
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
        rf'\Ahsrc( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z'
    )

    def __init__(
        self,
        x_number: types.Integer,
        x_minimum: types.Real,
        x_maximum: types.Real,
        y_number: types.Integer,
        y_minimum: types.Real,
        y_maximum: types.Real,
        z_number: types.Integer,
        z_minimum: types.Real,
        z_maximum: types.Real,
    ):
        """
        Initializes ``Hsrc``.

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
            InpError: SEMANTICS_OPTION.
        """

        if x_number is None or not (x_number.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x_number)
        if x_minimum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x_minimum)
        if x_maximum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x_maximum)
        if y_number is None or not (y_number.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y_number)
        if y_minimum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y_minimum)
        if y_maximum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y_maximum)
        if z_number is None or not (z_number.value > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z_number)
        if z_minimum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z_minimum)
        if z_maximum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z_maximum)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x_number,
                x_minimum,
                x_maximum,
                y_number,
                y_minimum,
                y_maximum,
                z_number,
                z_minimum,
                z_maximum,
            ]
        )

        self.x_number: typing.Final[types.Integer] = x_number
        self.x_minimum: typing.Final[types.Real] = x_minimum
        self.x_maximum: typing.Final[types.Real] = x_maximum
        self.y_number: typing.Final[types.Integer] = y_number
        self.y_minimum: typing.Final[types.Real] = y_minimum
        self.y_maximum: typing.Final[types.Real] = y_maximum
        self.z_number: typing.Final[types.Integer] = z_number
        self.z_minimum: typing.Final[types.Real] = z_minimum
        self.z_maximum: typing.Final[types.Real] = z_maximum


@dataclasses.dataclass
class HsrcBuilder:
    """
    Builds ``Hsrc``.

    Attributes:
        x_number: Number of mesh intervals in x direction.
        x_minimum: Minimum x-value for mesh.
        x_maximum: Maximum x-value for mesh.
        y_number: Number of mesh intervals in y direction.
        y_minimum: Minimum y-value for mesh.
        y_maximum: Maximum y-value for mesh.
        z_number: Number of mesh intervals in z direction.
        z_minimum: Minimum z-value for mesh.
        z_maximum: Maximum z-value for mesh.
    """

    x_number: str | int | types.Integer
    x_minimum: str | float | types.Real
    x_maximum: str | float | types.Real
    y_number: str | int | types.Integer
    y_minimum: str | float | types.Real
    y_maximum: str | float | types.Real
    z_number: str | int | types.Integer
    z_minimum: str | float | types.Real
    z_maximum: str | float | types.Real

    def build(self):
        """
        Builds ``HsrcBuilder`` into ``Hsrc``.

        Returns:
            ``Hsrc`` for ``HsrcBuilder``.
        """

        x_number = self.x_number
        if isinstance(self.x_number, types.Integer):
            x_number = self.x_number
        elif isinstance(self.x_number, int):
            x_number = types.Integer(self.x_number)
        elif isinstance(self.x_number, str):
            x_number = types.Integer.from_mcnp(self.x_number)

        x_minimum = self.x_minimum
        if isinstance(self.x_minimum, types.Real):
            x_minimum = self.x_minimum
        elif isinstance(self.x_minimum, float) or isinstance(self.x_minimum, int):
            x_minimum = types.Real(self.x_minimum)
        elif isinstance(self.x_minimum, str):
            x_minimum = types.Real.from_mcnp(self.x_minimum)

        x_maximum = self.x_maximum
        if isinstance(self.x_maximum, types.Real):
            x_maximum = self.x_maximum
        elif isinstance(self.x_maximum, float) or isinstance(self.x_maximum, int):
            x_maximum = types.Real(self.x_maximum)
        elif isinstance(self.x_maximum, str):
            x_maximum = types.Real.from_mcnp(self.x_maximum)

        y_number = self.y_number
        if isinstance(self.y_number, types.Integer):
            y_number = self.y_number
        elif isinstance(self.y_number, int):
            y_number = types.Integer(self.y_number)
        elif isinstance(self.y_number, str):
            y_number = types.Integer.from_mcnp(self.y_number)

        y_minimum = self.y_minimum
        if isinstance(self.y_minimum, types.Real):
            y_minimum = self.y_minimum
        elif isinstance(self.y_minimum, float) or isinstance(self.y_minimum, int):
            y_minimum = types.Real(self.y_minimum)
        elif isinstance(self.y_minimum, str):
            y_minimum = types.Real.from_mcnp(self.y_minimum)

        y_maximum = self.y_maximum
        if isinstance(self.y_maximum, types.Real):
            y_maximum = self.y_maximum
        elif isinstance(self.y_maximum, float) or isinstance(self.y_maximum, int):
            y_maximum = types.Real(self.y_maximum)
        elif isinstance(self.y_maximum, str):
            y_maximum = types.Real.from_mcnp(self.y_maximum)

        z_number = self.z_number
        if isinstance(self.z_number, types.Integer):
            z_number = self.z_number
        elif isinstance(self.z_number, int):
            z_number = types.Integer(self.z_number)
        elif isinstance(self.z_number, str):
            z_number = types.Integer.from_mcnp(self.z_number)

        z_minimum = self.z_minimum
        if isinstance(self.z_minimum, types.Real):
            z_minimum = self.z_minimum
        elif isinstance(self.z_minimum, float) or isinstance(self.z_minimum, int):
            z_minimum = types.Real(self.z_minimum)
        elif isinstance(self.z_minimum, str):
            z_minimum = types.Real.from_mcnp(self.z_minimum)

        z_maximum = self.z_maximum
        if isinstance(self.z_maximum, types.Real):
            z_maximum = self.z_maximum
        elif isinstance(self.z_maximum, float) or isinstance(self.z_maximum, int):
            z_maximum = types.Real(self.z_maximum)
        elif isinstance(self.z_maximum, str):
            z_maximum = types.Real.from_mcnp(self.z_maximum)

        return Hsrc(
            x_number=x_number,
            x_minimum=x_minimum,
            x_maximum=x_maximum,
            y_number=y_number,
            y_minimum=y_minimum,
            y_maximum=y_maximum,
            z_number=z_number,
            z_minimum=z_minimum,
            z_maximum=z_maximum,
        )

    @staticmethod
    def unbuild(ast: Hsrc):
        """
        Unbuilds ``Hsrc`` into ``HsrcBuilder``

        Returns:
            ``HsrcBuilder`` for ``Hsrc``.
        """

        return Hsrc(
            x_number=copy.deepcopy(ast.x_number),
            x_minimum=copy.deepcopy(ast.x_minimum),
            x_maximum=copy.deepcopy(ast.x_maximum),
            y_number=copy.deepcopy(ast.y_number),
            y_minimum=copy.deepcopy(ast.y_minimum),
            y_maximum=copy.deepcopy(ast.y_maximum),
            z_number=copy.deepcopy(ast.z_number),
            z_minimum=copy.deepcopy(ast.z_minimum),
            z_maximum=copy.deepcopy(ast.z_maximum),
        )
