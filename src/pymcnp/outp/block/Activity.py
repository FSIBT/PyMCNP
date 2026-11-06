import typing

import pandas

from ... import abc
from .. import line
from ..Block import Block


class Activity(Block):
    """
    Represents activity blocks.
    """

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes for activity blocks.

        Returns:
            Pandas dataframe for activity block.
        """

        assert hasattr(self, 'table_body')
        assert isinstance(self.table_body, abc.Array)
        assert all(isinstance(row, line.Activity) for row in self.table_body)

        if self.table_body:
            return pandas.concat((row.to_dataframe() for row in self.table_body), ignore_index=True)
        else:
            return pandas.DataFrame()


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
