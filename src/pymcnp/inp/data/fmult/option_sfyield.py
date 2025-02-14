import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmultOption_Sfyield(_option.FmultOption_, keyword='sfyield'):
    """
    Represents INP data card data option sfyield options.

    Attributes:
        fission_yield: Spontaneous fission yield.
    """

    _REGEX = re.compile(r'\Asfyield( \S+)\Z')

    def __init__(self, fission_yield: types.Real):
        """
        Initializes ``FmultOption_Sfyield``.

        Parameters:
            fission_yield: Spontaneous fission yield.

        Returns:
            ``FmultOption_Sfyield``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if fission_yield is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, fission_yield)

        self.value: typing.Final[tuple[any]] = types._Tuple([fission_yield])
        self.fission_yield: typing.Final[types.Real] = fission_yield

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmultOption_Sfyield`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmultOption_Sfyield``.

        Raises:
            McnpError: SYNTAX_FMULT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmultOption_Sfyield._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMULT_OPTION, source)

        fission_yield = types.Real.from_mcnp(tokens[1])

        return FmultOption_Sfyield(fission_yield)
