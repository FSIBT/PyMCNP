import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Emesh(_option.FmeshOption_, keyword='emesh'):
    """
    Represents INP data card data option emesh options.

    Attributes:
        energy: Values of mesh points in energy.
    """

    _REGEX = re.compile(r'\Aemesh( \S+)\Z')

    def __init__(self, energy: types.Real):
        """
        Initializes ``FmeshOption_Emesh``.

        Parameters:
            energy: Values of mesh points in energy.

        Returns:
            ``FmeshOption_Emesh``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if energy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, energy)

        self.value: typing.Final[tuple[any]] = types._Tuple([energy])
        self.energy: typing.Final[types.Real] = energy

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Emesh`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Emesh``.

        Raises:
            InpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Emesh._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        energy = types.Real.from_mcnp(tokens[1])

        return FmeshOption_Emesh(energy)
