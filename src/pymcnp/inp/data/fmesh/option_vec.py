import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Vec(_option.FmeshOption_, keyword='vec'):
    """
    Represents INP data card data option vec options.

    Attributes:
        x: Plane vector x component.
        y: Plane vector y component.
        z: Plane vector z component.
    """

    _REGEX = re.compile(r'\Avec( \S+)( \S+)( \S+)\Z')

    def __init__(self, x: types.Real, y: types.Real, z: types.Real):
        """
        Initializes ``FmeshOption_Vec``.

        Parameters:
            x: Plane vector x component.
            y: Plane vector y component.
            z: Plane vector z component.

        Returns:
            ``FmeshOption_Vec``.

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
        Generates ``FmeshOption_Vec`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Vec``.

        Raises:
            InpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Vec._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        x = types.Real.from_mcnp(tokens[1])
        y = types.Real.from_mcnp(tokens[2])
        z = types.Real.from_mcnp(tokens[3])

        return FmeshOption_Vec(x, y, z)
