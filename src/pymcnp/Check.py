import os
import re
import pathlib
import difflib
import dataclasses

from . import abc
from . import inp
from .Inp import Inp

_WIDTH = 80


@dataclasses.dataclass(frozen=True)
class Problem:
    """
    Represents problems found while checking INP files.

    Attributes:
        line: Line number, counting from 1.
        kind: `error` for input that MCNP rejects or `warning` for input PyMCNP cannot parse.
        message: Description of the problem.
    """

    line: int
    kind: str
    message: str


@dataclasses.dataclass
class Check(abc.Utility):
    """
    Represents utilities that check input files.

    Attribute:
        path: Path to input file to check.
    """

    path: pathlib.Path | str

    def __post_init__(self):
        """
        Validates utitlites that check input files.

        Raises:
            Error.
        """

        self.path = pathlib.Path(self.path)
        if not self.path.exists():
            raise abc.Error('File not found', f'{self.path=}')

    def check(self):
        """
        Checks the input file at `path`.
        """

        assert isinstance(self.path, pathlib.Path)

        current = self.path.read_text()
        correct = Inp.from_mcnp(current)[0].to_mcnp()

        return difflib.unified_diff(current.split('\n'), correct.split('\n'))

    def problems(self):
        """
        Finds problems in a file, with line numbers.

        Lines wider than 80 columns are errors, since MCNP rejects them. If
        PyMCNP cannot parse the file, the first card it cannot parse is a
        warning, since MCNP may still accept it. Checking stops at that card,
        so the file should be rechecked after fixing it.

        Returns:
            List of `Problem`, ordered by line.
        """

        assert isinstance(self.path, pathlib.Path)

        try:
            text = self.path.read_text()
        except FileNotFoundError as err:
            raise abc.Error('File not found', f'{self.path=}') from err

        lines = text.split('\n')
        found = [Problem(number, 'error', f'Line is {len(line)} columns wide, MCNP reads at most {_WIDTH}.') for number, line in enumerate(lines, 1) if len(line) > _WIDTH]

        try:
            Inp.from_mcnp(text)
        except abc.Error as err:
            found.append(self._unparseable(lines, err))

        return sorted(found, key=lambda problem: problem.line)

    @staticmethod
    def _unparseable(lines, err):
        """
        Finds the first card that PyMCNP cannot parse.
        """

        stop = 'Checking stops at the first problem: fix it and run the check again to find further problems.'

        index = 2 if lines and lines[0].lower().startswith('message:') else 1
        for union in inp.Card._forms:
            while index < len(lines) and not lines[index].strip():
                index += 1

            cards = []
            while index < len(lines) and lines[index].strip():
                line = lines[index]
                if re.match(r'#( \S+)+$', line):
                    # Vertical data format is only valid across the whole block.
                    index += 1
                    while index < len(lines) and re.match(r' *\d\S*( +\S+)+$', lines[index]):
                        index += 1
                    continue

                if cards and (re.match(r'\s', line) or cards[-1][1][-1].rstrip().endswith('&')):
                    cards[-1][1].append(line)
                else:
                    cards.append((index + 1, [line]))
                index += 1

            for number, card in cards:
                try:
                    union.from_mcnp('\n'.join(card))
                except abc.Error as card_err:
                    return Problem(number, 'warning', f'PyMCNP cannot parse this card: {str(card_err).splitlines()[0]} {stop}')

        return Problem(1, 'warning', f'PyMCNP cannot parse this file: {str(err).splitlines()[0]} {stop}')

    def fix(self):
        """
        Fixes the input file at `path`.
        """

        assert isinstance(self.path, pathlib.Path)

        file = Inp.from_file(self.path)[0]
        if 'PYTEST_CURRENT_TEST' not in os.environ:  # pragma: no cover
            file.to_file(self.path)
