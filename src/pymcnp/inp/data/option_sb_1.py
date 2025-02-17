import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Sb1(_option.DataOption_, keyword='sb'):
    """
    Represents INP data card sb_1 options.

    Attributes:
        function: Built-in function designator.
        a: Built-in function parameter #1.
        b: Built-in function parameter #2.
    """

    _REGEX = re.compile(r'\Asb( \S+)( \S+)( \S+)?\Z')

    def __init__(self, function: types.Integer, a: types.Real, b: types.Real = None):
        """
        Initializes ``DataOption_Sb1``.

        Parameters:
            function: Built-in function designator.
            a: Built-in function parameter #1.
            b: Built-in function parameter #2.

        Returns:
            ``DataOption_Sb1``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if function is None or function not in {-2, -3, -4, -5, -6, -7, -21, -31, -41}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, function)
        if a is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, a)

        self.value: typing.Final[tuple[any]] = types._Tuple([function, a, b])
        self.function: typing.Final[types.Integer] = function
        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Sb1`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Sb1``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Sb1._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        function = types.Integer.from_mcnp(tokens[1])
        a = types.Real.from_mcnp(tokens[2])
        b = types.Real.from_mcnp(tokens[3]) if tokens[3] else None

        return DataOption_Sb1(function, a, b)
