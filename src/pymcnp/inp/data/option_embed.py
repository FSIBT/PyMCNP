import re
import typing

from . import embed
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Embed(_option.DataOption_, keyword='embed'):
    """
    Represents INP data card embed options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Aembed(( (((background)( \S+))|((meshgeo)( \S+))|((mgeoin)( \S+))|((meeout)( \S+))|((meein)( \S+))|((calcvols)( \S+))|((debug)( \S+))|((filetype)( \S+))|((gmvfile)( \S+))|((length)( \S+))|((mcnpumfile)( \S+))))+)?\Z'
    )

    def __init__(self, options: tuple[embed.EmbedOption_] = None):
        """
        Initializes ``DataOption_Embed``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Embed``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, embed.EmbedOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Embed`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Embed``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Embed._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(embed.EmbedOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Embed(options)
