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
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into their corresponding data rows.

        Rows are matched with one regular expression, which is much faster than the generic parser for files with many rows.

        Parameters:
            source: Source string to compile.

        Returns:
            Data row corresponding to ``source``.

        Raises:
            Error: Expected data row.
            Error: Invalid value.
        """

        match = _ROW.match(source)
        if match is None:
            raise abc.Error('Expected ``Row``.', f'{source[:200]=}')

        parts = _SPACES.split(match[2])
        values = abc.Array[abc.Terminal[r'Total|[-+]?(?:\d+\.?\d*|\.\d+)(?:E[-+]?\d+)?|[-+]?(?:NaN|Inf(?:inity)?)'], abc.Terminal[r' +']](
            *(str.__new__(abc.Terminal[r'Total|[-+]?(?:\d+\.?\d*|\.\d+)(?:E[-+]?\d+)?|[-+]?(?:NaN|Inf(?:inity)?)'], value) for value in parts[0::2]),
            spaces=[str.__new__(abc.Terminal[r' +'], space) for space in parts[1::2]],
        )

        row = object.__new__(cls)
        object.__setattr__(row, '_indent', str.__new__(abc.Terminal[r' *'], match[1]))
        object.__setattr__(row, '_values', values)
        row.spaces = {}
        row.__post_init__()

        return row, source[match.end() :]

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
