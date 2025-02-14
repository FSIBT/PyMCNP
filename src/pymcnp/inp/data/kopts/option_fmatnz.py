import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Fmatnz(_option.KoptsOption_, keyword='fmatnz'):
    """
    Represents INP data card data option fmatnz options.

    Attributes:
        fmat_nz: fmat_nz.
    """

    _REGEX = re.compile(r'\Afmatnz( \S+)\Z')

    def __init__(self, fmat_nz: types.Real):
        """
        Initializes ``KoptsOption_Fmatnz``.

        Parameters:
            fmat_nz: fmat_nz.

        Returns:
            ``KoptsOption_Fmatnz``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if fmat_nz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, fmat_nz)

        self.value: typing.Final[tuple[any]] = types._Tuple([fmat_nz])
        self.fmat_nz: typing.Final[types.Real] = fmat_nz

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsOption_Fmatnz`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Fmatnz``.

        Raises:
            McnpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Fmatnz._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KOPTS_OPTION, source)

        fmat_nz = types.Real.from_mcnp(tokens[1])

        return KoptsOption_Fmatnz(fmat_nz)
