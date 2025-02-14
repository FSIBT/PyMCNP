import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbeeOption_Mtype(_option.EmbeeOption_, keyword='mtype'):
    """
    Represents INP data card data option mtype options.

    Attributes:
        kind: Multiplier type.
    """

    _REGEX = re.compile(r'\Amtype( \S+)\Z')

    def __init__(self, kind: types.String):
        """
        Initializes ``EmbeeOption_Mtype``.

        Parameters:
            kind: Multiplier type.

        Returns:
            ``EmbeeOption_Mtype``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if kind is None or type not in {
            'flux',
            'isotropic',
            'population',
            'reaction',
            'source',
            'track',
        }:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, kind)

        self.value: typing.Final[tuple[any]] = types._Tuple([kind])
        self.kind: typing.Final[types.String] = kind

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeeOption_Mtype`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbeeOption_Mtype``.

        Raises:
            McnpError: SYNTAX_EMBEE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbeeOption_Mtype._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBEE_OPTION, source)

        kind = types.String.from_mcnp(tokens[1])

        return EmbeeOption_Mtype(kind)
