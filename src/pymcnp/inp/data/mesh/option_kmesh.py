import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MeshOption_Kmesh(_option.MeshOption_, keyword='kmesh'):
    """
    Represents INP data card data option kmesh options.

    Attributes:
        vector: Locations of the coarse meshes in the z/theta directions.
    """

    _REGEX = re.compile(r'\Akmesh(( \S+)+)\Z')

    def __init__(self, vector: tuple[types.Real]):
        """
        Initializes ``MeshOption_Kmesh``.

        Parameters:
            vector: Locations of the coarse meshes in the z/theta directions.

        Returns:
            ``MeshOption_Kmesh``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, vector)

        self.value: typing.Final[tuple[any]] = types._Tuple([vector])
        self.vector: typing.Final[tuple[types.Real]] = vector

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MeshOption_Kmesh`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MeshOption_Kmesh``.

        Raises:
            McnpError: SYNTAX_MESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MeshOption_Kmesh._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_MESH_OPTION, source)

        vector = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return MeshOption_Kmesh(vector)
