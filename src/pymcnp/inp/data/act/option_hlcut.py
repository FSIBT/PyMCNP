import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Hlcut(_option.ActOption_, keyword='hlcut'):
    """
    Represents INP data card data option hlcut options.

    Attributes:
        cutoff: Spontaneous-decay half-life threshold.
    """

    _REGEX = re.compile(r'\Ahlcut( \S+)\Z')

    def __init__(self, cutoff: types.Real):
        """
        Initializes ``ActOption_Hlcut``.

        Parameters:
            cutoff: Spontaneous-decay half-life threshold.

        Returns:
            ``ActOption_Hlcut``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if cutoff is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, cutoff)

        self.value: typing.Final[tuple[any]] = types._Tuple([cutoff])
        self.cutoff: typing.Final[types.Real] = cutoff

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Hlcut`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Hlcut``.

        Raises:
            McnpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Hlcut._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_ACT_OPTION, source)

        cutoff = types.Real.from_mcnp(tokens[1])

        return ActOption_Hlcut(cutoff)
