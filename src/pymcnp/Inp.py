import re
import copy
import typing
import itertools
import collections
import dataclasses

import numpy

from . import abc
from . import inp


_REGEX_REPEAT = re.compile(r'(\S+) (\d+)R', re.IGNORECASE)
_REGEX_INSERT = re.compile(r'(\S+) (\d+)I (\S+)', re.IGNORECASE)
_REGEX_JUMP = re.compile(r'(?<=\s)(\d+)(J)(?=\s)', re.IGNORECASE)
_REGEX_LOG = re.compile(r'(\S+) (\d+)I?LOG (\S+)', re.IGNORECASE)
_REGEX_UNWRAPPED_CARD = re.compile(r'(?:c|[fs]c\d+)(?:\s|\Z)', re.IGNORECASE)

_WIDTH = 80
_INDENT = 5


def _wrap(line: str) -> str:
    """
    Wraps long card lines at `_WIDTH` columns with `&` continuation.

    Parameters:
        line: Line to wrap.

    Returns:
        `line` unchanged if it fits, is a comment or text card (`c`, `fc`, `sc`), or cannot be split, otherwise its wrapped lines.
    """

    if len(line) <= _WIDTH or _REGEX_UNWRAPPED_CARD.match(line):
        return line

    code, dollar, comment = line.partition('$')
    code = code.rstrip().removesuffix('&').rstrip()
    indent = ' ' * _INDENT if line.startswith(' ' * _INDENT) else ''
    words = code.split()
    if len(words) < 2:
        return line

    lines: list[str] = []
    current = indent + words[0] if indent else words[0]
    for word in words[1:]:
        if len(current) + 1 + len(word) + 2 > _WIDTH:
            lines.append(f'{current} &')
            current = ' ' * _INDENT + word
        else:
            current += f' {word}'

    lines.append(current + (f' {dollar}{comment}' if dollar else ''))
    return '\n'.join(lines)


class SpaceBlock(abc.Terminal):
    """
    Represents spaces for blocks.
    """

    _pattern = re.compile(r'(\n)([\s\S]*)', re.IGNORECASE)
    _default = '\n'


class SpaceCard(abc.Terminal):
    """
    Represents spaces for cards.
    """

    _pattern = re.compile(r'( *\n| *\$.*\n(?! {1,5})| *\n)([\s\S]*)', re.IGNORECASE)
    _default = '\n'


class Inp(abc.File):
    """
    Represents input files.

    Attributes:
        title: inp `title` card.
        cells: inp cell block.
        blank_0: inp black-line delimiter #0.
        surfaces: inp surface block.
        blank_1: inp black-line delimiter #1.
        data: inp data block.
        blank_2: inp black-line delimiter #2.
        other: inp other block.
    """

    title: typing.Annotated[abc.Terminal, r'.+\n'] | str
    cells: typing.Annotated[abc.Array, inp.card.Cell | inp.card.Comment, SpaceCard] | collections.abc.Sequence[inp.card.Cell | inp.card.Comment | str] | str = dataclasses.field(kw_only=True)
    blank_0: typing.Annotated[abc.Terminal, r' *(?:\$.*)?\n\n'] | str = abc.Terminal[r' *(?:\$.*)?\n\n']('\n\n')
    surfaces: typing.Annotated[abc.Array, inp.card.Surface | inp.card.Comment, SpaceCard] | collections.abc.Sequence[inp.card.Surface | inp.card.Comment | str] | str = dataclasses.field(kw_only=True)
    blank_1: typing.Annotated[abc.Terminal, r' *(?:\$.*)?\n\n'] | str = abc.Terminal[r' *(?:\$.*)?\n\n']('\n\n')
    data: typing.Annotated[abc.Array, inp.card.Data | inp.card.Comment, SpaceCard] | collections.abc.Sequence[inp.card.Data | inp.card.Comment | str] | str = dataclasses.field(kw_only=True)
    blank_2: typing.Annotated[abc.Terminal, r' *(?:\$.*)?(?:\n|\Z)'] | str = abc.Terminal[r' *(?:\$.*)?(?:\n|\Z)']('\n')
    other: typing.Annotated[abc.Terminal, r'\n[\s\S]*'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into input files.

        Parameters:
            source: Source string to compile.

        Returns:
            Nonterminal symbol corresponding to `source`.

        Raises:
            Error: Expected symbol.
            Error: Expected space.
        """

        assert isinstance(source, str)

        source = re.sub(r'\n +\n', '\n\n', source)

        # Preprocessing vertical data format.
        tokens = re.split(r'\n(#(?: \S+)+\n(?: *\d\S*(?: +\S+)+\n)+)', source)
        source = ''
        for token in tokens:
            if match := re.match(r'#((?: \S+)+)\n((?: *\d\S*(?: +\S+)+\n)+)', token):
                cards = re.split(r'\s+', match[1])[1:]
                rows = [[card] for card in cards]

                lines = match[2].split('\n')[:-1]
                for line in lines:
                    parameters = re.split(r'\s+', line)
                    for parameter, row in zip(parameters, rows):
                        row.append(parameter)

                source += '\n' + '\n'.join([' '.join(row) for row in rows]) + '\n'
            else:
                source += token

        # Preprocessing horizontal data format.
        source = _REGEX_REPEAT.sub(lambda match: f'{match[1]} {" ".join([match[1]] * int(match[2]))}', source)
        source = _REGEX_INSERT.sub(lambda match: ' '.join(map(str, numpy.linspace(float(match[1]), float(match[3]), num=int(match[2]) + 2))), source)
        source = _REGEX_JUMP.sub(lambda match: ' '.join([match[2]] * int(match[1])), source)
        source = _REGEX_LOG.sub(lambda match: ' '.join(map(str, numpy.geomspace(float(match[1]), float(match[3]), num=int(match[2]) + 2))), source)

        return super().from_mcnp(source)

    def to_mcnp(self) -> str:
        """
        Decompiles inps into source strings, wrapping long card lines at 80 columns.

        Returns:
            Source string corresponding to `self`.
        """

        source = super().to_mcnp()
        other = self.other.to_mcnp() if self.other != '' else ''
        body = source[: len(source) - len(other)] if other else source
        title, _, rest = body.partition('\n')

        return title + '\n' + '\n'.join(_wrap(line) for line in rest.split('\n')) + other

    def __post_init__(self) -> None:
        """
        Validates inps.
        """

        assert isinstance(self.data, abc.Array)
        assert all(isinstance(card, (inp.card.Data | inp.card.Comment)) for card in self.data)

        cell_count = sum(1 for cell in self.cells if not isinstance(cell, inp.card.Comment))

        for card in self.data:
            if isinstance(card, inp.card.data.Vol) and not (card.no != '' or len(card.x) == cell_count):
                raise abc.Error('Invalid value.', f'{card=}')

            if isinstance(card, inp.card.data.Area) and len(card.x) != cell_count:
                raise abc.Error('Invalid value.', f'{card=}')

    def scan_with(self, values: collections.abc.Iterable[typing.Any], apply: collections.abc.Callable[[typing.Self, typing.Any], None]) -> collections.abc.Iterator[typing.Self]:
        """
        Yields one deep copy of the input per value, changed by `apply`.

        Parameters:
            values: Values to scan.
            apply: Function that changes a copy for one value, e.g., `lambda inp, r: setattr(inp.surfaces[0], 'r', r)`.

        Yields:
            Independent copies, in the order of `values`. Use `list(...)` to pass them to `Run`.
        """

        for value in values:
            inp = copy.deepcopy(self)
            apply(inp, value)
            yield inp

    def scan(self, **fields: collections.abc.Iterable[typing.Any]) -> collections.abc.Iterator[typing.Self]:
        """
        Yields deep copies of the input for every combination of the values of `nps` and `seed`.

        Parameters:
            fields: Settable fields (`nps`, `seed`) with their values. With several fields, the last one varies fastest.

        Yields:
            Independent copies with the fields set. Use `list(...)` to pass them to `Run`.

        Raises:
            Error: Unknown field or no field.
        """

        unknown = [name for name in fields if name not in ('nps', 'seed')]
        if unknown or not fields:
            raise abc.Error('Invalid value.', f'cannot scan {unknown or "nothing"}; use `scan_with` for other fields')

        values = [list(value) for value in fields.values()]
        for combination in itertools.product(*values):
            inp = copy.deepcopy(self)
            for name, value in zip(fields, combination):
                setattr(inp, name, value)
            yield inp

    def _find(self, cards: collections.abc.Iterable[typing.Any], number: int | str, attribute: str, *types: type) -> typing.Any:
        wanted = int(str(number).strip())
        for card in cards:
            if (not types or isinstance(card, types)) and hasattr(card, attribute) and int(str(getattr(card, attribute)).strip()) == wanted:
                return card
        kind = types[0].__name__ if types else 'Card'
        raise abc.Error('Card not found.', f'{kind} {number=}')

    def cell(self, number: int | str) -> inp.card.Cell:
        """
        Returns the cell card with this number.

        Raises:
            Error: Cell not found.
        """

        return self._find(self.cells, number, 'j', inp.card.Cell)

    def surface(self, number: int | str) -> inp.card.Surface:
        """
        Returns the surface card with this number.

        Raises:
            Error: Surface not found.
        """

        return self._find(self.surfaces, number, 'j', inp.card.Surface)

    def material(self, number: int | str) -> inp.card.data.M:
        """
        Returns the `M` card of this material.

        Raises:
            Error: Material not found.
        """

        return self._find(self.data, number, 'suffix', inp.card.data.M)

    def tally(self, number: int | str) -> inp.card.data.F | inp.card.data.Fmesh:
        """
        Returns the `F` or `FMESH` card of this tally.

        Raises:
            Error: Tally not found.
        """

        return self._find(self.data, number, 'suffix', inp.card.data.F, inp.card.data.Fmesh)

    def cells_with_material(self, number: int | str) -> list[inp.card.Cell]:
        """
        Returns the cells filled with this material, in file order.
        This includes `LIKE n BUT` cells, which have the material of cell `n` unless a `MAT=` option replaces it.
        """

        wanted = int(str(number).strip())

        def material(cell: typing.Any, seen: tuple[int, ...] = ()) -> int | None:
            if hasattr(cell, 'like'):
                for option in cell.options:
                    if isinstance(option, inp.option.cell.Mat):
                        return int(str(option.m).strip())
                origin = int(str(cell.n).strip())
                return None if origin in seen else material(self.cell(origin), (*seen, int(str(cell.j).strip())))
            return int(str(cell.m).strip()) if hasattr(cell, 'm') else None

        return [cell for cell in self.cells if isinstance(cell, inp.card.Cell) and material(cell) == wanted]

    @property
    def nps(self) -> inp.literal.Integer | None:
        """
        Input file nps.

        Raises:
            Error.
        """

        assert isinstance(self.data, abc.Array)
        assert all(isinstance(card, (inp.card.Data | inp.card.Comment)) for card in self.data)

        for card in self.data:
            if not isinstance(card, inp.card.data.Nps):
                continue

            return card.npp
        return None

    @nps.setter
    def nps(self, nps: inp.literal.Integer | int | str) -> None:
        """
        Sets input file nps.

        Parameters:
            nps: Nps to set.

        Raises:
            Error.
        """

        assert isinstance(self.data, abc.Array)
        assert all(isinstance(card, (inp.card.Data | inp.card.Comment)) for card in self.data)

        for card in self.data:
            if not isinstance(card, inp.card.data.Nps):
                continue

            card.npp = nps
            break
        else:
            card = inp.card.data.Nps(npp=nps)
            self.data.append(card)

    @property
    def seed(self) -> inp.literal.Integer | None:
        """
        Input file seed.

        Raises:
            Error.
        """

        assert isinstance(self.data, abc.Array)
        assert all(isinstance(card, (inp.card.Data | inp.card.Comment)) for card in self.data)

        for card in self.data:
            if not isinstance(card, inp.card.data.Rand):
                continue

            if isinstance(card.options, abc.Terminal[r'']):
                continue

            for option in card.options:
                if not isinstance(option, inp.option.data.rand.Seed):
                    continue

                return option.value
            return None
        return None

    @seed.setter
    def seed(self, seed: inp.literal.Integer | int | str) -> None:
        """
        Sets input file seed.

        Parameters:
            seed: Seed to set.

        Raises:
            Error.
        """

        assert isinstance(self.data, abc.Array)
        assert all(isinstance(card, (inp.card.Data | inp.card.Comment)) for card in self.data)

        for card in self.data:
            if not isinstance(card, inp.card.data.Rand):
                continue

            if isinstance(card.options, abc.Terminal[r'']):
                card.options = [inp.option.data.rand.Seed(value=seed)]
                return

            for option in card.options:
                if not isinstance(option, inp.option.data.rand.Seed):
                    continue

                option.value = seed
                return

            option = inp.option.data.rand.Seed(value=seed)
            card.options.append(option)
            return

        option = inp.option.data.rand.Seed(value=seed)
        card = inp.card.data.Rand(options=[option])
        self.data.append(card)
        return
