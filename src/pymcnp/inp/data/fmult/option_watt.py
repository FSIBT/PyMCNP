import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmultOption_Watt(_option.FmultOption_, keyword='watt'):
    """
    Represents INP data card data option watt options.

    Attributes:
        a: Watt energy spectrum parameters a.
        b: Watt energy spectrum parameters b.
    """

    _REGEX = re.compile(r'\Awatt( \S+)( \S+)\Z')

    def __init__(self, a: types.Real, b: types.Real):
        """
        Initializes ``FmultOption_Watt``.

        Parameters:
            a: Watt energy spectrum parameters a.
            b: Watt energy spectrum parameters b.

        Returns:
            ``FmultOption_Watt``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if a is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, a)
        if b is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, b)

        self.value: typing.Final[tuple[any]] = types._Tuple([a, b])
        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmultOption_Watt`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmultOption_Watt``.

        Raises:
            McnpError: SYNTAX_FMULT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmultOption_Watt._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMULT_OPTION, source)

        a = types.Real.from_mcnp(tokens[1])
        b = types.Real.from_mcnp(tokens[2])

        return FmultOption_Watt(a, b)
