import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class EmbeeOption_Factor(_option.EmbeeOption_, keyword='factor'):
    """
    Represents INP data card data option factor options.

    Attributes:
        constant: Multiplicative constant.
    """

    _REGEX = re.compile(r'\Afactor( \S+)\Z')

    def __init__(self, constant: types.Real):
        """
        Initializes ``EmbeeOption_Factor``.

        Parameters:
            constant: Multiplicative constant.

        Returns:
            ``EmbeeOption_Factor``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if constant is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, constant)

        self.value: typing.Final[tuple[any]] = types._Tuple([constant])
        self.constant: typing.Final[types.Real] = constant

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeeOption_Factor`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``EmbeeOption_Factor``.

        Raises:
            InpError: SYNTAX_EMBEE_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = EmbeeOption_Factor._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        constant = types.Real.from_mcnp(tokens[1])

        return EmbeeOption_Factor(constant)
