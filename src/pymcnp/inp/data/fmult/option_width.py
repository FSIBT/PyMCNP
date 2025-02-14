import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmultOption_Width(_option.FmultOption_, keyword='width'):
    """
    Represents INP data card data option width options.

    Attributes:
        width: Width for sampling spontaneous fission.
    """

    _REGEX = re.compile(r'\Awidth( \S+)\Z')

    def __init__(self, width: types.Real):
        """
        Initializes ``FmultOption_Width``.

        Parameters:
            width: Width for sampling spontaneous fission.

        Returns:
            ``FmultOption_Width``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if width is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, width)

        self.value: typing.Final[tuple[any]] = types._Tuple([width])
        self.width: typing.Final[types.Real] = width

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmultOption_Width`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmultOption_Width``.

        Raises:
            McnpError: SYNTAX_FMULT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmultOption_Width._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMULT_OPTION, source)

        width = types.Real.from_mcnp(tokens[1])

        return FmultOption_Width(width)
