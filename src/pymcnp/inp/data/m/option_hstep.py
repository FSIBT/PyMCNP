import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Hstep(_option.MOption_, keyword='hstep'):
    """
    Represents INP data card data option hstep options.

    Attributes:
        step: Number of proton sub-step per energy step.
    """

    _REGEX = re.compile(r'\Ahstep( \S+)\Z')

    def __init__(self, step: types.Integer):
        """
        Initializes ``MOption_Hstep``.

        Parameters:
            step: Number of proton sub-step per energy step.

        Returns:
            ``MOption_Hstep``.

        Raises:
            InpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if step is None or not (step >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_OPTION_VALUE, step)

        self.value: typing.Final[tuple[any]] = types._Tuple([step])
        self.step: typing.Final[types.Integer] = step

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MOption_Hstep`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Hstep``.

        Raises:
            InpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Hstep._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_M_OPTION, source)

        step = types.Integer.from_mcnp(tokens[1])

        return MOption_Hstep(step)
