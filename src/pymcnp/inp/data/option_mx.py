import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Mx(_option.DataOption_, keyword='mx'):
    """
    Represents INP data card mx options.

    Attributes:
        zaids: Zaid substitutions for particles.
        designator: Data card particle designator.
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(r'\Amx(\d+?):(\S+?)(( \S+)+)\Z')

    def __init__(
        self, zaids: tuple[types.Zaid], designator: types.Designator, suffix: types.Integer
    ):
        """
        Initializes ``DataOption_Mx``.

        Parameters:
            zaids: Zaid substitutions for particles.
            designator: Data card particle designator.
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Mx``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_DESIGNATOR.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if zaids is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, zaids)
        if designator is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_DESIGNATOR, designator)
        if suffix is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([zaids])
        self.zaids: typing.Final[tuple[types.Zaid]] = zaids
        self.designator: typing.Final[types.Designator] = designator
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Mx`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Mx``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Mx._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        designator = types.Designator.from_mcnp(tokens[2])
        zaids = types._Tuple(
            [types.Zaid.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[3])]
        )

        return DataOption_Mx(zaids, designator, suffix)
