import typing

import pandas

from ... import abc
from .. import subblock
from ..Block import Block


class Tally(Block):
    """
    Represents tally blocks.
    """

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes for tally blocks.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        assert hasattr(self, 'number')
        assert isinstance(self.number, str)
        assert hasattr(self, 'tally_type')
        assert isinstance(self.tally_type, str)
        assert hasattr(self, 'particles')
        assert isinstance(self.particles, str)
        assert hasattr(self, 'nps')
        assert isinstance(self.nps, str)
        assert hasattr(self, 'subtallies')
        assert isinstance(self.subtallies, abc.Array)
        assert all(isinstance(subtally, subblock.Tally) for subtally in self.subtallies)

        if self.subtallies:
            df = pandas.concat((subtally.to_dataframe() for subtally in self.subtallies), ignore_index=True)

            df['number'] = self.number.strip()
            df['type'] = self.tally_type.strip()
            df['particles'] = self.particles.strip()
            df['nps'] = self.nps.strip()

            return df
        else:
            return pandas.DataFrame()


class TallySurface(Tally):
    """
    Represents surface tally blocks.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block ``r'        nps = '`` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block ``r'\\n           tally type '`` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block ``r'\\n           particle(s)'`` symbol.
        particles: tally block particles.
        surface_preamble: tally block ``           areas   \\n                surface.
        surface_number: tally block surface number.
        surface_area_preamble: tally block ``r'\\n                         '`` symbol.
        surface_area: tally block surface area.
        subtallies_preamble: tally block ``r'\\n \\n'`` symbol.
        subtallies: tally block subtallies.
    """

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    surface_preamble: typing.Annotated[abc.Terminal, r'\n\n           areas   \n                surface: ']
    surface_number: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    surface_area_preamble: typing.Annotated[abc.Terminal, r'\n                         ']
    surface_area: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.Surface, typing.Annotated[abc.Terminal, r'']]
    statistics: subblock.Statistics


class TallyAngle(Tally):
    """
    Represents angle tally blocks.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block ``r'        nps = '`` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block ``r'\\n           tally type '`` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block ``r'\\n           particle(s)'`` symbol.
        particles: tally block particles.
        subtallies_preamble: tally block ``r'\\n \\n'`` symbol.
        subtallies: tally block subtallies.
        statistics: tally statistics subblock.
    """

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.SurfaceAngle, typing.Annotated[abc.Terminal, r'']]


class TallyCell(Tally):
    """
    Represents cell tally blocks.
    """


class TallyCell_0(TallyCell):
    """
    Represents cell tally blocks, form #0.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block ``r'        nps = '`` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block ``r'\\n           tally type '`` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block ``r'\\n           particle(s)'`` symbol.
        particles: tally block particles.
        cell_preamble: tally block ``           volumes \\n                   cell.
        cell_number: tally block cell number.
        cell_volume_preamble: tally block ``r'\\n                         '`` symbol.
        cell_volume: tally block cell volume.
        subtallies_preamble: tally block ``r'\\n \\n'`` symbol.
        subtallies: tally block subtallies.
        statistics: tally statistics subblock.
    """

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    cell_preamble: typing.Annotated[abc.Terminal, r'\n\n           volumes \n                   cell: ']
    cell_number: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    cell_volume_preamble: typing.Annotated[abc.Terminal, r'\n                         ']
    cell_volume: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.Cell, typing.Annotated[abc.Terminal, r'']]


class TallyCell_1(TallyCell):
    """
    Represents cell tally blocks, form #1.

    Attributes:
        name: tally block name.
        number: tally block number.
        nps_preamble: tally block ``r'        nps = '`` symbol.
        nps: tally block nps.
        tally_type_preamble: tally block ``r'\\n           tally type '`` symbol.
        tally_type: tally block tally type.
        particles_preamble: tally block ``r'\\n           particle(s)'`` symbol.
        particles: tally block particles.
        subtallies_preamble: tally block ``r'\\n \\n'`` symbol.
        subtallies: tally block subtallies.
        statistics: tally statistics subblock.
    """

    name: typing.Annotated[abc.Terminal, r'\n1tally ']
    number: typing.Annotated[abc.Terminal, r'.{8}']
    nps_preamble: typing.Annotated[abc.Terminal, r'        nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    tally_type_preamble: typing.Annotated[abc.Terminal, r'\n           tally type ']
    tally_type: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    particles_preamble: typing.Annotated[abc.Terminal, r'\n           particle\(s\): ']
    particles: typing.Annotated[abc.Terminal, r'.+?(?=\n|\Z)']
    subtallies_preamble: typing.Annotated[abc.Terminal, r'\n \n']
    subtallies: typing.Annotated[abc.Array, subblock.tally.Cell, typing.Annotated[abc.Terminal, r'']]
