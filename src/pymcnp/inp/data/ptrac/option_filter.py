import re
import typing

from . import filter
from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Filter(_option.PtracOption_, keyword='filter'):
    """
    Represents INP data card data option filter options.

    Attributes:
        variables: MCNP6 variables for filtering.
    """

    _REGEX = re.compile(r'\Afilter((( \S+)( \S+)?( \S+))+)\Z')

    def __init__(self, variables: tuple[filter.FilterEntry_Variable]):
        """
        Initializes ``PtracOption_Filter``.

        Parameters:
            variables: MCNP6 variables for filtering.

        Returns:
            ``PtracOption_Filter``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if variables is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, variables)

        self.value: typing.Final[tuple[any]] = types._Tuple([variables])
        self.variables: typing.Final[tuple[filter.FilterEntry_Variable]] = variables

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Filter`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Filter``.

        Raises:
            McnpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Filter._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_PTRAC_OPTION, source)

        variables = types._Tuple(
            [
                filter.FilterEntry_Variable.from_mcnp(token[0])
                for token in filter.FilterEntry_Variable._REGEX.finditer(tokens[1])
            ]
        )

        return PtracOption_Filter(variables)
