import pathlib

import _data
import _code


EXCLUDE = [
    # CELL
    'geometry',
    # SURFACE
    'px',
    'py',
    'pz',
    'so',
    's',
    'sx',
    'sy',
    'sz',
    'c/x',
    'c/y',
    'c/z',
    'cx',
    'cy',
    'cz',
    'k/x',
    'k/y',
    'k/z',
    'kx',
    'ky',
    'kz',
    'sq',
    'gq',
    'tx',
    'ty',
    'tz',
    'x',
    'y',
    'z',
    'box',
    'rpp',
    'sph',
    'rcc',
    'rhp',
    'rec',
    'trc',
    'ell',
    'wed',
    'arb',
    # DATA
    'm',
]


def help(objobj, obj, comment, path, d):
    # ENTRIES
    if obj.entries:
        # ABSTRACT
        filename = path / '_entry.py'
        with filename.open('w') as file:
            file.write(_code._ENTRY(obj.name, comment, obj.entries, d))

        # CONCRETE
        for entry in obj.entries:
            if entry.name in EXCLUDE:
                continue

            filename = path / f'entry_{_code.P(entry.name)}.py'
            with filename.open('w') as file:
                file.write(_code.ENTRY(obj.name, comment, entry, d))

            if entry.options or entry.entries:
                filename = path / f'{entry.name}/'
                filename.mkdir(exist_ok=True)
                help(obj, entry, comment + f' {obj.name} entry', filename, d + 1)

    # OPTIONS
    if obj.options:
        # ABSTRACT
        filename = path / '_option.py'
        with filename.open('w') as file:
            file.write(_code._OPTION(obj.name, comment, obj.options, d))

        # CONCRETE
        for option in obj.options:
            if option.name in EXCLUDE:
                continue

            filename = path / f'option_{_code.P(option.name)}.py'
            with filename.open('w') as file:
                file.write(_code.OPTION(obj.name, comment, option, d))

            if option.options or option.entries:
                filename = path / f'{option.name}/'
                filename.mkdir(exist_ok=True)
                help(obj, option, comment + f' {obj.name} option', filename, d + 1)

    # __INIT__
    filename = path / '__init__.py'
    with filename.open('w') as file:
        a, b, o = _code.INIT(obj, '.')
        file.write(o)


a = ''
b = ''

for card in _data.CARDS:
    filename = pathlib.Path(__file__).parent / f'./inp/{card.name}'
    filename.mkdir(exist_ok=True)

    # print(card.name)
    # print(_code.REGEX(card))
    # print(_code.MATCH(card, 0))
    # print()
    hello = _code.INIT(card, f'.{card.name}')
    a += hello[0]
    b += hello[1]

    help(None, card, f'{card.name} card', filename, 1)

print(
    f"""
from ._card import InpCard_
from ._entry import InpEntry_
from ._option import InpOption_
from .card_cell import Cell
from .card_surface import Surface
from .card_data import Data
from .card_comment import Comment
from .inp import Inp
{a}

__all__ = [
    "InpCard_",
    "InpEntry_",
    "InpOption_",
    "Cell",
    "Surface",
    "Data",
    "Comment",
    "Inp",
    {b}
]
"""[1:-1]
)
