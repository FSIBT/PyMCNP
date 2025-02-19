import re
import typing

from . import _entry
from .....utils import types
from .....utils import errors
from .....utils import _parser


class FilterEntry_Variable(_entry.FilterEntry_):
    """
    Represents INP data card data option ptrac option variable entries.

    Attributes:
        lower: Lower bound for filtering.
        upper: Upper bound for filtering.
        variable: Variable name for PBL derived structure.
    """

    _REGEX = re.compile(r'( \S+)( \S+)?( \S+)')

    def __init__(self, lower: types.Real, variable: types.String, upper: types.Real = None):
        """
        Initializes ``FilterEntry_Variable``.

        Parameters:
            lower: Lower bound for filtering.
            upper: Upper bound for filtering.
            variable: Variable name for PBL derived structure.

        Returns:
            ``FilterEntryVariable``.

        Raises:
            InpError: SEMANTICS_ENTRY_VALUE.
        """

        if lower is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, lower)
        if upper is not None and not (upper >= lower):
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, upper)
        if variable is None or variable not in {''}:
            raise errors.InpError(errors.InpCode.SEMANTICS_ENTRY_VALUE, variable)

        self.parameters: typing.Final[tuple[any]] = types._Tuple([lower, variable, upper])
        self.lower: typing.Final[types.Real] = lower
        self.upper: typing.Final[types.Real] = upper
        self.variable: typing.Final[types.String] = variable

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FilterEntry_Variable`` from INP.

        Parameters:
            INP for ``FilterEntry_Variable``.

        Returns:
            ``FilterEntry_Variable``.

        Raises:
            InpError: SYNTAX_FILTER_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FilterEntry_Variable._REGEX.match(' ' + source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_ENTRY, source)

        lower = types.Real.from_mcnp(tokens[1])
        upper = types.Real.from_mcnp(tokens[2]) if tokens[2] else None
        variable = types.String.from_mcnp(tokens[3])

        return FilterEntry_Variable(lower, variable, upper)
