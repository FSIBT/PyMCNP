import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types


class Print(_option.DataOption):
    """
    Represents INP print elements.

    Attributes:
        tables: Tables to print.
    """

    _KEYWORD = 'print'

    _ATTRS = {
        'tables': types.Tuple[types.Integer],
    }

    _REGEX = re.compile(rf'\Aprint((?: {types.Integer._REGEX.pattern[2:-2]})+?)?\Z')

    def __init__(self, tables: types.Tuple[types.Integer] = None):
        """
        Initializes ``Print``.

        Parameters:
            tables: Tables to print.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                tables,
            ]
        )

        self.tables: typing.Final[types.Tuple[types.Integer]] = tables


@dataclasses.dataclass
class PrintBuilder(_option.DataOptionBuilder):
    """
    Builds ``Print``.

    Attributes:
        tables: Tables to print.
    """

    tables: list[str] | list[int] | list[types.Integer] = None

    def build(self):
        """
        Builds ``PrintBuilder`` into ``Print``.

        Returns:
            ``Print`` for ``PrintBuilder``.
        """

        if self.tables:
            tables = []
            for item in self.tables:
                if isinstance(item, types.Integer):
                    tables.append(item)
                elif isinstance(item, int):
                    tables.append(types.Integer(item))
                elif isinstance(item, str):
                    tables.append(types.Integer.from_mcnp(item))
            tables = types.Tuple(tables)
        else:
            tables = None

        return Print(
            tables=tables,
        )

    @staticmethod
    def unbuild(ast: Print):
        """
        Unbuilds ``Print`` into ``PrintBuilder``

        Returns:
            ``PrintBuilder`` for ``Print``.
        """

        return PrintBuilder(
            tables=copy.deepcopy(ast.tables),
        )
