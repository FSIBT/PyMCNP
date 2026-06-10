import typing
import dataclasses

from ... import abc
from ..Block import Block


class NeutronActivity(Block):
    """
    Represents neutronactivity blocks.

    Attributes:
        name: neutronactivity block `1neutron  activity in each cell` symbol.
        print_preamble: neutronactivity block `                                                                         print table ` symbol.
        print: neutronactivity block `126` symbol.
        table_heading_1: neutronactivity block `\\n\\n                       tracks     population   collisions   collisions     number        flux        average      average` symbol.
        table_heading_2: neutronactivity block `\\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp` symbol.
        table_heading_3: neutronactivity block `\\n                                                          (per history)` symbol.
        table_body_preamble: neutronactivity block `\\n\\n` symbol.
        table_body: neutronactivity block `table_body` parameter.
        table_total_preamble: neutronactivity block `\\n           total` symbol.
        table_total_tracks_preamble: neutronactivity block `    ` symbol.
        table_total_tracks: neutronactivity block `table_total_tracks` parameter.
        table_total_population_preamble: neutronactivity block `    ` symbol.
        table_total_population: neutronactivity block `table_total_population` parameter.
        table_total_collisions_preamble: neutronactivity block `  ` symbol.
        table_total_collisions: neutronactivity block `table_total_collisions` parameter.
        table_total_weighted_collisions_preamble: neutronactivity block `    ` symbol.
        table_total_weighted_collisions: neutronactivity block `table_total_weighted_collisions` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

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
    table_body: typing.Annotated[abc.Terminal, r'[\s\S]+?(?=\n           total|\Z)']
    table_total_preamble: typing.Annotated[abc.Terminal, r'\n           total'] = abc.Terminal[r'\n           total']('\n           total')
    table_total_tracks_preamble: typing.Annotated[abc.Terminal, r'    '] = abc.Terminal[r'    ']('    ')
    table_total_tracks: typing.Annotated[abc.Terminal, r'.{10}']
    table_total_population_preamble: typing.Annotated[abc.Terminal, r'    '] = abc.Terminal[r'    ']('    ')
    table_total_population: typing.Annotated[abc.Terminal, r'.{10}']
    table_total_collisions_preamble: typing.Annotated[abc.Terminal, r'  '] = abc.Terminal[r'  ']('  ')
    table_total_collisions: typing.Annotated[abc.Terminal, r'.{10}']
    table_total_weighted_collisions_preamble: typing.Annotated[abc.Terminal, r'    '] = abc.Terminal[r'    ']('    ')
    table_total_weighted_collisions: typing.Annotated[abc.Terminal, r'.{10}']
