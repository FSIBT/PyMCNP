import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SsrOption_Bcw(_option.SsrOption_, keyword='bcw'):
    """
    Represents INP data card data option bcw options.

    Attributes:
        radius: Radius of cylindrical window.
        zb: Bottom of cylindrical window.
        ze: Top of cylindrical window.
    """

    _REGEX = re.compile(r'\Abcw( \S+)( \S+)( \S+)\Z')

    def __init__(self, radius: types.Real, zb: types.Real, ze: types.Real):
        """
        Initializes ``SsrOption_Bcw``.

        Parameters:
            radius: Radius of cylindrical window.
            zb: Bottom of cylindrical window.
            ze: Top of cylindrical window.

        Returns:
            ``SsrOption_Bcw``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if radius is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, radius)
        if zb is None or not (0 < zb):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zb)
        if ze is None or not (0 < zb < ze):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ze)

        self.value: typing.Final[tuple[any]] = types._Tuple([radius, zb, ze])
        self.radius: typing.Final[types.Real] = radius
        self.zb: typing.Final[types.Real] = zb
        self.ze: typing.Final[types.Real] = ze

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SsrOption_Bcw`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SsrOption_Bcw``.

        Raises:
            InpError: SYNTAX_SSR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SsrOption_Bcw._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        radius = types.Real.from_mcnp(tokens[1])
        zb = types.Real.from_mcnp(tokens[2])
        ze = types.Real.from_mcnp(tokens[3])

        return SsrOption_Bcw(radius, zb, ze)
