import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Refs(_option.MOption_, keyword='refs'):
    """
    Represents INP data card data option refs options.

    Attributes:
        coefficents: Sellmeier coefficents.
    """

    _REGEX = re.compile(r'\Arefs(( \S+)+)\Z')

    def __init__(self, coefficents: tuple[types.Real]):
        """
        Initializes ``MOption_Refs``.

        Parameters:
            coefficents: Sellmeier coefficents.

        Returns:
            ``MOption_Refs``.

        Raises:
            InpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if coefficents is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_OPTION_VALUE, coefficents)

        self.value: typing.Final[tuple[any]] = types._Tuple([coefficents])
        self.coefficents: typing.Final[tuple[types.Real]] = coefficents

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MOption_Refs`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Refs``.

        Raises:
            InpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Refs._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_M_OPTION, source)

        coefficents = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return MOption_Refs(coefficents)
