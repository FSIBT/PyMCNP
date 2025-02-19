import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MeshOption_Jmesh(_option.MeshOption_, keyword='jmesh'):
    """
    Represents INP data card data option jmesh options.

    Attributes:
        vector: Locations of the coarse meshes in the y/z directions.
    """

    _REGEX = re.compile(r'\Ajmesh(( \S+)+)\Z')

    def __init__(self, vector: tuple[types.Real]):
        """
        Initializes ``MeshOption_Jmesh``.

        Parameters:
            vector: Locations of the coarse meshes in the y/z directions.

        Returns:
            ``MeshOption_Jmesh``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if vector is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, vector)

        self.value: typing.Final[tuple[any]] = types._Tuple([vector])
        self.vector: typing.Final[tuple[types.Real]] = vector

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MeshOption_Jmesh`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MeshOption_Jmesh``.

        Raises:
            InpError: SYNTAX_MESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MeshOption_Jmesh._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        vector = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return MeshOption_Jmesh(vector)
