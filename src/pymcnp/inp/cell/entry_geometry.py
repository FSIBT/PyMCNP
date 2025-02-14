import re
import typing


from . import _entry
from ...utils import types
from ...utils import errors
from ...utils import _parser


class CellEntry_Geometry(_entry.CellEntry_):
    """
    Represents INP cell card geometry entries.

    Attributes:
            infix: Cell geometry infix formula.
    """

    _REGEX = re.compile(r'((?:).+)')

    def __init__(self, infix: types.String):
        """
        Initializes ``CellEntry_Geometry``.

        Parameters:
                infix: Cell geometry infix formula.

        Returns:
                ``CellEntryGeometry``.

        Raises:
                McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        temp = re.sub(r' 0+', '', infix)
        temp = re.sub(r' +', '*', temp)
        temp = re.sub(r' ?([()]) ?', r'\1', temp)
        temp = re.sub(r' ?: ?', '+', temp)
        temp = re.sub(r'#', '-', temp)

        try:
            eval(temp)
        except SyntaxError:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_CELL_ENTRY_PARAMETER, infix)

        self.parameters: typing.Final[tuple[any]] = tuple([infix])
        self.infix: typing.typing.Final[types.String] = infix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``CellEntry_Geometry`` from INP.

        Parameters:
                INP for ``CellEntry_Geometry``.

        Returns:
                ``CellEntry_Geometry``.

        Raises:
                McnpError: SYNTAX_CELL_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = CellEntry_Geometry._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_CELL_ENTRY, source)

        infix = types.String.from_mcnp(tokens[1])

        return CellEntry_Geometry(infix)
