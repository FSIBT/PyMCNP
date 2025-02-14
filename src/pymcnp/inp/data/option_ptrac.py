import re
import typing

from . import ptrac
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Ptrac(_option.DataOption_, keyword='ptrac'):
    """
    Represents INP data card ptrac options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Aptrac(( (((buffer)( \S+))|((file)( \S+))|((max)( \S+))|((meph)( \S+))|((write)( \S+))|((conic)( \S+))|((event)( \S+))|((filter)((( \S+)( \S+)?( \S+))+))|((type)(( \S+)+))|((nps)(( \S+)+))|((cell)(( \S+)+))|((surface)(( \S+)+))|((tally)(( \S+)+))|((value)( \S+))))+)?\Z'
    )

    def __init__(self, options: tuple[ptrac.PtracOption_] = None):
        """
        Initializes ``DataOption_Ptrac``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Ptrac``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, ptrac.PtracOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Ptrac`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Ptrac``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Ptrac._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(ptrac.PtracOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Ptrac(options)
