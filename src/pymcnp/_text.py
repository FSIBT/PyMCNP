import re
import pathlib

import _data


# UTILITIES #
def has_suffix(element):
    return 'suffix' in [attribute.name for attribute in element.attributes]


def has_designator(element):
    return 'designator' in [attribute.name for attribute in element.attributes]


def TABS(t):
    return t * '    '


def CAMEL(name: str) -> str:
    name = re.sub('/', '_', name)
    if name:
        return name[0].upper() + name[1:]
    else:
        return ''


def SNAKE(name: str) -> str:
    name = re.sub('/', '_', name)
    return name.lower()


def FILE(name: str) -> str:
    name = re.sub('/', '_', name)
    return name.lower()


# ATTRIBUTE FUNCTIONS #
def ATTRS_REGEX(element):
    def _REGEX(element):
        return f"{"(\\d+?)" if has_suffix(element) else ""}{":(\\S+?)" if has_designator(element) else ""}{ATTRS_REGEX(element)}"

    o = ''

    for attribute in element.attributes:
        if attribute.name in {'suffix', 'designator'}:
            continue

        if 'Tuple' in attribute.type:
            if 'Option_' in attribute.type:
                o += (
                    f'(( ({{{SNAKE(element.name)}.{CAMEL(element.name)}Option_._REGEX.pattern}}))+)'
                )
            elif 'Entry' in attribute.type:
                o += f'(( {{{attribute.type[12:-1]}._REGEX.pattern}})+)'
            else:
                o += '(( \\S+)+)'
        else:
            if 'Option_' in attribute.type:
                o += f'( {{{SNAKE(element.name)}.{CAMEL(element.name)}Option_._REGEX.pattern}})'
            elif 'Entry' in attribute.type:
                o += f'( {{{attribute.type}._REGEX.pattern}})'
            else:
                o += '( \\S+)'

        if attribute.optional:
            o += '?'

    return o


def ATTRS_DICT(element):
    a = ''
    b = ''

    for attribute in element.attributes:
        a += f'"{attribute.name}": {attribute.type}, '

    return a + b


def ATTRS_LIST(element):
    o = ''

    for attribute in element.attributes:
        if attribute.name not in {'suffix', 'designator'}:
            o += f'{attribute.name}, '

    return o


def ATTRS_PARAM(element):
    a = []
    b = []

    for attribute in element.attributes:
        if attribute.optional:
            b += [f'{attribute.name}: {attribute.type} = None']
        else:
            a += [f'{attribute.name}: {attribute.type}']

    return ', '.join(a + b).strip()


def ATTRS_CHECK(element, parent_name, t):
    o = ''

    for attribute in element.attributes:
        if attribute.restriction:
            if attribute.optional:
                o += f'{TABS(t)}if {attribute.name} is not None and not ({attribute.restriction}):\n{TABS(t+1)}raise {f"errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, {attribute.name})" if parent_name else f"errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, {attribute.name})"}\n'
            else:
                o += f'{TABS(t)}if {attribute.name} is None or not ({attribute.restriction}):\n{TABS(t+1)}raise {f"errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, {attribute.name})" if parent_name else f"errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, {attribute.name})"}\n'
        else:
            if attribute.optional:
                continue
            else:
                o += f'{TABS(t)}if {attribute.name} is None:\n{TABS(t+1)}raise {f"errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, {attribute.name})" if parent_name else f"errors.InpError(errors.InpCode.SEMANTICS_CARD_VALUE, {attribute.name})"}\n'

    return o.strip()


def ATTRS_STORE(element, t):
    o = ''

    for attribute in element.attributes:
        o += f'{TABS(t)}self.{attribute.name}: typing.Final[{attribute.type}] = {attribute.name}\n'

    return o.strip()


def ATTRS_COMMENT(element, t):
    o = ''

    for attribute in element.attributes:
        o += f'{TABS(t)}{attribute.name}: {attribute.description}.\n'

    return o.strip()


# ELEMENT #
def INIT(element):
    return f"""
from .option_ import {CAMEL(element.name)}Option_
{''.join(f"from . import {SNAKE(option.name)}\n" if option.options else "" for option in element.options)[:-1]}
{''.join(f'from .{CAMEL(option.name)} import {CAMEL(option.name)}\n' for option in element.options)[:-1]}

__all__ = [
    "{CAMEL(element.name)}Option_",
    {''.join(f'\t"{SNAKE(option.name)}",\n' if option.options else "" for option in element.options).strip()}
    {''.join(f'\t"{CAMEL(option.name)}",\n' for option in element.options).strip()}
]
"""[1:-1]


def OPTION(element, depth):
    return f'''
import re
import typing

{''.join(f"from . import {SNAKE(option.name)}\n" if option.options else "" for option in element.options)}
from {"." * (depth - 1)}option_ import Option_
from {"." * depth}utils import types
from {"." * depth}utils import errors
from {"." * depth}utils import _parser
from {"." * depth}utils import _object


class {CAMEL(element.name)}Option_(Option_):
    """
    Represents generic INP {element.name} options.
    """

    _KEYWORD = ""
    _SUBCLASSES = {{}}
    _REGEX = re.compile(
        rf"{r'|'.join(f"{option.mnemonic}{r'(\S+)' if has_suffix(option) else ''}{r':(\S+)' if has_designator(option) else ''}{ATTRS_REGEX(option)}" for option in sorted(element.options, reverse=True, key=lambda scheme: len(scheme.mnemonic)))}"
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
'''[1:]


def ELEMENT(element, parent_name, depth):
    return f'''
import re
import typing

import molmass

{f"from . import {SNAKE(element.name)}" if element.options else ""}
{f"from .option_ import {CAMEL(parent_name)}Option_" if parent_name else "from .card_ import Card_"}
from {"." * depth}utils import types
from {"." * depth}utils import errors
from {"." * depth}utils import _parser
from {"." * depth}utils import _elements
from {"." * depth}utils import _visualization


class {CAMEL(element.name)}({f"{CAMEL(parent_name)}Option_, keyword='{element.mnemonic}'" if parent_name else "Card_"}):
    """
    Represents INP {element.name} elements.

    Attributes:
        InpError: {element.error}.
    """

    _ATTRS = {{{ATTRS_DICT(element)}}}

    _REGEX = re.compile(rf"{element.mnemonic}{r"(\S+)" if has_suffix(element) else ""}{r":(\S+)" if has_designator(element) else ""}{ATTRS_REGEX(element)}")
    
    def __init__(self, {ATTRS_PARAM(element)}):
        """
        Initializes ``{CAMEL(element.name)}``.

        Parameters:
            {ATTRS_COMMENT(element, 3)}

        Raises:
            InpError: {element.error}.
        """

        {ATTRS_CHECK(element, parent_name, 2)}

        self.value: typing.Final[types.Tuple] = types.Tuple([{ATTRS_LIST(element)}])\n
        {ATTRS_STORE(element, 2)}

    {element.extra}
'''[1:]


# SCRIPT #
def build_element(element, parent_name, path_dir, depth):
    if element.options:
        for option in element.options:
            path_subdir = path_dir / f'{SNAKE(element.name)}'
            path_subdir.mkdir(parents=True, exist_ok=True)

            path_subinit = path_subdir / '__init__.py'
            with path_subinit.open('w') as file:
                file.write(INIT(element))

            path_suboption = path_subdir / 'option_.py'
            with path_suboption.open('w') as file:
                file.write(OPTION(element, depth))

            build_element(option, element.name, path_subdir, depth + 1)

    if element.name not in {'cell', 'surface', 'comment'} and parent_name != '':
        path_file = path_dir / f'{CAMEL(element.name)}.py'
        with path_file.open('w') as file:
            file.write(ELEMENT(element, parent_name, depth - 1))


for card in _data.cards.options:
    build_element(card, '', pathlib.Path(__file__).parent / 'inp', 3)
