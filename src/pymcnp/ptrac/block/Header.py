import typing

from ... import abc
from ..Block import Block
from .. import line


class Header(Block):
    """
    Represents header blocks.

    Attributes:
        magic: header block `r'   -1\\n'` symbol.
        newline_0: header block `r'\\n'` symbol #0.
        code: header block `code` parameter.
        version: header block `version` parameter.
        code_date: header block code `date` parameter.
        run_datetime: header block run `datetime` parameter.
        newline_1: header block `r'\\n'` symbol #1.
        title: header block title line.
        newline_2: header block `r'\\n'` symbol #2.
        v: header block v line.
        newline_3: header block `r'\\n'` symbol #3.
        blank: header block n line `r' '` symbol.
        n1: n line `n1` parameter.
        n2: n line `n2` parameter.
        n3: n line `n3` parameter.
        n4: n line `n4` parameter.
        n5: n line `n5` parameter.
        n6: n line `n6` parameter.
        n7: n line `n7` parameter.
        n8: n line `n8` parameter.
        n9: n line `n9` parameter.
        n10: n line `n10` parameter.
        n11: n line `n11` parameter.
        n12: n line `n12` parameter.
        n13: n line `n13` parameter.
        n14: n line `n14` parameter.
        n15: n line `n15` parameter.
        n16: n line `n16` parameter.
        n17: n line `n17` parameter.
        n18: n line `n18` parameter.
        n19: n line `n19` parameter.
        n20: n line `n20` parameter.
        newline_4: header block `r'\\n'` symbol #4.
        l: header block l line.
        newline_5: header block `r'\\n'` symbol #5.
    """

    magic: typing.Annotated[abc.Terminal, r'   -1']
    newline_0: typing.Annotated[abc.Terminal, r'\n']
    code: typing.Annotated[abc.Terminal, r'.{8}']
    version: typing.Annotated[abc.Terminal, r'.{25}']
    code_date: typing.Annotated[abc.Terminal, r'.{9}']
    run_datetime: typing.Annotated[abc.Terminal, r'.{18}']
    newline_1: typing.Annotated[abc.Terminal, r'\n']
    title: typing.Annotated[abc.Terminal, r'.{80}']
    newline_2: typing.Annotated[abc.Terminal, r'\n']
    v: line.V
    newline_3: typing.Annotated[abc.Terminal, r'\n']
    blank: typing.Annotated[abc.Terminal, r' ']
    n1: typing.Annotated[abc.Terminal, r'.{5}']
    n2: typing.Annotated[abc.Terminal, r'.{5}']
    n3: typing.Annotated[abc.Terminal, r'.{5}']
    n4: typing.Annotated[abc.Terminal, r'.{5}']
    n5: typing.Annotated[abc.Terminal, r'.{5}']
    n6: typing.Annotated[abc.Terminal, r'.{5}']
    n7: typing.Annotated[abc.Terminal, r'.{5}']
    n8: typing.Annotated[abc.Terminal, r'.{5}']
    n9: typing.Annotated[abc.Terminal, r'.{5}']
    n10: typing.Annotated[abc.Terminal, r'.{5}']
    n11: typing.Annotated[abc.Terminal, r'.{5}']
    n12: typing.Annotated[abc.Terminal, r'.{5}']
    n13: typing.Annotated[abc.Terminal, r'.{5}']
    n14: typing.Annotated[abc.Terminal, r'.{5}']
    n15: typing.Annotated[abc.Terminal, r'.{5}']
    n16: typing.Annotated[abc.Terminal, r'.{5}']
    n17: typing.Annotated[abc.Terminal, r'.{5}']
    n18: typing.Annotated[abc.Terminal, r'.{5}']
    n19: typing.Annotated[abc.Terminal, r'.{5}']
    n20: typing.Annotated[abc.Terminal, r'.{5}']
    newline_4: typing.Annotated[abc.Terminal, r'\n ']
    l: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r' \d\d\d|  \d\d|   \d'], typing.Annotated[abc.Terminal, r'\n |']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    newline_5: typing.Annotated[abc.Terminal, r'\n']
