import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class StopOption_Fk(_option.StopOption_, keyword='fk'):
    """
    Represents INP data card data option fk options.

    Attributes:
        e: Tally fluctuation relative error before stop.
        suffix: Data card option option suffix.
    """

    _REGEX = re.compile(r'\Afk(\d+?)( \S+)\Z')

    def __init__(self, e: types.Integer, suffix: types.Integer):
        """
        Initializes ``StopOption_Fk``.

        Parameters:
            e: Tally fluctuation relative error before stop.
            suffix: Data card option option suffix.

        Returns:
            ``StopOption_Fk``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if e is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, e)
        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple([e])
        self.e: typing.Final[types.Integer] = e
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``StopOption_Fk`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``StopOption_Fk``.

        Raises:
            McnpError: SYNTAX_STOP_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = StopOption_Fk._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_STOP_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        e = types.Integer.from_mcnp(tokens[2])

        return StopOption_Fk(e, suffix)
