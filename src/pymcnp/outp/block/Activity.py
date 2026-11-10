import typing

import pandas

from ... import abc
from .. import line
from ..Block import Block

COLUMNS = (
    'cell',
    'tracks',
    'population',
    'collisions',
    'collisions_weighted',
    'number_weighted_energy',
    'flux_weighted_energy',
    'average_track_weight',
    'average_track_mfp',
)


class Activity(Block):
    """
    Represents activity blocks.
    """

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes for activity tables (print table 126), one row per cell, plus a final ``total`` row.

        Returns:
            Dataframe with the columns ``COLUMNS``; the ``total`` row has no cell and only tracks, population, collisions and weighted collisions.

        Raises:
            Error: Invalid table row.
        """

        assert hasattr(self, 'table_body')
        assert isinstance(self.table_body, abc.Array)
        assert all(isinstance(row, line.Activity) for row in self.table_body)

        rows = []
        for row in self.table_body:
            fields = row.to_mcnp().split()
            if len(fields) != 10:
                raise abc.Error('Invalid table row.', f'{row=}')
            rows.append([int(fields[1]), int(fields[2]), int(fields[3]), int(fields[4]), *map(float, fields[5:])])

        frame = pandas.DataFrame(rows, columns=list(COLUMNS))
        total = pandas.DataFrame(
            [
                {
                    'cell': None,
                    'tracks': int(str(getattr(self, 'table_total_tracks'))),
                    'population': int(str(getattr(self, 'table_total_population'))),
                    'collisions': int(str(getattr(self, 'table_total_collisions'))),
                    'collisions_weighted': float(str(getattr(self, 'table_total_weighted_collisions'))),
                }
            ],
            columns=list(COLUMNS),
        )
        frame = pandas.concat([frame, total], ignore_index=True) if rows else total
        frame['cell'] = frame['cell'].astype('Int64')

        return frame


class NeutronActivity(Activity):
    """
    Represents neutron activity blocks.

    Attributes:
        name: neutron activity block ``r'\\n1neutron  activity in each cell'`` symbol.
        print_preamble: neutron activity block ``r'                                                                         print table '`` symbol.
        print: neutron activity block ``r'126'`` symbol.
        table_heading_1: neutron activity block ``r'\\n\\n                       tracks     population   collisions   collisions     number        flux        average      average'`` symbol.
        table_heading_2: neutron activity block ``r'\\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp'`` symbol.
        table_heading_3: neutron activity block ``r'\\n                                                          (per history)'`` symbol.
        table_body_preamble: neutron activity block ``r'\\n\\n'`` symbol.
        table_body: neutron activity block table body.
        table_total_preamble: neutron activity block ``r'\\n\\n           total'`` symbol.
        table_total_tracks_preamble: neutron activity block ``r'    '`` symbol.
        table_total_tracks: neutron activity block table total tracks.
        table_total_population_preamble: neutron activity block ``r'    '`` symbol.
        table_total_population: neutron activity block table total population.
        table_total_collisions_preamble: neutron activity block ``r'  '`` symbol.
        table_total_collisions: neutron activity block table total collisions.
        table_total_weighted_collisions_preamble: neutron activity block ``r'    '`` symbol.
        table_total_weighted_collisions: neutron activity block table total weighted collisions.
    """

    name: typing.Annotated[abc.Terminal, r'\n1neutron  activity in each cell']
    print_preamble: typing.Annotated[
        abc.Terminal,
        r'                                                                         print table ',
    ]
    print: typing.Annotated[abc.Terminal, r'126']
    table_heading_1: typing.Annotated[
        abc.Terminal,
        r'\n\n                       tracks     population   collisions   collisions     number        flux        average      average',
    ]
    table_heading_2: typing.Annotated[
        abc.Terminal,
        r'\n              cell    entering                               \* weight     weighted     weighted   track weight   track mfp',
    ]
    table_heading_3: typing.Annotated[
        abc.Terminal,
        r'\n                                                          \(per history\)    energy       energy     \(relative\)      \(cm\)',
    ]
    table_body_preamble: typing.Annotated[abc.Terminal, r'\n\n']
    table_body: typing.Annotated[abc.Array, line.Activity, typing.Annotated[abc.Terminal, r'\n']]
    table_total_preamble: typing.Annotated[abc.Terminal, r'\n\n           total']
    table_total_tracks_preamble: typing.Annotated[abc.Terminal, r'    ']
    table_total_tracks: typing.Annotated[abc.Terminal, r'.{10}']
    table_total_population_preamble: typing.Annotated[abc.Terminal, r'    ']
    table_total_population: typing.Annotated[abc.Terminal, r'.{10}']
    table_total_collisions_preamble: typing.Annotated[abc.Terminal, r'  ']
    table_total_collisions: typing.Annotated[abc.Terminal, r'.{10}']
    table_total_weighted_collisions_preamble: typing.Annotated[abc.Terminal, r'    ']
    table_total_weighted_collisions: typing.Annotated[abc.Terminal, r'.{10}']


class PhotonActivity(Activity):
    """
    Represents photonactivity blocks.

    Attributes:
        name: photon activity block ``r'\\n1photon   activity in each cell'`` symbol.
        print_preamble: photon activity block ``r'                                                                         print table '`` symbol.
        print: photon activity block ``r'126'`` symbol.
        table_heading_1: photon activity block ``r'\\n\\n                       tracks     population   collisions   collisions     number        flux        average      average'`` symbol.
        table_heading_2: photon activity block ``r'\\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp'`` symbol.
        table_heading_3: photon activity block ``r'\\n                                                          (per history)'`` symbol.
        table_body_preamble: photon activity block ``r'\\n\\n'`` symbol.
        table_body: photon activity block table body.
        table_total_preamble: photon activity block ``r'\\n\\n           total'`` symbol.
        table_total_tracks_preamble: photon activity block ``r'    '`` symbol.
        table_total_tracks: photon activity block table total tracks.
        table_total_population_preamble: photon activity block ``r'    '`` symbol.
        table_total_population: photon activity block table total population.
        table_total_collisions_preamble: photon activity block ``r'  '`` symbol.
        table_total_collisions: photon activity block table total collisions.
        table_total_weighted_collisions_preamble: photon activity block ``r'    '`` symbol.
        table_total_weighted_collisions: photon activity block table total weighted collisions.
    """

    name: typing.Annotated[abc.Terminal, r'\n1photon   activity in each cell']
    print_preamble: typing.Annotated[
        abc.Terminal,
        r'                                                                         print table ',
    ]
    print: typing.Annotated[abc.Terminal, r'126']
    table_heading_1: typing.Annotated[
        abc.Terminal,
        r'\n\n                       tracks     population   collisions   collisions     number        flux        average      average',
    ]
    table_heading_2: typing.Annotated[
        abc.Terminal,
        r'\n              cell    entering                               \* weight     weighted     weighted   track weight   track mfp',
    ]
    table_heading_3: typing.Annotated[
        abc.Terminal,
        r'\n                                                          \(per history\)    energy       energy     \(relative\)      \(cm\)',
    ]
    table_body_preamble: typing.Annotated[abc.Terminal, r'\n\n']
    table_body: typing.Annotated[abc.Array, line.Activity, typing.Annotated[abc.Terminal, r'\n']]
    table_total_preamble: typing.Annotated[abc.Terminal, r'\n\n           total']
    table_total_tracks_preamble: typing.Annotated[abc.Terminal, r'    ']
    table_total_tracks: typing.Annotated[abc.Terminal, r'.{10}']
    table_total_population_preamble: typing.Annotated[abc.Terminal, r'    ']
    table_total_population: typing.Annotated[abc.Terminal, r'.{10}']
    table_total_collisions_preamble: typing.Annotated[abc.Terminal, r'  ']
    table_total_collisions: typing.Annotated[abc.Terminal, r'.{10}']
    table_total_weighted_collisions_preamble: typing.Annotated[abc.Terminal, r'    ']
    table_total_weighted_collisions: typing.Annotated[abc.Terminal, r'.{10}']
