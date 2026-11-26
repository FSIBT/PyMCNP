import re
import pathlib
import difflib
import warnings
import contextlib
import dataclasses

from . import abc
from . import inp
from .Inp import Inp
from .Inp import _REGEX_COMMENT
from .Inp import _expand

_WIDTH = 80


@contextlib.contextmanager
def _quiet():
    """
    Ignores the parser's warnings about lines wider than 80 columns, which ``Check`` reports itself, with line numbers.
    """

    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', 'Line exceeds 80', abc.Warning)
        yield


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

    index = 2 if lines and lines[0].lower().startswith('message:') else 1
    for union in (inp.card.Cell, inp.card.Surface, inp.card.Data):
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

            if _REGEX_COMMENT.match(line):
                # Comment cards are not cards to parse, but count as lines.
                index += 1
                continue

            # Cards are parsed as ``Inp`` parses them: shorthands expanded, without ``$`` comments.
            code = _expand(line.partition('$')[0]).rstrip()
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


@dataclasses.dataclass(frozen=True)
class Problem:
    """
    Represents problems found while checking INP files.

    Attributes:
        line: Line number, counting from 1.
        kind: ``error`` for input that MCNP rejects or ``warning`` for input PyMCNP cannot parse.
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
        Validates utilities that check input files.

        Raises:
            Error.
        """

        self.path = pathlib.Path(self.path)
        if not self.path.exists():
            raise abc.Error('File not found', f'{self.path=}')

    def check(self):
        """
        Checks the input file at ``path``.
        """

        assert isinstance(self.path, pathlib.Path)

        current = self.path.read_text()
        with _quiet():
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
            List of ``Problem``, ordered by line.
        """

        assert isinstance(self.path, pathlib.Path)

        try:
            text = self.path.read_text()
        except FileNotFoundError as err:
            raise abc.Error('File not found', f'{self.path=}') from err

        lines = text.split('\n')
        found = [Problem(number, 'error', f'Line exceeds {_WIDTH} characters maximum length ({len(line)} columns).') for number, line in enumerate(lines, 1) if len(line) > _WIDTH]

        try:
            with _quiet():
                remainder = Inp.from_mcnp(text)[1]
        except abc.Error as err:
            found.append(self._unparseable(lines, err))
        else:
            if remainder.strip():
                found.append(self._unparseable(lines, abc.Error('Expected end of file.', f'{remainder=}')))

        return sorted(found, key=lambda problem: problem.line)

    @staticmethod
    def _unparseable(lines, err):
        """
        Finds the first card that PyMCNP cannot parse, as ``_unparseable_card`` does.
        """

        stop = 'Checking stops at the first problem: fix it and run the check again to find further problems.'

        found = _unparseable_card(lines)
        if found is not None:
            number, card_err = found
            return Problem(number, 'warning', f'PyMCNP cannot parse this card: {str(card_err).splitlines()[0]} {stop}')

        return Problem(1, 'warning', f'PyMCNP cannot parse this file: {str(err).splitlines()[0]} {stop}')

    def fix(self):
        """
        Fixes the input file at ``path``.

        Rewrites the file as PyMCNP prints it, which wraps card lines wider
        than 80 columns. Lines it cannot shorten, e.g., long comments, stay as
        they are.

        Returns:
            List of ``Problem`` left in the fixed file, as ``problems`` finds
            them; empty if the file is clean.
        """

        assert isinstance(self.path, pathlib.Path)

        with _quiet():
            file = Inp.from_file(self.path)[0]
        file.to_file(self.path)

        return self.problems()
