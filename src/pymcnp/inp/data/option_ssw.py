import re
import typing

from . import ssw
from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Ssw(_option.DataOption_, keyword='ssw'):
    """
    Represents INP data card ssw options.

    Attributes:
        surfaces: Problem surfaces.
        cells: Problem cells.
        options: Dictionary of options.
    """

    _REGEX = re.compile(
        r'\Assw(( \S+)+)(( \S+)+)(( (((sym)( \S+))|((pty)(( \S+)+))|((cel)(( \S+)+))))+)?\Z'
    )

    def __init__(
        self,
        surfaces: tuple[types.Integer],
        cells: tuple[types.Integer],
        options: tuple[ssw.SswOption_] = None,
    ):
        """
        Initializes ``DataOption_Ssw``.

        Parameters:
            surfaces: Problem surfaces.
            cells: Problem cells.
            options: Dictionary of options.

        Returns:
            ``DataOption_Ssw``.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if surfaces is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, surfaces)
        if cells is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cells)

        self.value: typing.Final[tuple[any]] = types._Tuple([surfaces, cells, options])
        self.surfaces: typing.Final[tuple[types.Integer]] = surfaces
        self.cells: typing.Final[tuple[types.Integer]] = cells
        self.options: typing.Final[dict[str, ssw.SswOption_]] = (
            {val._KEYWORD: val for val in options} if options else None
        )

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Ssw`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Ssw``.

        Raises:
            InpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Ssw._REGEX.match(source)

        if not tokens:
            raise errors.InpError(errors.InpCode.SYNTAX_OPTION, source)

        surfaces = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[1])]
        )
        cells = types._Tuple(
            [types.Integer.from_mcnp(token[0]) for token in re.finditer(r'( \S+)', tokens[2])]
        )
        options = (
            types._Tuple(tuple(_parser.process_inp_option(ssw.SswOption_, tokens[3])))
            if tokens[3]
            else None
        )

        return DataOption_Ssw(surfaces, cells, options)
