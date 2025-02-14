import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbeeOption_Time(_option.EmbeeOption_, keyword='time'):
    """
    Represents INP data card data option time options.

    Attributes:
        factor: Multiplicative conversion factor for time-related output.
    """

    _REGEX = re.compile(r'\Atime( \S+)\Z')

    def __init__(self, factor: types.Real):
        """
        Initializes ``EmbeeOption_Time``.

        Parameters:
            factor: Multiplicative conversion factor for time-related output.

        Returns:
            ``EmbeeOption_Time``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if factor is None or not (factor > 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, factor)

        self.value: typing.Final[tuple[any]] = types._Tuple([factor])
        self.factor: typing.Final[types.Real] = factor

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeeOption_Time`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbeeOption_Time``.

        Raises:
            McnpError: SYNTAX_EMBEE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbeeOption_Time._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBEE_OPTION, source)

        factor = types.Real.from_mcnp(tokens[1])

        return EmbeeOption_Time(factor)
