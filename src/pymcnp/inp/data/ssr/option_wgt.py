import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SsrOption_Wgt(_option.SsrOption_, keyword='wgt'):
    """
    Represents INP data card data option wgt options.

    Attributes:
        constant: Particle weight multiplier.
    """

    _REGEX = re.compile(r'\Awgt( \S+)\Z')

    def __init__(self, constant: types.Real):
        """
        Initializes ``SsrOption_Wgt``.

        Parameters:
            constant: Particle weight multiplier.

        Returns:
            ``SsrOption_Wgt``.

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
        Generates ``SsrOption_Wgt`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SsrOption_Wgt``.

        Raises:
            InpError: SYNTAX_SSR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SsrOption_Wgt._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        constant = types.Real.from_mcnp(tokens[1])

        return SsrOption_Wgt(constant)
