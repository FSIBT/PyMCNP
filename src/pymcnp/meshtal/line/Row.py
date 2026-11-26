import re
import typing

import pandas

from ... import abc
from ..Line import Line


class Row(Line, abc.symbol.WithDataIter):
    """
    Represents data rows.

    Attributes:
        indent: data row leading spaces.
        values: data row values, i.e., optional energy and time bins, x, y, z, result, and relative error.
    """

    indent: typing.Annotated[abc.Terminal, r' *']
    values: typing.Annotated[
        abc.Array,
        typing.Annotated[abc.Terminal, r'Total|[-+]?(?:\d+\.?\d*|\.\d+)(?:E[-+]?\d+)?|[-+]?(?:NaN|Inf(?:inity)?)'],
        typing.Annotated[abc.Terminal, r' +'],
    ]

    def __post_init__(self) -> None:
        """
        Validates data rows.

        Raises:
            Error: Invalid value.
        """

        if not 5 <= len(self.values) <= 7:
            raise abc.Error('Invalid value.', f'{self.values=}')

    @classmethod
    def _from_mcnp_at(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        """
        Compiles source strings at positions into their corresponding data rows.

        Rows are matched with one regular expression, which is much faster than the generic parser for files with many rows.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.

        Returns:
            Data row corresponding to ``source`` at ``pos`` and the position where it ends.

        Raises:
            Error: Expected data row.
            Error: Invalid value.
        """

        match = _ROW.match(source, pos)
        if match is None:
            raise abc.Error('Expected ``Row``.', f'source[:200]={source[pos : pos + 200]!r}')

        parts = _SPACES.split(match[2])
        values = _VALUES(
            *(str.__new__(_VALUE_TERMINAL, value) for value in parts[0::2]),
            spaces=[str.__new__(_SPACE_TERMINAL, space) for space in parts[1::2]],
        )

        row = object.__new__(cls)
        object.__setattr__(row, '_indent', str.__new__(_INDENT_TERMINAL, match[1]))
        object.__setattr__(row, '_values', values)
        row.spaces = {}
        row.__post_init__()

        return row, match.end()

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for values.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for values.

        Returns:
            Pandas dataframe for all values.
        """

        yield (frame := pandas.DataFrame([[value if value == 'Total' else float(value) for value in self.values]]))

        if returning:
            return frame


_VALUE = r'(?:Total|[-+]?(?:\d+\.?\d*|\.\d+)(?:E[-+]?\d+)?|[-+]?(?:NaN|Inf(?:inity)?))'
_ROW = re.compile(rf'( *)({_VALUE}(?: +{_VALUE})*)', re.IGNORECASE)
_SPACES = re.compile(r'( +)')
_VALUE_TERMINAL = abc.Terminal[r'Total|[-+]?(?:\d+\.?\d*|\.\d+)(?:E[-+]?\d+)?|[-+]?(?:NaN|Inf(?:inity)?)']
_SPACE_TERMINAL = abc.Terminal[r' +']
_INDENT_TERMINAL = abc.Terminal[r' *']
_VALUES = abc.Array[_VALUE_TERMINAL, _SPACE_TERMINAL]
