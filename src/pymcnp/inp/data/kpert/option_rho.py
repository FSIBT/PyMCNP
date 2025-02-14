import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class KpertOption_Rho(_option.KpertOption_, keyword='rho'):
    """
    Represents INP data card data option rho options.

    Attributes:
        densities: List of densities.
    """

    _REGEX = re.compile(r'\Arho(( \S+)+)\Z')

    def __init__(self, densities: tuple[types.Zaid]):
        """
        Initializes ``KpertOption_Rho``.

        Parameters:
            densities: List of densities.

        Returns:
            ``KpertOption_Rho``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if densities is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, densities)

        self.value: typing.Final[tuple[any]] = types._Tuple([densities])
        self.densities: typing.Final[tuple[types.Zaid]] = densities

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KpertOption_Rho`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``KpertOption_Rho``.

        Raises:
            McnpError: SYNTAX_KPERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = KpertOption_Rho._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_KPERT_OPTION, source)

        densities = types._Tuple(
            [types.Zaid.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return KpertOption_Rho(densities)
