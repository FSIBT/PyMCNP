import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MeshOption_Ref(_option.MeshOption_, keyword='ref'):
    """
    Represents INP data card data option ref options.

    Attributes:
        point: Mesh reference point.
    """

    _REGEX = re.compile(r'\Aref(( \S+)+)\Z')

    def __init__(self, point: tuple[types.Real]):
        """
        Initializes ``MeshOption_Ref``.

        Parameters:
            point: Mesh reference point.

        Returns:
            ``MeshOption_Ref``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if point is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, point)

        self.value: typing.Final[tuple[any]] = types._Tuple([point])
        self.point: typing.Final[tuple[types.Real]] = point

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MeshOption_Ref`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MeshOption_Ref``.

        Raises:
            InpError: SYNTAX_MESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MeshOption_Ref._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        point = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return MeshOption_Ref(point)
