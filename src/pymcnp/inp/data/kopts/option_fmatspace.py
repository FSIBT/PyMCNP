import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Fmatspace(_option.KoptsOption_, keyword='fmatspace'):
    """
    Represents INP data card data option fmatspace options.

    Attributes:
        fmat_space: fmat_space.
    """

    _REGEX = re.compile(r'\Afmatspace( \S+)\Z')

    def __init__(self, fmat_space: types.Real):
        """
        Initializes ``KoptsOption_Fmatspace``.

        Parameters:
            fmat_space: fmat_space.

        Returns:
            ``KoptsOption_Fmatspace``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_space is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_space)

        self.value: typing.Final[tuple[any]] = types._Tuple([fmat_space])
        self.fmat_space: typing.Final[types.Real] = fmat_space

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsOption_Fmatspace`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Fmatspace``.

        Raises:
            InpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Fmatspace._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        fmat_space = types.Real.from_mcnp(tokens[1])

        return KoptsOption_Fmatspace(fmat_space)
