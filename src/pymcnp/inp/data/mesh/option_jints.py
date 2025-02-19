import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MeshOption_Jints(_option.MeshOption_, keyword='jints'):
    """
    Represents INP data card data option jints options.

    Attributes:
        number: Number of fine meshes within corresponding coarse meshes in the y/z directions.
    """

    _REGEX = re.compile(r'\Ajints( \S+)\Z')

    def __init__(self, number: types.Integer):
        """
        Initializes ``MeshOption_Jints``.

        Parameters:
            number: Number of fine meshes within corresponding coarse meshes in the y/z directions.

        Returns:
            ``MeshOption_Jints``.

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
        Generates ``MeshOption_Jints`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MeshOption_Jints``.

        Raises:
            InpError: SYNTAX_MESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MeshOption_Jints._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        number = types.Integer.from_mcnp(tokens[1])

        return MeshOption_Jints(number)
