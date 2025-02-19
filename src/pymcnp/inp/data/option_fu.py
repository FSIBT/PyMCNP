import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Fu(_option.DataOption_, keyword='fu'):
    """
    Represents INP data card fu options.

    Attributes:
        bounds: Input parameters for user bins.
        nt: Notation to inhibit automatic totaling.
        c: Notation to make bin values cumulative.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Afu(\d+?)(( \S+)+)( \S+)?( \S+)?\Z')

    def __init__(
        self,
        bounds: tuple[types.Real],
        suffix: types.Integer,
        nt: types.String = None,
        c: types.String = None,
    ):
        """
        Initializes ``DataOption_Fu``.

        Parameters:
            bounds: Input parameters for user bins.
            nt: Notation to inhibit automatic totaling.
            c: Notation to make bin values cumulative.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Fu``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if bounds is None or not (filter(lambda entry: not (entry > -1), bounds)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)
        if nt is not None and nt not in {'nt'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, nt)
        if c is not None and c not in {'c'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, c)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([bounds, nt, c])
        self.bounds: typing.Final[tuple[types.Real]] = bounds
        self.nt: typing.Final[types.String] = nt
        self.c: typing.Final[types.String] = c
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Fu`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Fu``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Fu._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        bounds = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )
        nt = types.String.from_mcnp(tokens[3]) if tokens[3] else None
        c = types.String.from_mcnp(tokens[4]) if tokens[4] else None

        return DataOption_Fu(bounds, suffix, nt, c)
