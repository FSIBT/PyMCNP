import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Fmatskpt(_option.KoptsOption_, keyword='fmatskpt'):
    """
    Represents INP data card data option fmatskpt options.

    Attributes:
        fmat_skip: fmat_skip.
    """

    _REGEX = re.compile(r'\Afmatskpt( \S+)\Z')

    def __init__(self, fmat_skip: types.Real):
        """
        Initializes ``KoptsOption_Fmatskpt``.

        Parameters:
            fmat_skip: fmat_skip.

        Returns:
            ``KoptsOption_Fmatskpt``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if fmat_skip is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, fmat_skip)

        self.value: typing.Final[tuple[any]] = types._Tuple([fmat_skip])
        self.fmat_skip: typing.Final[types.Real] = fmat_skip

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsOption_Fmatskpt`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Fmatskpt``.

        Raises:
            McnpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Fmatskpt._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KOPTS_OPTION, source)

        fmat_skip = types.Real.from_mcnp(tokens[1])

        return KoptsOption_Fmatskpt(fmat_skip)
