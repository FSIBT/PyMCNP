import re
import typing

from . import mesh
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Mesh(_option.DataOption_, keyword='mesh'):
    """
    Represents INP data card mesh options.

    Attributes:
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Amesh(( (((geom)( \S+))|((ref)(( \S+)+))|((origin)(( \S+)+))|((axs)(( \S+)+))|((vec)(( \S+)+))|((imesh)(( \S+)+))|((iints)( \S+))|((jmesh)(( \S+)+))|((jints)( \S+))|((kmesh)(( \S+)+))|((kints)( \S+))))+)?\Z'
    )

    def __init__(self, options: tuple[mesh.MeshOption_] = None):
        """
        Initializes ``DataOption_Mesh``.

        Parameters:
            options: Dictionary of options.

        Returns:
            ``DataOption_Mesh``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
        """

        self.value: typing.Final[tuple[any]] = types._Tuple([options])
        self.options: typing.Final[dict[str, mesh.MeshOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Mesh`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Mesh``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Mesh._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        options = (
            types._Tuple(tuple(_parser.process_inp_option(mesh.MeshOption_, tokens[1])))
            if tokens[1]
            else None
        )

        return DataOption_Mesh(options)
