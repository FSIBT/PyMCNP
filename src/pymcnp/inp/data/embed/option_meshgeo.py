import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbedOption_Meshgeo(_option.EmbedOption_, keyword='meshgeo'):
    """
    Represents INP data card data option meshgeo options.

    Attributes:
        form: Format specification of the embedded mesh input file.
    """

    _REGEX = re.compile(r'\Ameshgeo( \S+)\Z')

    def __init__(self, form: types.String):
        """
        Initializes ``EmbedOption_Meshgeo``.

        Parameters:
            form: Format specification of the embedded mesh input file.

        Returns:
            ``EmbedOption_Meshgeo``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if form is None or form not in {'lnk3dnt', 'abaqu', 'mcnpum'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, form)

        self.value: typing.Final[tuple[any]] = types._Tuple([form])
        self.form: typing.Final[types.String] = form

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbedOption_Meshgeo`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbedOption_Meshgeo``.

        Raises:
            McnpError: SYNTAX_EMBED_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbedOption_Meshgeo._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBED_OPTION, source)

        form = types.String.from_mcnp(tokens[1])

        return EmbedOption_Meshgeo(form)
