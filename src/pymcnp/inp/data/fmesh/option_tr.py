import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Tr(_option.FmeshOption_, keyword='tr'):
    """
    Represents INP data card data option tr options.

    Attributes:
        number: Transformation applied to the mesh.
    """

    _REGEX = re.compile(r'\Atr( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``FmeshOption_Tr``.

        Parameters:
            number: Transformation applied to the mesh.

        Returns:
            ``FmeshOption_Tr``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if number is None or not (1 <= number <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.Integer] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Tr`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Tr``.

        Raises:
            McnpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Tr._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMESH_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return FmeshOption_Tr(number)
