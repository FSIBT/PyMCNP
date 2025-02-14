import re
import typing

from . import rand
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Rand(_option.DataOption_, keyword='rand'):
    """
    Represents INP data card rand options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Arand(( (((gen)( \S+))|((seed)( \S+))|((stride)( \S+))|((hist)( \S+))))+)?\Z'
    )

    def __init__(self, options: tuple[rand.RandOption_] = None):
        """
        Initializes ``DataOption_Rand``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Rand``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, rand.RandOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Rand`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Rand``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Rand._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(rand.RandOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Rand(options)
