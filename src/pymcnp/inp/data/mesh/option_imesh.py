import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MeshOption_Imesh(_option.MeshOption_, keyword='imesh'):
    """
    Represents INP data card data option imesh options.

    Attributes:
        vector: Locations of the coarse meshes in the x/r directions.
    """

    _REGEX = re.compile(r'\Aimesh(( \S+)+)\Z')

    def __init__(self, vector: tuple[types.Real]):
        """
        Initializes ``MeshOption_Imesh``.

        Parameters:
            vector: Locations of the coarse meshes in the x/r directions.

        Returns:
            ``MeshOption_Imesh``.

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
        Generates ``MeshOption_Imesh`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MeshOption_Imesh``.

        Raises:
            InpError: SYNTAX_MESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MeshOption_Imesh._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        vector = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return MeshOption_Imesh(vector)
