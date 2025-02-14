import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Df(_option.DataOption_, keyword='df'):
    """
    Represents INP data card df options.

    Attributes:
        method: Interpolation method for dose function table.
        values: Dose function values.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Adf(\d+?)( \S+)(( \S+)+)\Z')

    def __init__(self, method: types.String, values: tuple[types.Real], suffix: types.Integer):
        """
        Initializes ``DataOption_Df``.

        Parameters:
            method: Interpolation method for dose function table.
            values: Dose function values.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Df``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if method is None or method not in {'log', 'lin'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, method)
        if values is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, values)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([method, values])
        self.method: typing.Final[types.String] = method
        self.values: typing.Final[tuple[types.Real]] = values
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Df`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Df``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Df._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        method = types.String.from_mcnp(tokens[2])
        values = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[3])]
        )

        return DataOption_Df(method, values, suffix)
