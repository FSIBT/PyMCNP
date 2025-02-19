import re
import typing

from . import ssr
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Ssr(_option.DataOption_, keyword='ssr'):
    """
    Represents INP data card ssr options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Assr(( (((old)(( \S+)+))|((cel)(( \S+)+))|((new)(( \S+)+))|((pty)(( \S+)+))|((col)( \S+))|((wgt)( \S+))|((psc)( \S+))|((axs)(( \S+)+))|((ext)( \S+))|((poa)( \S+))|((bcw)( \S+)( \S+)( \S+))))+)?\Z'
    )

    def __init__(self, options: tuple[ssr.SsrOption_] = None):
        """
        Initializes ``DataOption_Ssr``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Ssr``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, ssr.SsrOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Ssr`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Ssr``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Ssr._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(ssr.SsrOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Ssr(options)
