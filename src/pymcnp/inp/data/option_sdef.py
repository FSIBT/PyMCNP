import re
import typing

from . import sdef
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Sdef(_option.DataOption_, keyword='sdef'):
    """
    Represents INP data card sdef options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Asdef(( (((cel)( \S+))|((sur)( \S+))|((erg)( \S+))|((dir)( \S+))|((vec)( \S+)( \S+)( \S+))|((nrm)( \S+))|((pos)(( \S+)+))|((rad)( \S+))|((ext)( \S+))|((axs)( \S+)( \S+)( \S+))|((x)( \S+))|((y)( \S+))|((z)( \S+))|((ccc)( \S+))|((ara)( \S+))|((wgt)( \S+))|((eff)( \S+))|((par)( \S+))|((dat)( \S+)( \S+)( \S+))|((loc)( \S+)( \S+)( \S+))|((bem)( \S+)( \S+)( \S+))|((bap)( \S+)( \S+)( \S+))))+)?\Z'
    )

    def __init__(self, options: tuple[sdef.SdefOption_] = None):
        """
        Initializes ``DataOption_Sdef``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Sdef``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, sdef.SdefOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Sdef`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Sdef``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Sdef._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(sdef.SdefOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Sdef(options)
