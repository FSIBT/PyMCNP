import re
import typing

from . import _option
from ....utils import types
from ....utils import errors
from ....utils import _parser


class MeshOption_Vec(_option.MeshOption_, keyword='vec'):
    """
    Represents INP data card data option vec options.

    Attributes:
        vector: Vector giving the direction of the polar axis.
    """

    _REGEX = re.compile(r'\Avec(( \S+)+)\Z')

    def __init__(self, vector: tuple[types.Real]):
        """
        Initializes ``MeshOption_Vec``.

        Parameters:
            vector: Vector giving the direction of the polar axis.

        Returns:
            ``MeshOption_Vec``.

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
        Generates ``MeshOption_Vec`` from INP.

        Parameters:
            source: INP data card data option option.

        Returns:
            ``MeshOption_Vec``.

        Raises:
            InpError: SYNTAX_MESH_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = MeshOption_Vec._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        vector = types._Tuple(
            [types.Real.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )

        return MeshOption_Vec(vector)
