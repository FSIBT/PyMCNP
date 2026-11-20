import typing

import pandas

from . import abc
from . import outp


class Outp(abc.file.WithDataIter, abc.File):
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
        Outp file version.
        """

        return self.header.version

    @property
    def nps(self) -> str | None:
        """
        Output file nps, ``None`` without footer.
        """

        return self.footer.nps if isinstance(self.footer, outp.Footer) else None

    @property
    def run_time(self) -> str | None:
        """
        Output file run time, ``None`` without footer.
        """

        return self.footer.run_time if isinstance(self.footer, outp.Footer) else None

    @property
    def terminated(self) -> str | None:
        """
        Output file terminated, ``None`` without footer.
        """

        return self.footer.terminated if isinstance(self.footer, outp.Footer) else None

    @property
    def warnings(self) -> str | None:
        """
        Output file warnings, ``None`` without footer.
        """

        return self.footer.warnings if isinstance(self.footer, outp.Footer) else None

    def activities(self, kind: type[outp.block.Activity] = outp.block.Activity) -> tuple[outp.block.Activity, ...]:
        """
        Gets output file activity blocks.

        Parameters:
            kind: Activity block type to get.

        Returns:
            Activity blocks of kind ``kind``.
        """

        every = self.blocks.filter(kind)

        return tuple(every)

    def tallies(self, number: abc.Terminal | str | None = None, kind: type[outp.block.Tally] = outp.block.Tally) -> tuple[outp.block.Tally, ...]:
        """
        Gets output file tally blocks.

        Parameters:
            number: Tally block number to get.
            kind: Tally block type to get.

        Returns:
            Tally blocks of number ``number``, if specificed, and kind ``kind``.
        """

        every = self.blocks.filter(kind)

        number_matches = every

        if number is not None:
            number = abc.Terminal[r'.{8}'](str(number).rjust(8))
            number_matches = self.blocks.filter(kind, number=number)

        return tuple(number_matches)

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for tallies.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for tallies.

        Returns:
            Pandas dataframe for all tallies.
        """

        if tallies := self.blocks.filter(outp.block.Tally):
            if returning:
                frames = []

            for tally in tallies:
                yield (frame := tally.to_dataframe())

                if returning:
                    frames.append(frame)

            if returning:
                return pandas.concat(frames, ignore_index=True)
        else:
            if returning:
                return pandas.DataFrame()
