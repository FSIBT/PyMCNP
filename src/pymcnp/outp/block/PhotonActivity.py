import typing
import dataclasses

from ... import abc
from ..Block import Block


class PhotonActivity(Block):
    """
    Represents photonactivity blocks.

    Attributes:
        name: photon activity block `1photon   activity in each cell` symbol.
        print_preamble: photon activity block `                                                                         print table ` symbol.
        print: photon activity block `126` symbol.
        table_heading_1: photon activity block `\\n\\n                       tracks     population   collisions   collisions     number        flux        average      average` symbol.
        table_heading_2: photon activity block `\\n              cell    entering                               * weight     weighted     weighted   track weight   track mfp` symbol.
        table_heading_3: photon activity block `\\n                                                          (per history)` symbol.
        table_body_preamble: photon activity block `\\n\\n` symbol.
        table_body: photon activity block table body.
        table_total_preamble: photon activity block `\\n           total` symbol.
        table_total_tracks_preamble: photon activity block `    ` symbol.
        table_total_tracks: photon activity block table total tracks.
        table_total_population_preamble: photon activity block `    ` symbol.
        table_total_population: photon activity block table total population.
        table_total_collisions_preamble: photon activity block `  ` symbol.
        table_total_collisions: photon activity block table total collisions.
        table_total_weighted_collisions_preamble: photon activity block `    ` symbol.
        table_total_weighted_collisions: photon activity block table total weighted collisions.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1photon   activity in each cell'] = abc.Terminal[r'1photon   activity in each cell']('1photon   activity in each cell')
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
