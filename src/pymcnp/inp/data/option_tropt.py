import re
import typing

from . import tropt
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Tropt(_option.DataOption_, keyword='tropt'):
    """
    Represents INP data card tropt options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Atropt(( (((mcscat)( \S+))|((eloss)( \S+))|((nreact)( \S+))|((nescat)( \S+))|((genxs)( \S+))))+)?\Z'
    )

    def __init__(self, options: tuple[tropt.TroptOption_] = None):
        """
        Initializes ``DataOption_Tropt``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Tropt``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, tropt.TroptOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Tropt`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Tropt``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Tropt._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(tropt.TroptOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Tropt(options)
