import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbedOption_Filetype(_option.EmbedOption_, keyword='filetype'):
    """
    Represents INP data card data option filetype options.

    Attributes:
        kind: File type for the elemental edit output file.
    """

    _REGEX = re.compile(r'\Afiletype( \S+)\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``EmbedOption_Filetype``.

        Parameters:
            kind: File type for the elemental edit output file.

        Returns:
            ``EmbedOption_Filetype``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if kind is None or type not in {'ascii', 'binary'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, kind)

        self.value: typing.Final[tuple[any]] = types._Tuple([kind])
        self.kind: typing.Final[types.String] = kind

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbedOption_Filetype`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbedOption_Filetype``.

        Raises:
            InpError: SYNTAX_EMBED_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbedOption_Filetype._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        kind = types.String.from_mcnp(tokens[1])

        return EmbedOption_Filetype(kind)
