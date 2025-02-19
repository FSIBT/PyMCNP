import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Fs(_option.DataOption_, keyword='fs'):
    """
    Represents INP data card fs options.

    Attributes:
        numbers: Signed problem number of a segmenting surface..
        t: Notation to provide totals.
        c: Notation to make bin values cumulative.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Afs(\d+?)(( \S+)+)( \S+)?( \S+)?\Z')

    def __init__(
        self,
        numbers: tuple[types.Integer],
        suffix: types.Integer,
        t: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``DataOption_Fs``.

        Parameters:
            numbers: Signed problem number of a segmenting surface..
            t: Notation to provide totals.
            c: Notation to make bin values cumulative.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Fs``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if numbers is None or not (
            filter(lambda entry: not (-99_999_999 <= numbers <= 99_999_999), numbers)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numbers)
        if t is not None and t not in {'t'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, t)
        if c is not None and c not in {'c'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, c)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([numbers, t, c])
        self.numbers: typing.Final[tuple[types.Integer]] = numbers
        self.t: typing.Final[types.String] = t
        self.c: typing.Final[types.String] = c
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Fs`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Fs``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Fs._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        numbers = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )
        t = types.String.from_mcnp(tokens[3]) if tokens[3] else None
        c = types.String.from_mcnp(tokens[4]) if tokens[4] else None

        return DataOption_Fs(numbers, suffix, t, c)
