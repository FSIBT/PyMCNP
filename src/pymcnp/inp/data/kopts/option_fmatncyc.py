import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Fmatncyc(_option.KoptsOption_, keyword='fmatncyc'):
    """
    Represents INP data card data option fmatncyc options.

    Attributes:
        fmat_ncyc: fmat_ncyc.
    """

    _REGEX = re.compile(r'\Afmatncyc( \S+)\Z')

    def __init__(self, fmat_ncyc: types.Real):
        """
        Initializes ``KoptsOption_Fmatncyc``.

        Parameters:
            fmat_ncyc: fmat_ncyc.

        Returns:
            ``KoptsOption_Fmatncyc``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_ncyc is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_ncyc)

        self.value: typing.Final[tuple[any]] = types._Tuple([fmat_ncyc])
        self.fmat_ncyc: typing.Final[types.Real] = fmat_ncyc

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsOption_Fmatncyc`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Fmatncyc``.

        Raises:
            InpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Fmatncyc._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        fmat_ncyc = types.Real.from_mcnp(tokens[1])

        return KoptsOption_Fmatncyc(fmat_ncyc)
