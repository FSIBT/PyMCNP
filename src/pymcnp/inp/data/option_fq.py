import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Fq(_option.DataOption_, keyword='fq'):
    """
    Represents INP data card fq options.

    Attributes:
        a1: Letters representing tally bin types.
        a2: Letters representing tally bin types.
        a3: Letters representing tally bin types.
        a4: Letters representing tally bin types.
        a5: Letters representing tally bin types.
        a6: Letters representing tally bin types.
        a7: Letters representing tally bin types.
        a8: Letters representing tally bin types.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Afq(\d+?)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z')

    def __init__(
        self,
        a1: types.String,
        a2: types.String,
        a3: types.String,
        a4: types.String,
        a5: types.String,
        a6: types.String,
        a7: types.String,
        a8: types.String,
        suffix: types.Integer,
    ):
        """
        Initializes ``DataOption_Fq``.

        Parameters:
            a1: Letters representing tally bin types.
            a2: Letters representing tally bin types.
            a3: Letters representing tally bin types.
            a4: Letters representing tally bin types.
            a5: Letters representing tally bin types.
            a6: Letters representing tally bin types.
            a7: Letters representing tally bin types.
            a8: Letters representing tally bin types.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Fq``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if a1 is None or a1 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, a1)
        if a2 is None or a2 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, a2)
        if a3 is None or a3 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, a3)
        if a4 is None or a4 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, a4)
        if a5 is None or a5 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, a5)
        if a6 is None or a6 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, a6)
        if a7 is None or a7 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, a7)
        if a8 is None or a8 not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, a8)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([a1, a2, a3, a4, a5, a6, a7, a8])
        self.a1: typing.Final[types.String] = a1
        self.a2: typing.Final[types.String] = a2
        self.a3: typing.Final[types.String] = a3
        self.a4: typing.Final[types.String] = a4
        self.a5: typing.Final[types.String] = a5
        self.a6: typing.Final[types.String] = a6
        self.a7: typing.Final[types.String] = a7
        self.a8: typing.Final[types.String] = a8
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Fq`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Fq``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Fq._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        a1 = types.String.from_mcnp(tokens[2])
        a2 = types.String.from_mcnp(tokens[3])
        a3 = types.String.from_mcnp(tokens[4])
        a4 = types.String.from_mcnp(tokens[5])
        a5 = types.String.from_mcnp(tokens[6])
        a6 = types.String.from_mcnp(tokens[7])
        a7 = types.String.from_mcnp(tokens[8])
        a8 = types.String.from_mcnp(tokens[9])

        return DataOption_Fq(a1, a2, a3, a4, a5, a6, a7, a8, suffix)
