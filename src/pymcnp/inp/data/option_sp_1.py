import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Sp1(_option.DataOption_, keyword='sp'):
    """
    Represents INP data card sp_1 options.

    Attributes:
        function: Built-in function designator.
        a: Built-in function parameter #1.
        b: Built-in function parameter #2.
    """

    _REGEX = re.compile(r'\Asp( \S+)( \S+)( \S+)?\Z')

    def __init__(self, function: types.Integer, a: types.Real, b: types.Real = None):
        """
        Initializes ``DataOption_Sp1``.

        Parameters:
            function: Built-in function designator.
            a: Built-in function parameter #1.
            b: Built-in function parameter #2.

        Returns:
            ``DataOption_Sp1``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if function is None or function not in {-2, -3, -4, -5, -6, -7, -21, -31, -41}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, function)
        if a is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, a)

        self.value: typing.Final[tuple[any]] = types._Tuple([function, a, b])
        self.function: typing.Final[types.Integer] = function
        self.a: typing.Final[types.Real] = a
        self.b: typing.Final[types.Real] = b

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Sp1`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Sp1``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Sp1._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        function = types.Integer.from_mcnp(tokens[1])
        a = types.Real.from_mcnp(tokens[2])
        b = types.Real.from_mcnp(tokens[3]) if tokens[3] else None

        return DataOption_Sp1(function, a, b)
