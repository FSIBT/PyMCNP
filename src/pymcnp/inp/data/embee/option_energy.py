import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbeeOption_Energy(_option.EmbeeOption_, keyword='energy'):
    """
    Represents INP data card data option energy options.

    Attributes:
        factor: Multiplicative conversion factor for energy-related output.
    """

    _REGEX = re.compile(r'\Aenergy( \S+)\Z')

    def __init__(self, factor: types.Real):
        """
        Initializes ``EmbeeOption_Energy``.

        Parameters:
            factor: Multiplicative conversion factor for energy-related output.

        Returns:
            ``EmbeeOption_Energy``.

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
        Generates ``EmbeeOption_Energy`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbeeOption_Energy``.

        Raises:
            McnpError: SYNTAX_EMBEE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbeeOption_Energy._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBEE_OPTION, source)

        factor = types.Real.from_mcnp(tokens[1])

        return EmbeeOption_Energy(factor)
