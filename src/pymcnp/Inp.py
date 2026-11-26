import re
import typing
import warnings

from . import abc
from . import inp
from .abc.Symbol import _unix_newlines
from .inp._shorthand import _expand_lines
from .inp._shorthand import _REGEX_COMMENT
from .abc._path import _join
from .abc._path import _steps


_REGEX_UNWRAPPED_CARD = re.compile(r' {0,4}(?:c|[fs]c\d+)(?:\s|\Z)', re.IGNORECASE)
# Vertical data format: a ``#`` in columns 1-5 followed by card names, then one row of entries per line. Rows start with
# a number or a jump, so the next card ends the block, and they carry no ``$`` comment.
_REGEX_VERTICAL_HEADER = re.compile(r' {0,4}#((?:[ \t]+[^\s$]+)+)[ \t]*\Z')
_REGEX_VERTICAL_ROW = re.compile(r'[ \t]*(?:[-+]?\.?\d|\d*J(?:\s|\Z))[^$]*\Z', re.IGNORECASE)
# A shorthand in a row is not one entry of one card (``2J`` jumps over two cards), so a row with one is not read.
_REGEX_VERTICAL_SHORTHAND = re.compile(r'\d+J|[-+]?(?:\d+\.?\d*|\.\d+)(?:E[-+]?\d+)?(?:R|I|M|I?LOG)', re.IGNORECASE)

# The message block: ``message:`` in column 1, up to and including the first blank line.
_REGEX_MESSAGE = re.compile(r'message:[\s\S]*?\n\n', re.IGNORECASE)

_WIDTH = 80
_INDENT = 5


def _vertical_block(lines: list[str], index: int) -> tuple[list[str], int] | None:
    """
    Reads one vertical data format block.

    Parameters:
        lines: Lines of an input file.
        index: Index of the line that may start a block.

    Returns:
        The block's cards in horizontal format and the index of the line after the block, or None if no block starts at
        ``index``, its rows do not each have one entry per card name, or a row holds a shorthand (``nJ``, ``nR``, ``nI``,
        ``nLOG``, ``xM``). Such a block stays as it is, so it ends the data block and is left in the remainder instead of
        being read wrong.
    """

    header = _REGEX_VERTICAL_HEADER.match(lines[index])
    if header is None:
        return None

    names = header[1].split()
    rows = []
    end = index + 1
    while end < len(lines) and _REGEX_VERTICAL_ROW.match(lines[end]):
        rows.append(lines[end].split())
        end += 1

    if not rows or any(len(row) != len(names) or any(map(_REGEX_VERTICAL_SHORTHAND.fullmatch, row)) for row in rows):
        return None

    return [' '.join([name, *(row[column] for row in rows)]) for column, name in enumerate(names)], end


def _vertical(source: str) -> str:
    """
    Rewrites the vertical data format blocks of an input file in horizontal format, one card per line in place of the block.

    The title and the text after the data block are left verbatim.

    Parameters:
        source: Input file text, with blank lines already empty.

    Returns:
        ``source`` with its vertical data format blocks rewritten.
    """

    lines = source.split('\n')
    result = lines[:1]
    blanks = 0
    index = 1
    while index < len(lines):
        if blanks < 3 and (block := _vertical_block(lines, index)) is not None:
            cards, index = block
            result += cards
            continue

        blanks += not lines[index]
        result.append(lines[index])
        index += 1

    return '\n'.join(result)


def _expand_cards(source: str) -> str:
    """
    Expands the horizontal data format shorthands in the cards of an input file.

    The title, comment cards, ``$`` comments, text cards (``fc``, ``sc``) and the text after the data block are left verbatim.

    Parameters:
        source: Input file text, with blank lines already empty.

    Returns:
        ``source`` with the shorthands of its cards written out.
    """

    title, newline, rest = source.partition('\n')
    lines = rest.split('\n')
    # The cell, surface and data blocks end at the third blank line.
    end = len(lines)
    blanks = 0
    for index, line in enumerate(lines):
        blanks += not line
        if blanks == 3:
            end = index
            break

    return title + newline + '\n'.join(_expand_lines(lines[:end]) + lines[end:])


def _wrap(line: str) -> str:
    """
    Wraps long card lines at ``_WIDTH`` columns with ``&`` continuation.

    Parameters:
        line: Line to wrap.

    Returns:
        ``line`` unchanged if it fits, is a comment or text card (``c``, ``fc``, ``sc``) starting in columns 1-5, or cannot be
        split, otherwise its wrapped lines. A ``$`` comment stays at the end of the last line.
    """

    if len(line) <= _WIDTH or _REGEX_UNWRAPPED_CARD.match(line):
        return line

    code, dollar, comment = line.partition('$')
    code = code.rstrip()
    # A line that ends in ``&`` is continued on the next line, so its last wrapped line keeps the ``&``.
    continued = code.endswith('&')
    code = code.removesuffix('&').rstrip()
    # The first line keeps an indent of 1-4 spaces, so a continuation line in columns 2-5 stays one; a deeper indent is
    # reset to ``_INDENT`` spaces, so the line can still be shortened.
    indent = line[: min(len(line) - len(line.lstrip(' ')), _INDENT)]
    words = code.split()
    if len(words) < 2:
        return line

    lines: list[str] = []
    current = indent + words[0]
    for word in words[1:]:
        if len(current) + 1 + len(word) + 2 > _WIDTH:
            lines.append(f'{current} &')
            current = ' ' * _INDENT + word
        else:
            current += f' {word}'

    lines.append(current + (' &' if continued else '') + (f' {dollar}{comment}' if dollar else ''))
    return '\n'.join(lines)


def _title_line(lines: list[str]) -> int:
    """
    Finds the title card of an INP file, after its ``message:`` block if it has one.

    Parameters:
        lines: Lines of the INP file.

    Returns:
        Index of the title card's line.
    """

    if lines and lines[0].lower().startswith('message:'):
        for index, line in enumerate(lines):
            if not line.strip():
                return index + 1

    return 0


def _unparseable_card(lines: list[str]) -> tuple[int, abc.Error] | None:
    """
    Finds the first card of an INP file that PyMCNP cannot parse.

    Comment cards are skipped, and each card is parsed as ``Inp`` parses it:
    shorthands expanded, without ``$`` comments, to its end.

    Parameters:
        lines: Lines of the INP file.

    Returns:
        Number of the card's first line, counting from 1, and the error, or
        None if every card parses.
    """

    index = _title_line(lines) + 1
    for union in (inp.card.Cell, inp.card.Surface, inp.card.Data):
        while index < len(lines) and not lines[index].strip():
            index += 1

        cards = []
        while index < len(lines) and lines[index].strip():
            line = lines[index]
            if (block := _vertical_block(lines, index)) is not None:
                # Vertical data format is only valid across the whole block.
                index = block[1]
                continue

            if _REGEX_COMMENT.match(line):
                # Comment cards are not cards to parse, but count as lines.
                index += 1
                continue

            # Cards are parsed without ``$`` comments; ``from_mcnp`` expands their shorthands as ``Inp`` does.
            code = line.partition('$')[0].rstrip()
            if cards and (re.match(r'\s', line) or cards[-1][1][-1].endswith('&')):
                cards[-1][1].append(code)
            else:
                cards.append((index + 1, [code]))
            index += 1

        for number, card in cards:
            try:
                rest = union.from_mcnp('\n'.join(card))[1]
                if rest.strip():
                    raise abc.Error(f'Expected end of card at {rest.strip().split()[0]!r}.', f'{rest=}')
            except abc.Error as card_err:
                return number, card_err

    return None


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
        message: inp ``message:`` block, up to and including its blank line, or None.
        title: inp ``title`` card.
        cells: inp cell block.
        blank_0: inp black-line delimiter #0.
        surfaces: inp surface block.
        blank_1: inp black-line delimiter #1.
        data: inp data block.
        blank_2: inp black-line delimiter #2.
        other: inp other block.
    """

    message: typing.Annotated[abc.Terminal, _REGEX_MESSAGE.pattern] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    title: typing.Annotated[abc.Terminal, r'.+\n']
    cells: typing.Annotated[abc.Array, inp.card.Cell | inp.card.Comment, SpaceCard]
    blank_0: typing.Annotated[abc.Terminal, r' *(?:\$.*)?\n\n'] = abc.Terminal[r' *(?:\$.*)?\n\n']('\n\n')
    surfaces: typing.Annotated[abc.Array, inp.card.Surface | inp.card.Comment, SpaceCard]
    blank_1: typing.Annotated[abc.Terminal, r' *(?:\$.*)?\n\n'] = abc.Terminal[r' *(?:\$.*)?\n\n']('\n\n')
    data: typing.Annotated[abc.Array, inp.card.Data | inp.card.Comment, SpaceCard]
    blank_2: typing.Annotated[abc.Terminal, r' *(?:\$.*)?(?:\n|\Z)'] = abc.Terminal[r' *(?:\$.*)?(?:\n|\Z)']('\n')
    other: typing.Annotated[abc.Terminal, r'\n[\s\S]*'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    @staticmethod
    def _prepare_message(value: typing.Any) -> typing.Any:
        """
        Prepares ``message`` values: None is no message block, a ``str`` message gets the ``message:`` keyword if it
        has none and its ending blank line.

        The ``message`` field's setter calls it, e.g., ``inp.message = 'outp=run.o'`` stores
        ``'message: outp=run.o\\n\\n'``.

        Raises:
            abc.Error: The message holds a blank line, which would end the message block.
        """

        if value is None or (isinstance(value, str) and not isinstance(value, abc.Symbol) and not value.strip()):
            return ''
        if not isinstance(value, str) or isinstance(value, abc.Symbol):
            return value
        value = value.rstrip()
        if re.search(r'\n[ \t]*\n', value):
            raise abc.Error('A message cannot hold a blank line, which ends the message block.', f'{value=}')
        if not value.lower().startswith('message:'):
            value = 'message: ' + value.strip()
        return value + '\n\n'

    @staticmethod
    def _prepare_title(value: typing.Any) -> typing.Any:
        """
        Adds the title card's trailing newline to a ``str`` title without one.

        The ``title`` field's setter calls it, so the constructor, the setter
        and ``scan`` all add it, e.g., ``Inp(title='Sphere', ...)``.
        """

        if isinstance(value, str) and not isinstance(value, abc.Symbol) and not value.endswith('\n'):
            return value + '\n'
        return value

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

            if isinstance(card, inp.card.data.Area) and len(card.x) != len(surface_numbers):
                raise abc.Error('Invalid value.', f'{card=}')

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into input files.

        Parsing stops at the first data card PyMCNP cannot parse, even one that
        parses in part: that card and every card after it are the remainder,
        with their shorthands expanded.

        Parameters:
            source: Source string to compile.

        Returns:
            Nonterminal symbol corresponding to ``source`` and the remainder.

        Raises:
            Error: Expected symbol, e.g., a cell or surface card PyMCNP cannot
                parse.
            Error: Expected space.
        """

        source = _unix_newlines(source)
        for line in re.finditer(r'[^\n]{81}', source):
            warnings.warn(abc.Warning('Line exceeds 80 characters maximum length', f'{line[0]}'))

        source = re.sub(r'\n +\n', '\n\n', source)

        # The message block is kept as it is; the title follows it.
        message = match[0] if (match := _REGEX_MESSAGE.match(source)) else ''
        source = source[len(message) :]

        # Preprocessing vertical data format.
        source = _vertical(source)

        # Preprocessing horizontal data format.
        source = message + _expand_cards(source)

        try:
            return super().from_mcnp(source)
        except abc.Error as err:
            # A data card that parses only in part stops the data block inside the card. Parsing up to the first card
            # that does not parse instead leaves it and every card after it as the remainder. Up to a cell or surface
            # card, the blocks after it are missing, so that fails as well.
            lines = source.split('\n')
            found = _unparseable_card(lines)
            if found is None:
                raise
            start = sum(len(line) + 1 for line in lines[: found[0] - 1])
            try:
                inpt, rest = super().from_mcnp(source[:start])
            except abc.Error as prefix_err:
                # An error without a stack is not one of the grammar, e.g., two cells with one number: it is the
                # problem, rather than the card.
                raise (err if prefix_err.stack else prefix_err) from None
            return inpt, rest + source[start:]

    def to_mcnp(self) -> str:
        """
        Decompiles inps into source strings, wrapping long card lines at 80 columns.

        Returns:
            Source string corresponding to ``self``.
        """

        assert isinstance(self.other, abc.Terminal)

        source = super().to_mcnp()
        message = self.message or ''
        body = source[len(message) : len(source) - len(self.other)] if self.other else source[len(message) :]
        title, _, rest = body.partition('\n')

        # The message block is not wrapped: it is not a card.
        return message + title + '\n' + '\n'.join(_wrap(line) for line in rest.split('\n')) + self.other

    def _scan_path(self, path: str) -> str:
        """
        Translates ``scan`` paths: the index into ``cells`` or ``surfaces`` is a card number, not a list position.

        The index into ``data`` is the list position, as in ``inp.data[i]``, comment cards included.

        Parameters:
            path: Path given to ``scan``, e.g., ``surfaces[99].r`` for surface card 99.

        Returns:
            Path into ``self``, e.g., ``surfaces[5].r`` if surface card 99 is the sixth item of ``surfaces``.

        Raises:
            Error: No card with that number.
        """

        steps = _steps(path)
        if len(steps) > 1 and steps[0] in {(True, 'cells'), (True, 'surfaces')} and not steps[1][0]:
            number = typing.cast(int, steps[1][1])
            kind = inp.card.Cell if steps[0][1] == 'cells' else inp.card.Surface
            block = typing.cast(abc.Array, getattr(self, str(steps[0][1])))
            found = [index for index, card in enumerate(block) if isinstance(card, kind) and card.j == number]
            if not found:
                name = 'cell' if kind is inp.card.Cell else 'surface'
                raise abc.Error(f'No {name} {number}.', f'{path=}: in ``scan`` paths, the index into ``{steps[0][1]}`` is the {name} number.')
            steps[1] = (False, found[0])

        return _join(steps)

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


def _message(self: Inp) -> abc.Terminal | None:
    """
    inp ``message:`` block, up to and including its blank line, or None if the file has none.
    """

    message = _message_field.fget(self)
    return message if message != '' else None


# ``message`` reads None, rather than an empty terminal, when there is no message block; ``to_mcnp`` writes the stored
# constituent.
_message_field = typing.cast(property, Inp.message)
Inp.message = property(_message, _message_field.fset, doc=_message.__doc__)  # type: ignore[method-assign,assignment]
