import typing

import pandas

from ... import abc
from ..Line import Line


class Tally(Line, abc.symbol.WithDataIter):
    """
    Represents tally lines.

    Attributes:
        bin: line bin.
        count: line count.
        error: line error.
    """

    bin: typing.Annotated[abc.Terminal, r'    \S+']
    count: typing.Annotated[abc.Terminal, r'   \S+']
    error: typing.Annotated[abc.Terminal, r' \S+']

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for tally lines.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for tally lines.

        Returns:
            Pandas dataframe for all tally lines.
        """

        yield (
            frame := pandas.DataFrame(
                {
                    'bins': [float(self.bin)],
                    'counts': [float(self.count)],
                    'errors': [float(self.error)],
                }
            )
        )

        if returning:
            return frame
