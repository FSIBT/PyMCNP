import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_De(_option.DataOption_, keyword='de'):
    """
    Represents INP data card de options.

    Attributes:
        method: Interpolation method for energy table.
        values: Energy values.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Ade(\d+?)( \S+)(( \S+)+)\Z')

    def __init__(self, method: types.String, values: tuple[types.Real], suffix: types.Integer):
        """
        Initializes ``DataOption_De``.

        Parameters:
            method: Interpolation method for energy table.
            values: Energy values.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_De``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if method is None or method not in {'log', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, method)
        if values is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, values)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([method, values])
        self.method: typing.Final[types.String] = method
        self.values: typing.Final[tuple[types.Real]] = values
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_De`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_De``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_De._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        method = types.String.from_mcnp(tokens[2])
        values = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[3])]
        )

        return DataOption_De(method, values, suffix)
