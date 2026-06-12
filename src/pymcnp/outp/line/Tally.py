import typing
import dataclasses

import pandas

from ... import abc
from ..Line import Line


class Tally(Line):
    """
    Represents tally lines.

    Attributes:
        bin: line bin.
        count: line count.
        error: line error.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    bin: typing.Annotated[abc.Terminal, r'    \S+']
    count: typing.Annotated[abc.Terminal, r'   \S+']
    error: typing.Annotated[abc.Terminal, r' \S+']

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes for tally lines.

        Returns:
            Corresonding pandas dataframe for `self`.
        """

        return pandas.DataFrame(
            {
                'bins': [float(self.bin)],
                'counts': [float(self.count)],
                'errors': [float(self.error)],
            }
        )
