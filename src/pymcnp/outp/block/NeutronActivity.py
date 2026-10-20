import typing
import dataclasses

import pandas

from ... import abc
from . import _activity
from ..Block import Block


class NeutronActivity(Block):
    """
    Represents neutron activity blocks.

    Attributes:
        name: neutron activity block `1neutron  activity in each cell` symbol.
        print_preamble: neutron activity block ``'                                                                         print table '`` symbol.
        print: neutron activity block `126` symbol.
        table_heading_1: neutron activity block ``'\\n\\n                       tracks     population   collisions   collisions     number        flux        average      average'`` symbol.
        table_heading_2: neutron activity block ``'\\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp'`` symbol.
        table_heading_3: neutron activity block ``'\\n                                                          (per history)'`` symbol.
        table_body_preamble: neutron activity block ``'\\n\\n'`` symbol.
        table_body: neutron activity block table body.
        table_total_preamble: neutron activity block ``'\\n           total'`` symbol.
        table_total_tracks_preamble: neutron activity block ``'    '`` symbol.
        table_total_tracks: neutron activity block table total tracks.
        table_total_population_preamble: neutron activity block ``'    '`` symbol.
        table_total_population: neutron activity block table total population.
        table_total_collisions_preamble: neutron activity block ``'  '`` symbol.
        table_total_collisions: neutron activity block table total collisions.
        table_total_weighted_collisions_preamble: neutron activity block ``'    '`` symbol.
        table_total_weighted_collisions: neutron activity block table total weighted collisions.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    name: typing.Annotated[abc.Terminal, r'\n1neutron  activity in each cell'] = abc.Terminal[r'1neutron  activity in each cell']('1neutron  activity in each cell')
    print_preamble: typing.Annotated[
        abc.Terminal,
        r'                                                                         print table ',
    ] = abc.Terminal[r'                                                                         print table ']('                                                                         print table ')
    print: typing.Annotated[abc.Terminal, r'126'] = abc.Terminal[r'126']('126')
    table_heading_1: typing.Annotated[
        abc.Terminal,
        r'\n\n                       tracks     population   collisions   collisions     number        flux        average      average',
    ] = abc.Terminal[r'\n\n                       tracks     population   collisions   collisions     number        flux        average      average'](
        '\n\n                       tracks     population   collisions   collisions     number        flux        average      average'
    )
    table_heading_2: typing.Annotated[
        abc.Terminal,
        r'\n              cell    entering                               \* weight     weighted     weighted   track weight   track mfp',
    ] = abc.Terminal[r'\n              cell    entering                               \* weight     weighted     weighted   track weight   track mfp'](
        '\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp'
    )
    table_heading_3: typing.Annotated[
        abc.Terminal,
        r'\n                                                          \(per history\)    energy       energy     \(relative\)      \(cm\)',
    ] = abc.Terminal[r'\n                                                          \(per history\)    energy       energy     \(relative\)      \(cm\)'](
        '\n                                                          (per history)    energy       energy     (relative)      (cm)'
    )
    table_body_preamble: typing.Annotated[abc.Terminal, r'\n\n'] = abc.Terminal[r'\n\n']('\n\n')
    table_body: typing.Annotated[abc.Terminal, r'[\s\S]+?(?=\n           total|\Z)'] = dataclasses.field(kw_only=True)
    table_total_preamble: typing.Annotated[abc.Terminal, r'\n           total'] = abc.Terminal[r'\n           total']('\n           total')
    table_total_tracks_preamble: typing.Annotated[abc.Terminal, r'    '] = abc.Terminal[r'    ']('    ')
    table_total_tracks: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    table_total_population_preamble: typing.Annotated[abc.Terminal, r'    '] = abc.Terminal[r'    ']('    ')
    table_total_population: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    table_total_collisions_preamble: typing.Annotated[abc.Terminal, r'  '] = abc.Terminal[r'  ']('  ')
    table_total_collisions: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)
    table_total_weighted_collisions_preamble: typing.Annotated[abc.Terminal, r'    '] = abc.Terminal[r'    ']('    ')
    table_total_weighted_collisions: typing.Annotated[abc.Terminal, r'.{10}'] = dataclasses.field(kw_only=True)

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates a dataframe from the activity table, one row per cell and a final row for the totals (`cell` is missing there).

        Returns:
            Dataframe with the columns `cell`, `tracks`, `population`, `collisions`, `collisions_weighted`, `number_weighted_energy`, `flux_weighted_energy`, `average_track_weight` and `average_track_mfp`.
        """

        return _activity.to_dataframe(self)
