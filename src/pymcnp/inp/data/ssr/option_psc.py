import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SsrOption_Psc(_option.SsrOption_, keyword='psc'):
    """
    Represents INP data card data option psc options.

    Attributes:
        constant: Constant for approximation in PSC evaluation.
    """

    _REGEX = re.compile(r'\Apsc( \S+)\Z')

    def __init__(self, constant: types.Real):
        """
        Initializes ``SsrOption_Psc``.

        Parameters:
            constant: Constant for approximation in PSC evaluation.

        Returns:
            ``SsrOption_Psc``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if constant is None or not (constant >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, constant)

        self.value: typing.Final[tuple[any]] = types._Tuple([constant])
        self.constant: typing.Final[types.Real] = constant

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SsrOption_Psc`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SsrOption_Psc``.

        Raises:
            McnpError: SYNTAX_SSR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SsrOption_Psc._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_SSR_OPTION, source)

        constant = types.Real.from_mcnp(tokens[1])

        return SsrOption_Psc(constant)
