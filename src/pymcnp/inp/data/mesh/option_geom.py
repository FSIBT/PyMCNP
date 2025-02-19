import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MeshOption_Geom(_option.MeshOption_, keyword='geom'):
    """
    Represents INP data card data option geom options.

    Attributes:
        geometry: Controls mesh geometry type.
    """

    _REGEX = re.compile(r'\Ageom( \S+)\Z')

    def __init__(self, geometry: types.String):
        """
        Initializes ``MeshOption_Geom``.

        Parameters:
            geometry: Controls mesh geometry type.

        Returns:
            ``MeshOption_Geom``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if geometry is None or geometry not in {'xyz', 'rzt', 'rpt'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, geometry)

        self.value: typing.Final[tuple[any]] = types._Tuple([geometry])
        self.geometry: typing.Final[types.String] = geometry

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MeshOption_Geom`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MeshOption_Geom``.

        Raises:
            InpError: SYNTAX_MESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MeshOption_Geom._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        geometry = types.String.from_mcnp(tokens[1])

        return MeshOption_Geom(geometry)
