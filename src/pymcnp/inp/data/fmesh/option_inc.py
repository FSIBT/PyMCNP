import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Inc(_option.FmeshOption_, keyword='inc'):
    """
    Represents INP data card data option inc options.

    Attributes:
        lower: Collision for FMESH tally lower bound.
        upper: Collision for FMESH tally upper bound.
    """

    _REGEX = re.compile(r'\Ainc( \S+)( \S+)?\Z')

    def __init__(self, lower: types.Real, upper: types.Real = None):
        """
        Initializes ``FmeshOption_Inc``.

        Parameters:
            lower: Collision for FMESH tally lower bound.
            upper: Collision for FMESH tally upper bound.

        Returns:
            ``FmeshOption_Inc``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if lower is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, lower)

        self.value: typing.Final[tuple[any]] = types._Tuple([lower, upper])
        self.lower: typing.Final[types.Real] = lower
        self.upper: typing.Final[types.Real] = upper

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Inc`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Inc``.

        Raises:
            McnpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Inc._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMESH_OPTION, source)

        lower = types.Real.from_mcnp(tokens[1])
        upper = types.Real.from_mcnp(tokens[2]) if tokens[2] else None

        return FmeshOption_Inc(lower, upper)
