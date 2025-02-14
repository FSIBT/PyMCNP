import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MeshOption_Origin(_option.MeshOption_, keyword='origin'):
    """
    Represents INP data card data option origin options.

    Attributes:
        point: Mesh origin point.
    """

    _REGEX = re.compile(r'\Aorigin(( \S+)+)\Z')

    def __init__(self, point: tuple[types.Real]):
        """
        Initializes ``MeshOption_Origin``.

        Parameters:
            point: Mesh origin point.

        Returns:
            ``MeshOption_Origin``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        if point is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, point)

        self.value: typing.Final[tuple[any]] = types._Tuple([point])
        self.point: typing.Final[tuple[types.Real]] = point

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MeshOption_Origin`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MeshOption_Origin``.

        Raises:
            McnpError: SYNTAX_MESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MeshOption_Origin._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_MESH_OPTION, source)

        point = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return MeshOption_Origin(point)
