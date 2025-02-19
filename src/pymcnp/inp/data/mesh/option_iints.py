import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MeshOption_Iints(_option.MeshOption_, keyword='iints'):
    """
    Represents INP data card data option iints options.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the x/r directions.
    """

    _REGEX = re.compile(r'\Aiints( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``MeshOption_Iints``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the x/r directions.

        Returns:
            ``MeshOption_Iints``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if number is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, number)

        self.value: typing.Final[tuple[any]] = types._Tuple([number])
        self.number: typing.Final[types.Integer] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MeshOption_Iints`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MeshOption_Iints``.

        Raises:
            InpError: SYNTAX_MESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MeshOption_Iints._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return MeshOption_Iints(number)
