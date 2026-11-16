import abc
import typing

import pandas


class WithDataIter(abc.ABC):
    """
    Represents symbols with iterative dataframe writers.
    """

    @abc.abstractmethod
    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for repeated subsymbols.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for repeated subsymbols.

        Returns:
            Pandas dataframe for all repeated subsymbols.
        """

        raise NotImplementedError

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes for repeated subsymbols.

        Returns:
            Pandas dataframe for all repeated subsymbols.
        """

        generator = self.to_dataframe_iter(returning=True)
        try:
            while True:
                next(generator)
        except StopIteration as stop:
            assert stop.value is not None
            return stop.value
