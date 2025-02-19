import re
import typing

from . import var
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Var(_option.DataOption_, keyword='var'):
    """
    Represents INP data card var options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(r'\Avar(( (((rr)( \S+))))+)?\Z')

    def __init__(self, options: tuple[var.VarOption_] = None):
        """
        Initializes ``DataOption_Var``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Var``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, var.VarOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Var`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Var``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Var._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(var.VarOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Var(options)
