import re


def has_suffix(element):
    return 'suffix' in [attribute.name for attribute in element.attributes]


def has_designator(element):
    return 'designator' in [attribute.name for attribute in element.attributes]


def T(t):
    return '    ' * t


def U(word):
    word = re.sub('/', '_', word)
    return word.upper()


def L(word):
    # word = re.sub('/', '_', word)
    return word.lower()


def C(word):
    word = re.sub('_', '', word)
    word = re.sub('/', '_', word)
    return word[0].upper() + word[1:].lower()


def P(word):
    word = re.sub('/', '_', word)
    return word.lower()


def LIST_N(element):
    optional = filter(lambda attribute: attribute.optional, element.attributes)
    required = filter(lambda attribute: not attribute.optional, element.attributes)
    attributes = list(required) + list(optional)

    return ', '.join(f'{attribute.name}' for attribute in attributes).strip()


def LIST_N_NSD(element):
    optional = filter(lambda attribute: attribute.optional, element.attributes)
    required = filter(lambda attribute: not attribute.optional, element.attributes)
    attributes = list(required) + list(optional)

    return ', '.join(
        f'{attribute.name}'
        for attribute in filter(
            lambda attribute: attribute.name not in {'suffix', 'designator'}, attributes
        )
    ).strip()


def LIST_NT(element):
    optional = filter(lambda attribute: attribute.optional, element.attributes)
    required = filter(lambda attribute: not attribute.optional, element.attributes)
    attributes = list(required) + list(optional)

    return ', '.join(f'{attribute.name}: {attribute.type}' for attribute in attributes).strip()


def LIST_NTO(element):
    optional = filter(lambda attribute: attribute.optional, element.attributes)
    required = filter(lambda attribute: not attribute.optional, element.attributes)
    attributes = list(required) + list(optional)

    return ', '.join(
        f'{attribute.name}: {attribute.type}'
        if not attribute.optional
        else f'{attribute.name}: {attribute.type} = None'
        for attribute in attributes
    ).strip()


def COMMENT(element, t):
    return '\n'.join(
        f'{T(t)}{attribute.name}: {attribute.description}.' for attribute in element.attributes
    ).strip()


def ERROR(element, t):
    return '\n'.join(
        f'{T(t)}McnpError: {attribute.error}.' for attribute in element.attributes
    ).strip()


def ASSIGN(element, t):
    o = ''

    for attribute in element.attributes:
        if attribute.name == 'options':
            o += f'{T(t)}self.{attribute.name}: typing.Final[dict[str, {attribute.type[6:-1]}]] = {{val._KEYWORD: val for val in {attribute.name}}} if options else None\n'
        else:
            o += f'{T(t)}self.{attribute.name}: typing.Final[{attribute.type}] = {attribute.name}\n'

    return o.strip()

    o += '\n'.join(
        f'{T(t)}self.{attribute.name}: typing.Final[{attribute.type}] = {attribute.name}'
        for attribute in element.attributes
    ).strip()


def CHECK(element, t):
    o = ''

    for attribute in element.attributes:
        if attribute.optional:
            if attribute.restriction:
                o += f'{T(t)}if {attribute.name} is not None and not ({attribute.restriction}):\n'
            else:
                continue
        else:
            if attribute.restriction:
                o += f'{T(t)}if {attribute.name} is None or not ({attribute.restriction}):\n'
            else:
                o += f'{T(t)}if {attribute.name} is None:\n'

        o += f'{T(t)}   raise errors.McnpError(errors.McnpCode.{attribute.error}, {attribute.name})\n'

    return o.strip()


def MATCH(element, t):
    o = ''
    i = 1

    if has_suffix(element):
        o += f'{T(t)}suffix = types.Integer.from_mcnp(tokens[{i}])\n'
        i += 1
    if has_designator(element):
        o += f'{T(t)}designator = types.Designator.from_mcnp(tokens[{i}])\n'
        i += 1

    for j, attribute in enumerate(element.attributes):
        if attribute.name in {'suffix', 'designator'}:
            continue

        if 'tuple' in attribute.type:
            if 'Option_' in attribute.type:
                o += f'{T(t)}{attribute.name} = types._Tuple(tuple(_parser.process_inp_option({attribute.type[6:-1]}, tokens[{i + j}])))'
            elif 'Entry' in attribute.type:
                o += f'{T(t)}{attribute.name} = types._Tuple([{attribute.type[6:-1]}.from_mcnp(token[0]) for token in {attribute.type[6:-1]}._REGEX.finditer(tokens[{i + j}])])'
            else:
                o += f'{T(t)}{attribute.name} = types._Tuple([{attribute.type[6:-1]}.from_mcnp(token[0]) for token in re.finditer(r"( \\S+)", tokens[{i + j}])])'
        else:
            if 'Option_' in attribute.type:
                o += f'{T(t)}{attribute.name} = next(_parser.process_inp_option({attribute.type}, tokens[{i + j}]))'
            else:
                o += f'{T(t)}{attribute.name} = {attribute.type}.from_mcnp(tokens[{i + j}])'

        if attribute.optional:
            o += f' if tokens[{i + j}] else None\n'
        else:
            o += '\n'

    return o.strip()


def REGEX(element):
    o = ''

    for attribute in element.attributes:
        if attribute.name in {'suffix', 'designator'}:
            continue

        o += _REGEX(attribute.type, attribute.optional, element.options, element.entries)

    return o


def _REGEX(type, optional, options, entries):
    o = ''

    if 'tuple' in type:
        if 'Option' in type:
            o += f'(( ({r'|'.join(f"(({option.mnemonic}){_REGEX_OPTION(option)})" for option in options)}))+)'
        elif 'Entry' in type:
            o += f'(({REGEX(next(filter(lambda entry: C(entry.name) in type, entries)))})+)'
        else:
            o += '(( \\S+)+)'
    else:
        if 'Option' in type:
            o += f' ({r'|'.join(f"(({option.mnemonic}){_REGEX_OPTION(option)})" for option in options)})'
        elif 'Entry' in type:
            o += f'( {REGEX(next(filter(lambda entry: C(entry.name) in type, entries)))})'
        else:
            o += '( \\S+)'

    if optional:
        o += '?'

    return o


def _REGEX_OPTION(option):
    o = f"{"(\\d+?)" if has_suffix(option) else ""}{":(\\S+?)" if has_designator(option) else ""}{REGEX(option)}"

    return o


def _OPTION(name, comment, options, d):
    return f'''
import re
import enum
import typing

from .{'.' * d} import _option
from ..{'.' * d}utils import types
from ..{'.' * d}utils import errors
from ..{'.' * d}utils import _parser


class {C(name)}Option_(_option.InpOption_):
    """
    Represents generic INP {comment} options.
    """

    _KEYWORD = ''

    _SUBCLASSES = {{}}

    _REGEX = re.compile(
        r"{_REGEX(f'{C(name)}Option_', False, options, None)[1:]}"
    )

    def __init_subclass__(cls, keyword: str):
        cls._KEYWORD: typing.Final[str] = keyword

        if keyword not in cls._SUBCLASSES:
            cls._SUBCLASSES[keyword] = [cls]
        else:
            cls._SUBCLASSES[keyword] += [cls]

    def __class_getitem__(cls, keyword: str):
        return cls._SUBCLASSES[keyword]
'''


def OPTION(name, comment, option, d):
    return f'''
import re
import typing
import itertools
{f'\nfrom . import {L(option.name)}\n' if option.options or option.entries else '\n'}from . import _option
from ..{'.' * d}utils import types
from ..{'.' * d}utils import errors
from ..{'.' * d}utils import _parser


class {C(name)}Option_{C(option.name)}(_option.{C(name)}Option_, keyword="{L(option.mnemonic)}"):
    """
    Represents INP {comment} {L(option.name)} options.

    Attributes:
        {COMMENT(option, 2)}
    """

    _REGEX = re.compile(
        rf"\\A{option.mnemonic}{_REGEX_OPTION(option)}\\Z"
    )

    def __init__(self, {LIST_NTO(option)}):
        """
        Initializes ``{C(name)}Option_{C(option.name)}``.

        Parameters:
            {COMMENT(option, 3)}

        Returns:
            ``{C(name)}Option_{C(option.name)}``.

        Raises:
            {ERROR(option, 3)}
        """

        {CHECK(option, 2)}

        self.value: typing.Final[tuple[any]] = types._Tuple([{LIST_N_NSD(option)}])
        {ASSIGN(option, 2)}

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``{C(name)}Option_{C(option.name)}`` from INP.

        Parameters:
            source: INP {comment} option.

        Returns:
            ``{C(name)}Option_{C(option.name)}``.

        Raises:
            McnpError: SYNTAX_{U(name)}_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = {C(name)}Option_{C(option.name)}._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_{U(name)}_OPTION, source)

        {MATCH(option, 2)}

        return {C(name)}Option_{C(option.name)}({LIST_N(option)})
'''[1:]


def _ENTRY(name, comment, entries, d):
    return f'''
from .{'.' * d} import _entry
from ..{'.' * d}utils import types
from ..{'.' * d}utils import errors
from ..{'.' * d}utils import _parser

class {C(name)}Entry_(_entry.InpEntry_):
    """
    Represents generic INP {comment} entry.
    """

    pass
'''[1:]


def ENTRY(name, comment, entry, d):
    return f'''
import re
import typing
import itertools
{f'\nfrom . import {L(entry.name)}\n' if entry.options or entry.entries else '\n'}from . import _entry
from ..{'.' * d}utils import types
from ..{'.' * d}utils import errors
from ..{'.' * d}utils import _parser


class {C(name)}Entry_{C(entry.name)}(_entry.{C(name)}Entry_):
    """
    Represents INP {comment} {L(entry.name)} entries.

    Attributes:
        {COMMENT(entry, 2)}
    """

    _REGEX = re.compile(
        rf"{REGEX(entry)}"
    )

    def __init__(self, {LIST_NTO(entry)}):
        """
        Initializes ``{C(name)}Entry_{C(entry.name)}``.

        Parameters:
            {COMMENT(entry, 3)}

        Returns:
            ``{C(name)}Entry{C(entry.name)}``.

        Raises:
            McnpError: SEMANTICS_DATA_ENTRY_VALUE.
        """

        {CHECK(entry, 2)}

        self.parameters: typing.Final[tuple[any]] = types._Tuple([{LIST_N(entry)}])
        {ASSIGN(entry, 2)}

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``{C(name)}Entry_{C(entry.name)}`` from INP.

        Parameters:
            INP for ``{C(name)}Entry_{C(entry.name)}``.

        Returns:
            ``{C(name)}Entry_{C(entry.name)}``.

        Raises:
            McnpError: SYNTAX_{U(name)}_ENTRY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = {C(name)}Entry_{C(entry.name)}._REGEX.match(' ' + source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_{U(name)}_ENTRY, source)

        {MATCH(entry, 2)}

        return {C(name)}Entry_{C(entry.name)}({LIST_N(entry)})
'''[1:]


def INIT(element, start):
    o = ''
    a = ''

    if element.options:
        a += f'from {start}._option import {C(element.name)}Option_\n'
        o += f'from ._option import {C(element.name)}Option_\n'
        for option in element.options:
            a += f'from {start}.option_{re.sub('/', '_', option.name)} import {C(element.name)}Option_{C(option.name)}\n'
            o += f'from .option_{re.sub('/', '_', option.name)} import {C(element.name)}Option_{C(option.name)}\n'

        for option in element.options:
            if option.options or option.entries:
                a += f'from {start} import {option.name}\n'
                a += INIT(option, f'{start}.{P(option.name)}')[0]
                o += f'from . import {option.name}\n'
                o += INIT(option, f'.{P(option.name)}')[0]

    if element.entries:
        a += f'from {start}._entry import {C(element.name)}Entry_\n'
        o += f'from ._entry import {C(element.name)}Entry_\n'
        for entry in element.entries:
            a += f'from {start}.entry_{re.sub('/', '_', entry.name)} import {C(element.name)}Entry_{C(entry.name)}\n'
            o += f'from .entry_{re.sub('/', '_', entry.name)} import {C(element.name)}Entry_{C(entry.name)}\n'

        for entry in element.entries:
            if entry.options or entry.entries:
                a += f'from {start} import {entry.name}\n'
                a += INIT(entry, f'{start}.{P(entry.name)}')[0]
                o += f'from . import {entry.name}\n'
                o += INIT(entry, f'.{P(entry.name)}')[0]

    b = ''
    o += '\n__all__=[\n'

    if element.options:
        b += f'\t"{C(element.name)}Option_",\n'
        o += f'\t"{C(element.name)}Option_",\n'
        for option in element.options:
            b += f'\t"{C(element.name)}Option_{C(option.name)}",\n'
            o += f'\t"{C(element.name)}Option_{C(option.name)}",\n'

        for option in element.options:
            if option.options or option.entries:
                b += f'\t"{option.name}",\n'
                b += INIT(option, start)[1]
                o += f'\t"{option.name}",\n'
                o += INIT(option, start)[1]

    if element.entries:
        b += f'\t"{C(element.name)}Entry_",\n'
        o += f'\t"{C(element.name)}Entry_",\n'
        for entry in element.entries:
            b += f'\t"{C(element.name)}Entry_{C(entry.name)}",\n'
            o += f'\t"{C(element.name)}Entry_{C(entry.name)}",\n'

        for entry in element.entries:
            if entry.options or entry.entries:
                b += f'\t"{entry.name}",\n'
                b += INIT(entry, start)[1]
                o += f'\t"{entry.name}",\n'
                o += INIT(entry, start)[1]

    o += ']\n'

    return a, b, o
