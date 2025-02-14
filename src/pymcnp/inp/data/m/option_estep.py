import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Estep(_option.MOption_, keyword='estep'):
    """
    Represents INP data card data option estep options.

    Attributes:
        step: Number of electron sub-step per energy step.
    """

    _REGEX = re.compile(r'\Aestep( \S+)\Z')

    def __init__(self, step: types.Integer):
        """
        Initializes ``MOption_Estep``.

        Parameters:
            step: Number of electron sub-step per energy step.

        Returns:
            ``MOption_Estep``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if step is None or not (step >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, step)

        self.value: typing.Final[tuple[any]] = types._Tuple([step])
        self.step: typing.Final[types.Integer] = step

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MOption_Estep`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Estep``.

        Raises:
            McnpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Estep._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_M_OPTION, source)

        step = types.Integer.from_mcnp(tokens[1])

        return MOption_Estep(step)
