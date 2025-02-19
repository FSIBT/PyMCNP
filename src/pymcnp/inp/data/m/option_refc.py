import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MOption_Refc(_option.MOption_, keyword='refc'):
    """
    Represents INP data card data option refc options.

    Attributes:
        coefficents: Cauchy coefficents.
    """

    _REGEX = re.compile(r'\Arefc(( \S+)+)\Z')

    def __init__(self, coefficents: tuple[types.Real]):
        """
        Initializes ``MOption_Refc``.

        Parameters:
            coefficents: Cauchy coefficents.

        Returns:
            ``MOption_Refc``.

        Raises:
            InpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if coefficents is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_DATA_OPTION_VALUE, coefficents)

        self.value: typing.Final[tuple[any]] = types._Tuple([coefficents])
        self.coefficents: typing.Final[tuple[types.Real]] = coefficents

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MOption_Refc`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MOption_Refc``.

        Raises:
            InpError: SYNTAX_M_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MOption_Refc._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_M_OPTION, source)

        coefficents = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return MOption_Refc(coefficents)
