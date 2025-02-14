import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbeeOption_Atom(_option.EmbeeOption_, keyword='atom'):
    """
    Represents INP data card data option atom options.

    Attributes:
        setting: Flag to multiply by atom density.
    """

    _REGEX = re.compile(r'\Aatom( \S+)\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``EmbeeOption_Atom``.

        Parameters:
            setting: Flag to multiply by atom density.

        Returns:
            ``EmbeeOption_Atom``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, setting)

        self.value: typing.Final[tuple[any]] = types._Tuple([setting])
        self.setting: typing.Final[types.String] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeeOption_Atom`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbeeOption_Atom``.

        Raises:
            McnpError: SYNTAX_EMBEE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbeeOption_Atom._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBEE_OPTION, source)

        setting = types.String.from_mcnp(tokens[1])

        return EmbeeOption_Atom(setting)
