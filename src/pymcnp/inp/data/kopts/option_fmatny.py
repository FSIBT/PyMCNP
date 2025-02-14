import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Fmatny(_option.KoptsOption_, keyword='fmatny'):
    """
    Represents INP data card data option fmatny options.

    Attributes:
        fmat_ny: fmat_ny.
    """

    _REGEX = re.compile(r'\Afmatny( \S+)\Z')

    def __init__(self, fmat_ny: types.Real):
        """
        Initializes ``KoptsOption_Fmatny``.

        Parameters:
            fmat_ny: fmat_ny.

        Returns:
            ``KoptsOption_Fmatny``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if fmat_ny is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, fmat_ny)

        self.value: typing.Final[tuple[any]] = types._Tuple([fmat_ny])
        self.fmat_ny: typing.Final[types.Real] = fmat_ny

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsOption_Fmatny`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Fmatny``.

        Raises:
            McnpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Fmatny._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KOPTS_OPTION, source)

        fmat_ny = types.Real.from_mcnp(tokens[1])

        return KoptsOption_Fmatny(fmat_ny)
