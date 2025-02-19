import re
import typing

from . import kopts
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Kopts(_option.DataOption_, keyword='kopts'):
    """
    Represents INP data card kopts options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Akopts(( (((blocksize)( \S+))|((kinetics)( \S+))|((precursor)( \S+))|((ksental)( \S+))|((fmat)( \S+))|((fmatskpt)( \S+))|((fmatncyc)( \S+))|((fmatspace)( \S+))|((fmataccel)( \S+))|((fmatreduce)( \S+))|((fmatnx)( \S+))|((fmatny)( \S+))|((fmatnz)( \S+))))+)?\Z'
    )

    def __init__(self, options: tuple[kopts.KoptsOption_] = None):
        """
        Initializes ``DataOption_Kopts``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Kopts``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, kopts.KoptsOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Kopts`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Kopts``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Kopts._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(kopts.KoptsOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Kopts(options)
