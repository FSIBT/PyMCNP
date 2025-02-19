import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SsrOption_Poa(_option.SsrOption_, keyword='poa'):
    """
    Represents INP data card data option poa options.

    Attributes:
        angle: Angle within which particles accepeted for transport.
    """

    _REGEX = re.compile(r'\Apoa( \S+)\Z')

    def __init__(self, angle: types.Real):
        """
        Initializes ``SsrOption_Poa``.

        Parameters:
            angle: Angle within which particles accepeted for transport.

        Returns:
            ``SsrOption_Poa``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if angle is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, angle)

        self.value: typing.Final[tuple[any]] = types._Tuple([angle])
        self.angle: typing.Final[types.Real] = angle

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SsrOption_Poa`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SsrOption_Poa``.

        Raises:
            InpError: SYNTAX_SSR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SsrOption_Poa._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        angle = types.Real.from_mcnp(tokens[1])

        return SsrOption_Poa(angle)
