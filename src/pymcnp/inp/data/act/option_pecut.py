import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Pecut(_option.ActOption_, keyword='pecut'):
    """
    Represents INP data card data option pecut options.

    Attributes:
        cutoff: Delayed-gamma energy cutoff.
    """

    _REGEX = re.compile(r'\Apecut( \S+)\Z')

    def __init__(self, cutoff: types.Real):
        """
        Initializes ``ActOption_Pecut``.

        Parameters:
            cutoff: Delayed-gamma energy cutoff.

        Returns:
            ``ActOption_Pecut``.

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
        Generates ``ActOption_Pecut`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Pecut``.

        Raises:
            McnpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Pecut._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_ACT_OPTION, source)

        cutoff = types.Real.from_mcnp(tokens[1])

        return ActOption_Pecut(cutoff)
