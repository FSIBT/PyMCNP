import re

from . import _option
from ... import types


class Print(_option.DataOption):
    """
    Represents INP print elements.
    """

    _KEYWORD = 'print'

    _ATTRS = {
        'tables': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(rf'\Aprint((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z')

    def __init__(self, tables: list[str] | list[int] | list[types.Integer] = None):
        """
        Initializes ``Print``.

        Parameters:
            tables: Tables to print.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.tables: types.Tuple(types.Integer) = tables

    @property
    def tables(self) -> types.Tuple(types.Integer):
        """
        Tables to print

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._tables

    @tables.setter
    def tables(self, tables: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets ``tables``.

        Parameters:
            tables: Tables to print.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if tables is not None:
            array = []
            for item in tables:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            tables = types.Tuple(types.Integer)(array)

        self._tables: types.Tuple(types.Integer) = tables
