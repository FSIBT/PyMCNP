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
    blocks: typing.Annotated[abc.Array, outp.Block, abc.Terminal[r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
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

    @property
    def activities(self) -> tuple[outp.block.Activity, ...]:
        """
        Output file activites.
        """

        return tuple(block for block in self.blocks if isinstance(block, outp.block.Activity)) if isinstance(self.blocks, abc.Array) else ()

    @property
    def activities_neutron(self) -> tuple[outp.block.NeutronActivity, ...]:
        """
        Output file neutron activites.
        """

        return tuple(block for block in self.blocks if isinstance(block, outp.block.NeutronActivity)) if isinstance(self.blocks, abc.Array) else ()

    @property
    def activities_photon(self) -> tuple[outp.block.PhotonActivity, ...]:
        """
        Output file photon activites.
        """

        return tuple(block for block in self.blocks if isinstance(block, outp.block.PhotonActivity)) if isinstance(self.blocks, abc.Array) else ()

    @property
    def tallies(self) -> tuple[outp.block.Tally, ...]:
        """
        Output file tallies.
        """

        return tuple(block for block in self.blocks if isinstance(block, outp.block.Tally)) if isinstance(self.blocks, abc.Array) else ()

    @property
    def tallies_surface(self) -> tuple[outp.block.Tally, ...]:
        """
        Output file surface tallies.
        """

        return tuple(block for block in self.blocks if isinstance(block, outp.block.TallySurface)) if isinstance(self.blocks, abc.Array) else ()

    @property
    def tallies_angle(self) -> tuple[outp.block.Tally, ...]:
        """
        Output file angle tallies.
        """

        return tuple(block for block in self.blocks if isinstance(block, outp.block.TallyAngle)) if isinstance(self.blocks, abc.Array) else ()

    @property
    def tallies_cell(self) -> tuple[outp.block.Tally, ...]:
        """
        Output file cell tallies.
        """

        return tuple(block for block in self.blocks if isinstance(block, outp.block.TallyCell)) if isinstance(self.blocks, abc.Array) else ()

    def to_dataframe(self) -> dict[str, pandas.DataFrame]:
        """
        Generates pandas dataframes from output files.

        Returns:
            Tuple of corresponding pandas dataframes.
        """

        tallies = {}

        for block in self.blocks:
            if isinstance(block, outp.block.Tally):
                assert hasattr(block, 'number')
                assert isinstance(block.number, str)
                tallies[block.number.strip()] = block.to_dataframe()

        return tallies
