import re
import os
import pathlib

import inp_data


# UTILITIES #
def has_suffix(element):
    return 'suffix' in [attribute.name for attribute in element.attributes]


def has_designator(element):
    return 'designator' in [attribute.name for attribute in element.attributes]


def TABS(t):
    return t * '    '


def CAMEL(name: str, more: str = '') -> str:
    if more:
        if '_' in name:
            name = CAMEL(name)
            return name.split('_')[0] + more + '_' + name.split('_')[1]
        else:
            return CAMEL(name) + more
    else:
        name = re.sub('/', '_', name)

        if name:
            return name[0].upper() + name[1:]
        else:
            return ''


def SNAKE(name: str) -> str:
    name = re.sub('/', '_', name)
    return name.lower()


# ATTRIBUTE FUNCTIONS #
def ATTRS_REGEX(element):
    def _REGEX(element):
        return f'{"(\\d+?)" if has_suffix(element) else ""}{":(\\S+?)" if has_designator(element) else ""}{ATTRS_REGEX(element)}'

    o = ''

    for attribute in element.attributes:
        if attribute.name in {'suffix', 'designator'}:
            continue

        if 'Tuple' in attribute.type:
            if 'Option' in attribute.type:
                o += f'((?: (?:{{{attribute.type[12:-1]}._REGEX.pattern[2:-2]}}))+?)'
            else:
                o += f'((?: {{{attribute.type[12:-1]}._REGEX.pattern[2:-2]}})+?)'
        else:
            if 'Option' in attribute.type:
                o += f'( (?:{{{attribute.type}._REGEX.pattern[2:-2]}}))'
            elif attribute.type == 'types.Boolean':
                o += f'( {attribute.restriction})'
            else:
                if attribute.can_quote:
                    o += f'( \\"{{{attribute.type}._REGEX.pattern[2:-2]}}\\")'
                elif attribute.can_paren:
                    o += f'( {{{attribute.type}._REGEX.pattern[2:-2]}}| [(]{{{attribute.type}._REGEX.pattern[2:-2]}}[)])'
                else:
                    o += f'( {{{attribute.type}._REGEX.pattern[2:-2]}})'

        if attribute.optional:
            o += '?'

    return o


def GET_REGEX(element):
    if element.regex:
        return element.regex
    else:
        return rf'{element.mnemonic}{r"(\d+)" if has_suffix(element) else ""}{r":(\S+)" if has_designator(element) else ""}{ATTRS_REGEX(element)}'


def ATTRS_DICT(element):
    a = ''
    b = ''

    for attribute in element.attributes:
        a += f'"{attribute.name}": {attribute.type}, '

    return a + b


def ATTR_PARAM(attribute):
    if attribute.type.startswith('types.Tuple'):
        if 'types.Integer' in attribute.type:
            return f'{attribute.name}: list[str] | list[int] | list[types.Integer]'
        elif 'types.Real' in attribute.type:
            return f'{attribute.name}: list[str] | list[float] | list[types.Real]'
        else:
            return f'{attribute.name}: list[str] | list[{attribute.type[12:-1]}]'
    else:
        if 'types.Integer' in attribute.type:
            return f'{attribute.name}: str | int | types.Integer'
        elif 'types.Real' in attribute.type:
            return f'{attribute.name}: str | int | float | types.Real'
        else:
            return f'{attribute.name}: str | {attribute.type}'


def ATTRS_PARAM(element):
    a = []
    b = []

    for attribute in element.attributes:
        if attribute.optional:
            b += [ATTR_PARAM(attribute) + ' = None']
        else:
            a += [ATTR_PARAM(attribute)]

    return ', '.join(a + b)


def ATTR_CHECK(attribute, parent_name, t):
    if attribute.restriction:
        if attribute.optional:
            return f'if {attribute.name} is not None and not ({attribute.restriction}):\n{TABS(t + 1)}raise {f"errors.InpError(errors.InpCode.SEMANTICS_OPTION, {attribute.name})" if parent_name else f"errors.InpError(errors.InpCode.SEMANTICS_CARD, {attribute.name})"}'
        else:
            return f'if {attribute.name} is None or not ({attribute.restriction}):\n{TABS(t + 1)}raise {f"errors.InpError(errors.InpCode.SEMANTICS_OPTION, {attribute.name})" if parent_name else f"errors.InpError(errors.InpCode.SEMANTICS_CARD, {attribute.name})"}'
    else:
        if attribute.optional:
            return ''
        else:
            return f'if {attribute.name} is None:\n{TABS(t + 1)}raise {f"errors.InpError(errors.InpCode.SEMANTICS_OPTION, {attribute.name})" if parent_name else f"errors.InpError(errors.InpCode.SEMANTICS_CARD, {attribute.name})"}'


def ATTRS_STORE(element, t):
    o = ''

    for attribute in element.attributes:
        o += f'{TABS(t)}self.{attribute.name}: {attribute.type} = {attribute.name}\n'

    return o.strip()


def ATTRS_COMMENT(element, t):
    o = ''

    for attribute in element.attributes:
        o += f'{TABS(t)}{attribute.name}: {attribute.description}.\n'

    return o.strip()


def ATTR_BUILDER(element, attribute, t):
    o = ''

    o += f'{TABS(t)}if {attribute.name} is not None:\n'

    if attribute.type.startswith('types.Tuple'):
        o += f'{TABS(t)}    array = []\n'
        o += f'{TABS(t)}    for item in {attribute.name}:\n'
        o += f'{TABS(t)}        if isinstance(item, {attribute.type[12:-1]}):\n'
        o += f'{TABS(t)}            array.append(item)\n'

        if 'types.Integer' in attribute.type:
            o += f'{TABS(t)}        elif isinstance(item, int):\n'
            o += f'{TABS(t)}            array.append({attribute.type[12:-1]}(item))\n'
        if 'types.Real' in attribute.type:
            o += f'{TABS(t)}        elif isinstance(item, int) or isinstance(item, float):\n'
            o += f'{TABS(t)}            array.append({attribute.type[12:-1]}(item))\n'

        o += f'{TABS(t)}        elif isinstance(item, str):\n'
        o += f'{TABS(t)}            array.append({attribute.type[12:-1]}.from_mcnp(item))\n'
        o += f'{TABS(t)}    {attribute.name} = types.Tuple({attribute.type[12:-1]})(array)\n'
    else:
        o += f'{TABS(t)}    if isinstance({attribute.name}, {attribute.type}):\n'
        o += f'{TABS(t)}        {attribute.name} = {attribute.name}\n'

        if 'types.Integer' in attribute.type:
            o += f'{TABS(t)}    elif isinstance({attribute.name}, int):\n'
            o += f'{TABS(t)}        {attribute.name} = {attribute.type}({attribute.name})\n'
        if 'types.Real' in attribute.type:
            o += f'{TABS(t)}    elif isinstance({attribute.name}, int) or isinstance({attribute.name}, float):\n'
            o += f'{TABS(t)}        {attribute.name} = {attribute.type}({attribute.name})\n'

        o += f'{TABS(t)}    elif isinstance({attribute.name}, str):\n'
        o += f'{TABS(t)}        {attribute.name} = {attribute.type}.from_mcnp({attribute.name})\n'

    return o.strip()


def INIT(element):
    return f"""
from ._option import {CAMEL(element.name, 'Option')}
{''.join(f'from . import {SNAKE(option.name)}\n' if option.options else '' for option in element.options)[:-1]}
{''.join(f'from .{CAMEL(option.name)} import {CAMEL(option.name)}\n' for option in element.options)[:-1]}

__all__ = [
    "{CAMEL(element.name, 'Option')}",
    {''.join(f'\t"{SNAKE(option.name)}",\n' if option.options else '' for option in element.options).strip()}
    {''.join(f'\t"{CAMEL(option.name)}",\n' for option in element.options).strip()}
]
"""[1:-1]


def OPTION(element, depth):
    return f'''
import re
import typing

{''.join(f'from . import {SNAKE(option.name)}\n' if option.options else '' for option in element.options)}
from {'.' * (depth - 1)} import _option
from {'.' * depth} import types
from {'.' * depth} import errors
from {'.' * depth} import _parser


class {CAMEL(element.name, 'Option')}(_option.Option):
    """
    Represents generic INP {element.name} options.
    """

    pass
'''[1:]


def ATTRS_PROPS(element, parent_name):
    return ''.join(
        f'''
    @property
    def {attribute.name}(self) -> {attribute.type}:
        """
        {attribute.description[0].upper() + attribute.description[1:]}

        Raises:
            InpError: {element.error}.
            TypeError:
        """

        return self._{attribute.name}

    @{attribute.name}.setter
    def {attribute.name}(self, {ATTR_PARAM(attribute)}) -> None:
        """
        Sets ``{attribute.name}``.

        Parameters:
            {attribute.name}: {attribute.description}.

        Raises:
            InpError: {element.error}.
            TypeError:
        """

        {ATTR_BUILDER(element, attribute, 2)}

        {ATTR_CHECK(attribute, parent_name, 2)}

        self._{attribute.name}: {attribute.type} = {attribute.name}
'''
        for attribute in element.attributes
    )


def ELEMENT(element, parent_name, depth):
    return f'''
import re
import math
import copy
import typing
import dataclasses

import numpy
import molmass

{'from . import f' if parent_name == "sdef" else ""}
{f'from . import {SNAKE(element.name)}' if element.options else ''}
{'from . import _option' if parent_name else 'from . import _card'}
from {'.' * depth} import _show
from {'.' * depth} import types
from {'.' * depth} import errors
from {'.' * depth} import _parser
from {'.' * depth} import _elements


class {CAMEL(element.name)}(_option.{CAMEL(parent_name, 'Option')}):
    """
    Represents INP {element.name.split('_')[0]}{f' variation #{element.name.split("_")[1]}' if len(element.name.split('_')) - 1 else ''} elements.
    """

    _KEYWORD = "{element.mnemonic}"

    _ATTRS = {{{ATTRS_DICT(element)}}}

    _REGEX = re.compile(rf"\\A{GET_REGEX(element)}\\Z", re.IGNORECASE)
    
    def __init__(self, {ATTRS_PARAM(element)}):
        """
        Initializes ``{CAMEL(element.name)}``.

        Parameters:
            {ATTRS_COMMENT(element, 3)}

        Raises:
            InpError: {element.error}.
        """

        {ATTRS_STORE(element, 2)}

    {ATTRS_PROPS(element, parent_name)}

    {element.extra.strip()}
'''[1:]


# SCRIPT #
paths = []
delete = [
    'src/pymcnp/inp/data/act/dgeb/_option.py',
    'src/pymcnp/inp/data/act/dneb/_option.py',
    'src/pymcnp/inp/data/dd/_option.py',
    'src/pymcnp/inp/data/ds_1/_option.py',
    'src/pymcnp/inp/data/ds_2/_option.py',
    'src/pymcnp/inp/data/dxt/_option.py',
    'src/pymcnp/inp/data/embed/matcell/_option.py',
    'src/pymcnp/inp/data/f_1/_option.py',
    'src/pymcnp/inp/data/f_2/_option.py',
    'src/pymcnp/inp/data/files/_option.py',
    'src/pymcnp/inp/data/ksrc/_option.py',
    'src/pymcnp/inp/data/pikmt/_option.py',
    'src/pymcnp/inp/data/ptrac/filter/_option.py',
    'src/pymcnp/inp/data/uran/_option.py',
    'src/pymcnp/inp/data/sdef/F.py',
]
restore = [
    'src/pymcnp/inp/cell/__init__.py',
    'src/pymcnp/inp/data/Ds_1.py',
    'src/pymcnp/inp/data/Ds_2.py',
    'src/pymcnp/inp/data/F_0.py',
    'src/pymcnp/inp/data/F_2.py',
    'src/pymcnp/inp/data/M_0.py',
    'src/pymcnp/inp/data/Phys_2.py',
    'src/pymcnp/inp/data/Spdtl.py',
    'src/pymcnp/inp/data/act/dgeb/Bias.py',
    'src/pymcnp/inp/data/act/dgeb/__init__.py',
    'src/pymcnp/inp/data/act/dneb/Bias.py',
    'src/pymcnp/inp/data/act/dneb/__init__.py',
    'src/pymcnp/inp/data/dd/Diagnostic.py',
    'src/pymcnp/inp/data/dd/__init__.py',
    'src/pymcnp/inp/data/ds_1/Variables.py',
    'src/pymcnp/inp/data/ds_1/__init__.py',
    'src/pymcnp/inp/data/ds_2/Variables.py',
    'src/pymcnp/inp/data/ds_2/__init__.py',
    'src/pymcnp/inp/data/dxt/Shell.py',
    'src/pymcnp/inp/data/dxt/__init__.py',
    'src/pymcnp/inp/data/embed/Calcvols.py',
    'src/pymcnp/inp/data/embed/matcell/Entry.py',
    'src/pymcnp/inp/data/embed/matcell/__init__.py',
    'src/pymcnp/inp/data/f_1/Sphere.py',
    'src/pymcnp/inp/data/f_1/__init__.py',
    'src/pymcnp/inp/data/f_2/Ring.py',
    'src/pymcnp/inp/data/f_2/__init__.py',
    'src/pymcnp/inp/data/files/File.py',
    'src/pymcnp/inp/data/files/__init__.py',
    'src/pymcnp/inp/data/ksrc/Location.py',
    'src/pymcnp/inp/data/ksrc/__init__.py',
    'src/pymcnp/inp/data/pikmt/Photonbias.py',
    'src/pymcnp/inp/data/pikmt/__init__.py',
    'src/pymcnp/inp/data/ptrac/filter/Entry.py',
    'src/pymcnp/inp/data/ptrac/filter/__init__.py',
    'src/pymcnp/inp/data/sdef/__init__.py',
    'src/pymcnp/inp/data/sdef/tme_1/Embedded.py',
    'src/pymcnp/inp/data/sdef/tme_1/__init__.py',
    'src/pymcnp/inp/data/uran/Stochastic.py',
    'src/pymcnp/inp/data/uran/__init__.py',
]


def build_element(element, parent_name, path_dir, depth):
    if element.options:
        for option in element.options:
            path_subdir = path_dir / f'{SNAKE(element.name)}'
            path_subdir.mkdir(parents=True, exist_ok=True)

            path_subinit = path_subdir / '__init__.py'
            with path_subinit.open('w') as file:
                file.write(INIT(element))

            path_suboption = path_subdir / '_option.py'
            with path_suboption.open('w') as file:
                file.write(OPTION(element, depth))

            build_element(option, element.name, path_subdir, depth + 1)

    if parent_name != 'alsdkjfhalsdkjf':
        path_file = path_dir / f'{CAMEL(element.name)}.py'
        paths.append(path_file)
        with path_file.open('w') as file:
            file.write(ELEMENT(element, parent_name, depth - 1))


for card in inp_data.cards.options:
    build_element(card, 'alsdkjfhalsdkjf', pathlib.Path(__file__).parent.parent / 'src/pymcnp/inp', 3)

os.system('ruff check --fix')
os.system('ruff format')

for path in paths:
    with path.open('r') as file:
        text = file.read()
    text = re.sub(r'import numpy\n\n\n', 'import numpy\n\n', text)
    text = re.sub(r'import re\n\n\n', 'import re\n\n', text)
    text = re.sub(r'from [.] import f\n\n', 'from . import f\n', text)
    with path.open('w') as file:
        file.write(text)

for path in restore:
    os.system(f'git restore {path}')
for path in delete:
    os.system(f'rm {path}')
