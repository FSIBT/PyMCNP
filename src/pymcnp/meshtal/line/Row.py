import typing

from ... import abc
from ..Line import Line


class Row(Line):
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
