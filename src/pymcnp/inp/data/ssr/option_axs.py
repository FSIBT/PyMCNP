import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class SsrOption_Axs(_option.SsrOption_, keyword='axs'):
    """
    Represents INP data card data option axs options.

    Attributes:
        cosines: Direction cosines defining.
    """

    _REGEX = re.compile(r'\Aaxs(( \S+)+)\Z')

    def __init__(self, cosines: tuple[types.Real]):
        """
        Initializes ``SsrOption_Axs``.

        Parameters:
            cosines: Direction cosines defining.

        Returns:
            ``SsrOption_Axs``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if cosines is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cosines)

        self.value: typing.Final[tuple[any]] = types._Tuple([cosines])
        self.cosines: typing.Final[tuple[types.Real]] = cosines

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SsrOption_Axs`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``SsrOption_Axs``.

        Raises:
            InpError: SYNTAX_SSR_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = SsrOption_Axs._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        cosines = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return SsrOption_Axs(cosines)
