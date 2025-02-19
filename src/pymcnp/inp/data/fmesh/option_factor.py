import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Factor(_option.FmeshOption_, keyword='factor'):
    """
    Represents INP data card data option factor options.

    Attributes:
        multiple: Multiplicative factor for each mesh.
    """

    _REGEX = re.compile(r'\Afactor( \S+)\Z')

    def __init__(self, multiple: types.Real):
        """
        Initializes ``FmeshOption_Factor``.

        Parameters:
            multiple: Multiplicative factor for each mesh.

        Returns:
            ``FmeshOption_Factor``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if multiple is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, multiple)

        self.value: typing.Final[tuple[any]] = types._Tuple([multiple])
        self.multiple: typing.Final[types.Real] = multiple

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Factor`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Factor``.

        Raises:
            InpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Factor._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        multiple = types.Real.from_mcnp(tokens[1])

        return FmeshOption_Factor(multiple)
