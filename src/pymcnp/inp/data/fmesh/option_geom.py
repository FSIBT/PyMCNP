import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class FmeshOption_Geom(_option.FmeshOption_, keyword='geom'):
    """
    Represents INP data card data option geom options.

    Attributes:
        geometry: Mesh geometry.
    """

    _REGEX = re.compile(r'\Ageom( \S+)\Z')

    def __init__(self, geometry: types.String):
        """
        Initializes ``FmeshOption_Geom``.

        Parameters:
            geometry: Mesh geometry.

        Returns:
            ``FmeshOption_Geom``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if geometry is None or geometry not in {'xyz', 'rec', 'rzt', 'cyl'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, geometry)

        self.value: typing.Final[tuple[any]] = types._Tuple([geometry])
        self.geometry: typing.Final[types.String] = geometry

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmeshOption_Geom`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``FmeshOption_Geom``.

        Raises:
            McnpError: SYNTAX_FMESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = FmeshOption_Geom._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_FMESH_OPTION, source)

        geometry = types.String.from_mcnp(tokens[1])

        return FmeshOption_Geom(geometry)
