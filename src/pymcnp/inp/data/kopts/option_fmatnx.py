import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KoptsOption_Fmatnx(_option.KoptsOption_, keyword='fmatnx'):
    """
    Represents INP data card data option fmatnx options.

    Attributes:
        fmat_nx: fmat_nx.
    """

    _REGEX = re.compile(r'\Afmatnx( \S+)\Z')

    def __init__(self, fmat_nx: types.Real):
        """
        Initializes ``KoptsOption_Fmatnx``.

        Parameters:
            fmat_nx: fmat_nx.

        Returns:
            ``KoptsOption_Fmatnx``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fmat_nx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fmat_nx)

        self.value: typing.Final[tuple[any]] = types._Tuple([fmat_nx])
        self.fmat_nx: typing.Final[types.Real] = fmat_nx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsOption_Fmatnx`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KoptsOption_Fmatnx``.

        Raises:
            InpError: SYNTAX_KOPTS_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KoptsOption_Fmatnx._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        fmat_nx = types.Real.from_mcnp(tokens[1])

        return KoptsOption_Fmatnx(fmat_nx)
