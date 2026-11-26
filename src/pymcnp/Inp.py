import re
import typing
import warnings

import numpy

from . import abc
from . import inp


_REGEX_REPEAT = re.compile(r'(\S+) (\d+)R', re.IGNORECASE)
_REGEX_INSERT = re.compile(r'(\S+) (\d+)I (\S+)', re.IGNORECASE)
_REGEX_JUMP = re.compile(r'(?<!\S)(\d+)(J)(?!\S)', re.IGNORECASE)
_REGEX_LOG = re.compile(r'(\S+) (\d+)I?LOG (\S+)', re.IGNORECASE)
_REGEX_UNWRAPPED_CARD = re.compile(r'(?:c|[fs]c\d+)(?:\s|\Z)', re.IGNORECASE)
_REGEX_COMMENT = re.compile(r' {0,4}c(?:\s|\Z)', re.IGNORECASE)

_WIDTH = 80
_INDENT = 5


def _expand(code: str) -> str:
    """
    Expands the horizontal data format shorthands (``nR``, ``nI``, ``nJ``, ``nLOG``) of one line of card text.

    Parameters:
        code: Card text, without a ``$`` comment.

    Returns:
        ``code`` with its shorthands written out.
    """

    code = _REGEX_REPEAT.sub(lambda match: f'{match[1]} {" ".join([match[1]] * int(match[2]))}', code)
    code = _REGEX_INSERT.sub(lambda match: ' '.join(map(str, numpy.linspace(float(match[1]), float(match[3]), num=int(match[2]) + 2))), code)
    code = _REGEX_JUMP.sub(lambda match: ' '.join([match[2]] * int(match[1])), code)
    code = _REGEX_LOG.sub(lambda match: ' '.join(map(str, numpy.geomspace(float(match[1]), float(match[3]), num=int(match[2]) + 2))), code)
    return code


def _expand_cards(source: str) -> str:
    """
    Expands the horizontal data format shorthands in the cards of an input file.

    The title, comment cards, ``$`` comments and the text after the data block are left verbatim.

    Parameters:
        source: Input file text, with blank lines already empty.

    Returns:
        ``source`` with the shorthands of its cards written out.
    """

    title, newline, rest = source.partition('\n')
    lines = []
    blanks = 0
    for line in rest.split('\n'):
        if blanks < 3 and line and not _REGEX_COMMENT.match(line):
            code, dollar, comment = line.partition('$')
            line = _expand(code) + dollar + comment

        blanks += not line
        lines.append(line)

    return title + newline + '\n'.join(lines)


def _wrap(line: str) -> str:
    """
    Wraps long card lines at ``_WIDTH`` columns with ``&`` continuation.

    Parameters:
        line: Line to wrap.

    Returns:
        ``line`` unchanged if it fits, is a comment or text card (``c``, ``fc``, ``sc``), or cannot be split, otherwise its wrapped lines.
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

    _pattern = re.compile(r'(\n)', re.IGNORECASE)
    _default = '\n'


class SpaceCard(abc.Terminal):
    """
    Represents spaces for cards.
    """

    _pattern = re.compile(r'( *\n| *\$.*\n(?! {1,5})| *\n)', re.IGNORECASE)
    _default = '\n'


class Inp(abc.File):
    """
    Represents input files.

    Attributes:
        title: inp ``title`` card.
        cells: inp cell block.
        blank_0: inp black-line delimiter #0.
        surfaces: inp surface block.
        blank_1: inp black-line delimiter #1.
        data: inp data block.
        blank_2: inp black-line delimiter #2.
        other: inp other block.
    """

    title: typing.Annotated[abc.Terminal, r'.+\n']
    cells: typing.Annotated[abc.Array, inp.card.Cell | inp.card.Comment, SpaceCard]
    blank_0: typing.Annotated[abc.Terminal, r' *(?:\$.*)?\n\n'] = abc.Terminal[r' *(?:\$.*)?\n\n']('\n\n')
    surfaces: typing.Annotated[abc.Array, inp.card.Surface | inp.card.Comment, SpaceCard]
    blank_1: typing.Annotated[abc.Terminal, r' *(?:\$.*)?\n\n'] = abc.Terminal[r' *(?:\$.*)?\n\n']('\n\n')
    data: typing.Annotated[abc.Array, inp.card.Data | inp.card.Comment, SpaceCard]
    blank_2: typing.Annotated[abc.Terminal, r' *(?:\$.*)?(?:\n|\Z)'] = abc.Terminal[r' *(?:\$.*)?(?:\n|\Z)']('\n')
    other: typing.Annotated[abc.Terminal, r'\n[\s\S]*'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates input files.
        """

        cell_numbers = set()
        for card in (cells := self.cells.filter(inp.card.Cell)):
            if isinstance(card, inp.card.Cell_2):
                if card.n not in cell_numbers:
                    raise abc.Error('Invalid value.', f'{card.n=}')

                card.material(cells)

            if card.j in cell_numbers:
                raise abc.Error('Invalid value.', f'{card.j=}')

            cell_numbers.add(card.j)

        surface_numbers = set()
        for card in self.surfaces.filter(inp.card.Surface):
            if card.j in surface_numbers:
                raise abc.Error('Invalid value.', f'{card.j=}')

            surface_numbers.add(card.j)

        cell_count = len(cell_numbers)
        for card in self.data.filter(inp.card.Data):
            if isinstance(card, inp.card.data.Vol) and card.no == '' and len(card.x) != cell_count:
                raise abc.Error('Invalid value.', f'{card=}')

            if isinstance(card, inp.card.data.Area) and len(card.x) != cell_count:
                raise abc.Error('Invalid value.', f'{card=}')

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into input files.

        Parameters:
            source: Source string to compile.

        Returns:
            Nonterminal symbol corresponding to ``source``.

        Raises:
            Error: Expected symbol.
            Error: Expected space.
        """

        for line in re.finditer(r'[^\n]{81}', source):
            warnings.warn(abc.Warning('Line exceeds 80 characters maximum length', f'{line[0]}'))

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
        source = _expand_cards(source)

        return super().from_mcnp(source)

    def to_mcnp(self) -> str:
        """
        Decompiles inps into source strings, wrapping long card lines at 80 columns.

        Returns:
            Source string corresponding to ``self``.
        """

        assert isinstance(self.other, abc.Terminal)

        source = super().to_mcnp()
        body = source[: len(source) - len(self.other)] if self.other else source
        title, _, rest = body.partition('\n')

        return title + '\n' + '\n'.join(_wrap(line) for line in rest.split('\n')) + self.other

    @property
    def nps(self) -> inp.literal.Integer | None:
        """
        Input file nps.
        """

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
        """

        nps = inp.literal.Integer(str(nps))

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
        """

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
        """

        seed = inp.literal.Integer(str(seed))

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
        card = inp.card.data.Rand(options=abc.Array[inp.option.data.Rand, None](option))
        self.data.append(card)
        return

    def cell_cards(
        self,
        number: inp.literal.Integer | int | str | None = None,
        material: inp.literal.Integer | int | str | None = None,
        density: inp.literal.Real | float | int | str | None = None,
        kind: type[inp.card.Cell] = inp.card.Cell,
    ) -> tuple[inp.card.Cell, ...]:
        """
        Gets input file cell cards.

        Parameters:
            number: Cell card number to get.
            material: Cell card material to get.
            density: Cell card density to get.
            kind: Cell card type to get.

        Returns:
            Cell cards with number ``number``, material ``material``, density ``density``, if specified, and kind ``kind``.
        """

        every = self.cells.filter(kind)

        number_matches = every
        material_matches = every
        density_matches = every

        if number is not None:
            number = inp.literal.Integer(str(number))
            number_matches = self.cells.filter(kind, j=number)

        if material is not None:
            material = inp.literal.Integer(str(material))
            material_matches = tuple((cell for cell in every if cell.material(every) == material))

        if density is not None:
            density = inp.literal.Real(str(density))
            density_matches = tuple((cell for cell in every if cell.density(every) == density))

        return tuple((cell for cell in every if cell in number_matches and cell in material_matches and cell in density_matches))

    def surface_cards(self, number: inp.literal.Integer | int | str | None = None, kind: type[inp.card.Surface] = inp.card.Surface) -> tuple[inp.card.Surface, ...]:
        """
        Gets input file surface cards.

        Parameters:
            number: Surface card number to get.
            kind: Surface card type to get.

        Returns:
            Surface cards with ``number`` number, if specified, and kind ``kind``.
        """

        every = self.surfaces.filter(kind)

        number_matches = every

        if number is not None:
            number = inp.literal.Integer(str(number))
            number_matches = self.surfaces.filter(kind, j=number)

        return tuple(number_matches)

    def data_cards(self, kind: type[inp.card.Data] = inp.card.Data) -> tuple[inp.card.Data, ...]:
        """
        Gets input file data cards.

        Parameters:
            kind: Data card type to get.

        Returns:
            Data cards with kind ``kind``.
        """

        every = self.data.filter(kind)

        return tuple(every)

    def comment_cards(self) -> tuple[tuple[inp.card.Comment, ...], tuple[inp.card.Comment, ...], tuple[inp.card.Comment, ...]]:
        """
        Gets input file comment cards.

        Returns:
            Comment cards from the cell, surface, and data card blocks, respectively.
        """

        return (
            tuple(self.cells.filter(inp.card.Comment)),
            tuple(self.surfaces.filter(inp.card.Comment)),
            tuple(self.data.filter(inp.card.Comment)),
        )
