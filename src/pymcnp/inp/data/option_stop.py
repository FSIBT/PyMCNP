import re
import typing

from . import stop
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Stop(_option.DataOption_, keyword='stop'):
    """
    Represents INP data card stop options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(r'\Astop(( (((nps)( \S+)( \S+)?)|((ctme)( \S+))|((fk)(\d+?)( \S+))))+)?\Z')

    def __init__(self, options: tuple[stop.StopOption_] = None):
        """
        Initializes ``DataOption_Stop``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Stop``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, stop.StopOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Stop`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Stop``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Stop._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(stop.StopOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Stop(options)
