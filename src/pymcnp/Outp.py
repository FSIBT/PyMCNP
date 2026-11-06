import typing

import pandas

from . import abc
from . import outp


class Outp(abc.File):
    """
    Represents output files.

    Attributes:
        header: outp header.
        blocks: outp blocks.
        footer: outp footer.
    """

    header: outp.Header
    blocks: typing.Annotated[abc.Array, outp.Block, abc.Terminal[r'']]
    footer: outp.Footer

    @property
    def version(self) -> str:
        """
        outp version.
        """

        return self.header.version

    @property
    def nps(self) -> str:
        """
        outp nps.
        """

        return self.footer.nps

    @property
    def run_time(self) -> str:
        """
        outp run_time.
        """

        return self.footer.run_time

    @property
    def terminated(self) -> str:
        """
        outp terminated.
        """

        return self.footer.terminated

    @property
    def warnings(self) -> str:
        """
        outp warnings.
        """

        return self.footer.warnings

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes from output files.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        tallies = self.blocks.filter(outp.block.Tally)

        if not tallies:
            return pandas.DataFrame()
        else:
            return pandas.concat((tally.to_dataframe() for tally in tallies), ignore_index=True)

    def to_dataframe_iter(self) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame]:
        """
        Generates pandas dataframes from output files iteratively.

        Yields:
            Pandas dataframes concatenated into the returned dataframe.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        tallies = self.blocks.filter(outp.block.Tally)

        if not tallies:
            return pandas.DataFrame()

        frames = []
        for tally in tallies:
            frame = tally.to_dataframe()
            yield frame
            frames.append(frame)

        return pandas.concat(frames, ignore_index=True)
