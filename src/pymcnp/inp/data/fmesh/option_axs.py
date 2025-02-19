import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Axs(_option.FmeshOption_, keyword='axs'):
    """
    Represents INP data card data option axs options.

    Attributes:
        x: Cylindrical mesh axis vector x component.
        y: Cylindrical mesh axis vector y component.
        z: Cylindrical mesh axis vector z component.
    """

    _REGEX = re.compile(r'\Aaxs( \S+)( \S+)( \S+)\Z')

    def __init__(self, x: types.Real, y: types.Real, z: types.Real):
        """
        Initializes ``FmeshOption_Axs``.

        Parameters:
            x: Cylindrical mesh axis vector x component.
            y: Cylindrical mesh axis vector y component.
            z: Cylindrical mesh axis vector z component.

        Returns:
            ``FmeshOption_Axs``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)

        self.value: typing.Final[tuple[any]] = types._Tuple([x, y, z])
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Axs`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Axs``.

        Raises:
            InpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Axs._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])

        return FmeshOption_Axs(x, y, z)
