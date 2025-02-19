import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class PertOption_Rho(_option.PertOption_, keyword='rho'):
    """
    Represents INP data card data option rho options.

    Attributes:
        density: Perturbed density.
    """

    _REGEX = re.compile(r'\Arho( \S+)\Z')

    def __init__(self, density: types.Real):
        """
        Initializes ``PertOption_Rho``.

        Parameters:
            density: Perturbed density.

        Returns:
            ``PertOption_Rho``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if density is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, density)

        self.value: typing.Final[tuple[any]] = types._Tuple([density])
        self.density: typing.Final[types.Real] = density

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PertOption_Rho`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``PertOption_Rho``.

        Raises:
            InpError: SYNTAX_PERT_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PertOption_Rho._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        density = types.Real.from_mcnp(tokens[1])

        return PertOption_Rho(density)
