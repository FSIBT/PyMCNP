import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbeeOption_List(_option.EmbeeOption_, keyword='list'):
    """
    Represents INP data card data option list options.

    Attributes:
        reactions: List of reactions.
    """

    _REGEX = re.compile(r'\Alist( \S+)\Z')

    def __init__(self, reactions: types.Real):
        """
        Initializes ``EmbeeOption_List``.

        Parameters:
            reactions: List of reactions.

        Returns:
            ``EmbeeOption_List``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if reactions is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, reactions)

        self.value: typing.Final[tuple[any]] = types._Tuple([reactions])
        self.reactions: typing.Final[types.Real] = reactions

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeeOption_List`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbeeOption_List``.

        Raises:
            McnpError: SYNTAX_EMBEE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbeeOption_List._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBEE_OPTION, source)

        reactions = types.Real.from_mcnp(tokens[1])

        return EmbeeOption_List(reactions)
