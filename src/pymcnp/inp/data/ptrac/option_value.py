import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PtracOption_Value(_option.PtracOption_, keyword='value'):
    """
    Represents INP data card data option value options.

    Attributes:
        cutoff: Specifies tally cutoff above which history events will be written..
    """

    _REGEX = re.compile(r'\Avalue( \S+)\Z')

    def __init__(self, cutoff: types.Real):
        """
        Initializes ``PtracOption_Value``.

        Parameters:
            cutoff: Specifies tally cutoff above which history events will be written..

        Returns:
            ``PtracOption_Value``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cutoff is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutoff)

        self.value: typing.Final[tuple[any]] = types._Tuple([cutoff])
        self.cutoff: typing.Final[types.Real] = cutoff

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracOption_Value`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PtracOption_Value``.

        Raises:
            InpError: SYNTAX_PTRAC_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracOption_Value._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        cutoff = types.Real.from_mcnp(tokens[1])

        return PtracOption_Value(cutoff)
