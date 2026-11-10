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
        footer: outp footer, empty if MCNP stopped early, e.g., with ``bad trouble``.
    """

    header: outp.Header
    blocks: typing.Annotated[abc.Array, outp.Block, abc.Terminal[r'']]
    footer: outp.Footer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    @property
    def version(self) -> str:
        """
        outp version.
        """

        return self.header.version

    @property
    def nps(self) -> str | None:
        """
        outp nps, ``None`` without footer.
        """

        return self.footer.nps if isinstance(self.footer, outp.Footer) else None

    @property
    def run_time(self) -> str | None:
        """
        outp run_time, ``None`` without footer.
        """

        return self.footer.run_time if isinstance(self.footer, outp.Footer) else None

    @property
    def terminated(self) -> str | None:
        """
        outp terminated, ``None`` without footer.
        """

        return self.footer.terminated if isinstance(self.footer, outp.Footer) else None

    @property
    def warnings(self) -> str | None:
        """
        outp warnings, ``None`` without footer.
        """

        return self.footer.warnings if isinstance(self.footer, outp.Footer) else None

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
