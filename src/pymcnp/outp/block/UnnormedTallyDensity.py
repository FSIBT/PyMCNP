import typing
import dataclasses

from ... import abc
from ..Block import Block


class UnnormedTallyDensity(Block):
    """
    Represents unnormed tally density blocks.

    Attributes:
        name: unnormed tally density block `1unnormed tally density` symbol.
        tally_preamble: unnormed tally density block ` for tally ` symbol.
        tally: unnormed tally density block tally parameter.
        nonzero_tally_mean_preamble: unnormed tally density block ` nonzero tally mean(m)` symbol.
        nonzero_tally_mean: unnormed tally density block nonzero tally mean parameter.
        nps_preamble: unnormed tally density block `   nps = ` symbol.
        nps: unnormed tally density block nps parameter.
        print_preamble: unnormed tally density block ` print table ` symbol.
        print: unnormed tally density block `161` symbol.
        table_heading: unnormed tally density block `\\n\\n abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin\\(d=decade,slope= 0.0\\)` symbol.
        table_body_preamble: unnormed tally density block `\\n` symbol.
        table_body: unnormed tally density block table body parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1unnormed tally density'] = abc.Terminal[r'1unnormed tally density']('1unnormed tally density')
    tally_preamble: typing.Annotated[abc.Terminal, r' for tally '] = abc.Terminal[r' for tally '](' for tally ')
    tally: typing.Annotated[abc.Terminal, r'.{8}']
    nonzero_tally_mean_preamble: typing.Annotated[abc.Terminal, r'          nonzero tally mean\(m\) = '] = abc.Terminal[r'          nonzero tally mean\(m\) = ']('          nonzero tally mean(m) = ')
    nonzero_tally_mean: typing.Annotated[abc.Terminal, r'.{9}']
    nps_preamble: typing.Annotated[abc.Terminal, r'   nps = '] = abc.Terminal[r'   nps = ']('   nps = ')
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    print_preamble: typing.Annotated[abc.Terminal, r'  print table '] = abc.Terminal[r'  print table ']('  print table ')
    print: typing.Annotated[abc.Terminal, r'161'] = abc.Terminal[r'161']('161')
    table_heading: typing.Annotated[
        abc.Terminal,
        r'\n\n abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin\(d=decade,slope= 0\.0\)',
    ] = abc.Terminal[r'\n\n abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin\(d=decade,slope= 0\.0\)'](
        '\n\n abscissa              ordinate   log plot of tally probability density function in tally fluctuation chart bin(d=decade,slope= 0.0)'
    )
    table_body_preamble: typing.Annotated[abc.Terminal, r'\n'] = abc.Terminal[r'\n']('\n')
    table_body: typing.Annotated[abc.Terminal, r'[\s\S]*?(?=\n1|\Z)']
