import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Hsrc(_option.DataOption_, keyword='hsrc'):
    """
    Represents INP data card hsrc options.

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

    _REGEX = re.compile(r'\Ahsrc( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

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
        Initializes ``DataOption_Hsrc``.

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

        Returns:
            ``DataOption_Hsrc``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if x_number is None or not (x_number > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, x_number)
        if x_minimum is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, x_minimum)
        if x_maximum is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, x_maximum)
        if y_number is None or not (y_number > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, y_number)
        if y_minimum is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, y_minimum)
        if y_maximum is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, y_maximum)
        if z_number is None or not (z_number > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, z_number)
        if z_minimum is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, z_minimum)
        if z_maximum is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, z_maximum)

        self.value: typing.Final[tuple[any]] = types._Tuple(
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

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Hsrc`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Hsrc``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Hsrc._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        x_number = types.Integer.from_mcnp(tokens[1])
        x_minimum = types.Real.from_mcnp(tokens[2])
        x_maximum = types.Real.from_mcnp(tokens[3])
        y_number = types.Integer.from_mcnp(tokens[4])
        y_minimum = types.Real.from_mcnp(tokens[5])
        y_maximum = types.Real.from_mcnp(tokens[6])
        z_number = types.Integer.from_mcnp(tokens[7])
        z_minimum = types.Real.from_mcnp(tokens[8])
        z_maximum = types.Real.from_mcnp(tokens[9])

        return DataOption_Hsrc(
            x_number,
            x_minimum,
            x_maximum,
            y_number,
            y_minimum,
            y_maximum,
            z_number,
            z_minimum,
            z_maximum,
        )
