import typing
import dataclasses

from ... import abc
from ..Block import Block


class StartingMcrun(Block):
    """
    Represents startingmcrun blocks.

    Attributes:
        name: startingmcrun block `1starting mcrun.` symbol.
        cp0_preamble: startingmcrun block `      cp0 = ` symbol.
        cp0: startingmcrun block `cp0` parameter.
        print_preamble: startingmcrun block `                                                                       print table ` symbol.
        print: startingmcrun block `110` symbol.
        title_preamble: startingmcrun block `\\n\\n      ` symbol.
        title: startingmcrun block `title` parameter.
        table_heading: startingmcrun block `\\n\\n\\n     nps    x          y          z          cell       surf     u          v          w        energy     weight      time` symbol.
        table_body_preamble: startingmcrun block `\\n \\n` symbol.
        table_body: startingmcrun block `table_body` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    name: typing.Annotated[abc.Terminal, r'\n1starting mcrun\.'] = abc.Terminal[r'1starting mcrun\.']('1starting mcrun.')
    cp0_preamble: typing.Annotated[abc.Terminal, r'      cp0 = '] = abc.Terminal[r'      cp0 = ']('      cp0 = ')
    cp0: typing.Annotated[abc.Terminal, r'.{5}']
    print_preamble: typing.Annotated[
        abc.Terminal,
        r'                                                                       print table ',
    ] = abc.Terminal[r'                                                                       print table ']('                                                                       print table ')
    print: typing.Annotated[abc.Terminal, r'110'] = abc.Terminal[r'110']('110')
    title_preamble: typing.Annotated[abc.Terminal, r'\n\n      '] = abc.Terminal[r'\n\n      ']('\n\n      ')
    title: typing.Annotated[abc.Terminal, r'.{80}']
    table_heading: typing.Annotated[
        abc.Terminal,
        r'\n\n\n     nps    x          y          z          cell       surf     u          v          w        energy     weight      time',
    ] = abc.Terminal[r'\n\n\n     nps    x          y          z          cell       surf     u          v          w        energy     weight      time'](
        '\n\n\n     nps    x          y          z          cell       surf     u          v          w        energy     weight      time'
    )
    table_body_preamble: typing.Annotated[abc.Terminal, r'\n \n'] = abc.Terminal[r'\n \n']('\n \n')
    table_body: typing.Annotated[abc.Terminal, r'[\s\S]*?(?=\n1|\Z)']
