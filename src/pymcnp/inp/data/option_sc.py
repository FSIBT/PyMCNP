import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Sc(_option.DataOption_, keyword='sc'):
    """
    Represents INP data card sc options.

    Attributes:
        comment: source comment.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Asc(\d+?)(( \S+)+)\Z')

    def __init__(self, comment: tuple[str], suffix: types.Integer):
        """
        Initializes ``DataOption_Sc``.

        Parameters:
            comment: source comment.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Sc``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if comment is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, comment)
        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([comment])
        self.comment: typing.Final[tuple[str]] = comment
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Sc`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Sc``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Sc._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        comment = types._Tuple(
            [str.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )

        return DataOption_Sc(comment, suffix)
