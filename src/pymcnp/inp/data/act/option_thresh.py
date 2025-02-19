import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class ActOption_Thresh(_option.ActOption_, keyword='thresh'):
    """
    Represents INP data card data option thresh options.

    Attributes:
        fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.
    """

    _REGEX = re.compile(r'\Athresh( \S+)\Z')

    def __init__(self, fraction: types.Real):
        """
        Initializes ``ActOption_Thresh``.

        Parameters:
            fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.

        Returns:
            ``ActOption_Thresh``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fraction is None or not (0 <= fraction <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fraction)

        self.value: typing.Final[tuple[any]] = types._Tuple([fraction])
        self.fraction: typing.Final[types.Real] = fraction

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActOption_Thresh`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``ActOption_Thresh``.

        Raises:
            InpError: SYNTAX_ACT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = ActOption_Thresh._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        fraction = types.Real.from_mcnp(tokens[1])

        return ActOption_Thresh(fraction)
