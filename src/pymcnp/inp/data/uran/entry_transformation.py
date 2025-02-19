import re
import typing

from . import _entry
from ....utils import types
from ....utils import errors
from ....utils import _parser


class UranEntry_Transformation(_entry.UranEntry_):
    """
    Represents INP data card data option transformation entries.

    Attributes:
        number: Universe number for transformation.
        maximum_x: Maximum displacement in the x direction.
        maximum_y: Maximum displacement in the y direction.
        maximum_z: Maximum displacement in the z direction.
    """

    _REGEX = re.compile(r'( \S+)( \S+)( \S+)( \S+)')

    def __init__(
        self,
        number: types.Integer,
        maximum_x: types.Real,
        maximum_y: types.Real,
        maximum_z: types.Real,
    ):
        """
        Initializes ``UranEntry_Transformation``.

        Parameters:
            number: Universe number for transformation.
            maximum_x: Maximum displacement in the x direction.
            maximum_y: Maximum displacement in the y direction.
            maximum_z: Maximum displacement in the z direction.

        Returns:
            ``UranEntryTransformation``.

        Raises:
            InpError: SEMANTICS_ENTRY_VALUE.
        """

        if number is None or not (0 <= number <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, number)
        if maximum_x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, maximum_x)
        if maximum_y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, maximum_y)
        if maximum_z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, maximum_z)

        self.parameters: typing.Final[tuple[any]] = types._Tuple(
            [number, maximum_x, maximum_y, maximum_z]
        )
        self.number: typing.Final[types.Integer] = number
        self.maximum_x: typing.Final[types.Real] = maximum_x
        self.maximum_y: typing.Final[types.Real] = maximum_y
        self.maximum_z: typing.Final[types.Real] = maximum_z

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``UranEntry_Transformation`` from INP.

        Parameters:
            INP for ``UranEntry_Transformation``.

        Returns:
            ``UranEntry_Transformation``.

        Raises:
            InpError: SYNTAX_URAN_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = UranEntry_Transformation._REGEX.match(' ' + source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_ENTRY, source)

        number = types.Integer.from_mcnp(tokens[1])
        maximum_x = types.Real.from_mcnp(tokens[2])
        maximum_y = types.Real.from_mcnp(tokens[3])
        maximum_z = types.Real.from_mcnp(tokens[4])

        return UranEntry_Transformation(number, maximum_x, maximum_y, maximum_z)
