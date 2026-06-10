import re
import typing
import collections

import numpy

from . import abc
from . import inp


_REGEX_REPEAT = re.compile(r'(\S+) (\d+)R', re.IGNORECASE)
_REGEX_INSERT = re.compile(r'(\S+) (\d+)I (\S+)', re.IGNORECASE)
_REGEX_JUMP = re.compile(r'(?<=\s)(\d+)(J)(?=\s)', re.IGNORECASE)
_REGEX_LOG = re.compile(r'(\S+) (\d+)I?LOG (\S+)', re.IGNORECASE)


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

    _pattern = re.compile(r'( *\n| +\$.+\n(?! {1,5})| *\n)([\s\S]*)', re.IGNORECASE)
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
    cells: typing.Annotated[abc.Array, inp.card.Cell | inp.card.Comment, SpaceCard] | collections.abc.Sequence[inp.card.Cell | inp.card.Comment | str] | str
    blank_0: typing.Annotated[abc.Terminal, r'(?: *\$.+)?\n\n'] | str = abc.Terminal[r'(?: *\$.+)?\n\n']('\n\n')
    surfaces: typing.Annotated[abc.Array, inp.card.Surface | inp.card.Comment, SpaceCard] | collections.abc.Sequence[inp.card.Surface | inp.card.Comment | str] | str
    blank_1: typing.Annotated[abc.Terminal, r'(?: *\$.+)?\n\n'] | str = abc.Terminal[r'(?: *\$.+)?\n\n']('\n\n')
    data: typing.Annotated[abc.Array, inp.card.Data | inp.card.Comment, SpaceCard] | collections.abc.Sequence[inp.card.Data | inp.card.Comment | str] | str
    blank_2: typing.Annotated[abc.Terminal, r'(?: *\$.+)?\n'] | str = abc.Terminal[r'(?: *\$.+)?\n']('\n')
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
        source = _REGEX_INSERT.sub(lambda match: ' '.join(map(str, numpy.linspace(float(match[1]), float(match[3]), num=int(match[2])))), source)
        source = _REGEX_JUMP.sub(lambda match: ' '.join([match[2]] * int(match[1])), source)
        source = _REGEX_LOG.sub(lambda match: ' '.join(map(str, numpy.logspace(float(match[1]), float(match[3]), num=int(match[2])))), source)

        return super().from_mcnp(source)

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
        else:
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
            else:
                return None
        else:
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
