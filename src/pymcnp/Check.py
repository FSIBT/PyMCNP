import pathlib
import difflib
import warnings
import contextlib
import dataclasses

from . import abc
from .Inp import Inp
from .Inp import _unparseable_card

_WIDTH = 80


@contextlib.contextmanager
def _quiet(read_again: bool = False):
    """
    Ignores the parser's warnings about lines wider than 80 columns, which ``Check`` reports itself, with line numbers,
    and, for a file ``read_again``, the warning about a file read as Latin-1, which its first read issued.
    """

    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', 'Line exceeds 80', abc.Warning)
        if read_again:
            warnings.filterwarnings('ignore', abc._text.NOT_UTF8, abc.Warning)
        yield


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

        current = abc._text.read_text(self.path)
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
            text = abc._text.read_text(self.path)
        except FileNotFoundError as err:
            raise abc.Error('File not found', f'{self.path=}') from err

        lines = text.split('\n')
        found = [Problem(number, 'error', f'Line exceeds {_WIDTH} characters maximum length ({len(line)} columns).') for number, line in enumerate(lines, 1) if len(line) > _WIDTH]

        try:
            with _quiet():
                remainder = Inp.from_mcnp(text)[1]
        except abc.Error as err:
            found.append(self._unparseable(lines, err, bool(err.stack)))
        else:
            if remainder.strip():
                found.append(self._unparseable(lines, abc.Error('Expected end of file.', f'{remainder=}'), True))

        return sorted(found, key=lambda problem: problem.line)

    @staticmethod
    def _unparseable(lines, err, lookup):
        """
        Finds the first card that PyMCNP cannot parse, as ``_unparseable_card`` does.

        Looks for the card only if ``lookup``: an error without a stack comes
        from checking parsed cards, e.g., two cells with one number, not from
        a card that does not parse, so it is reported whole, for the file.
        """

        stop = 'Checking stops at the first problem: fix it and run the check again to find further problems.'

        found = _unparseable_card(lines) if lookup else None
        if found is not None:
            number, card_err = found
            return Problem(number, 'warning', f'PyMCNP cannot parse this card: {str(card_err).splitlines()[0]} {stop}')

        message = str(err).splitlines()[0] if lookup else ' '.join(str(err).split())
        return Problem(1, 'warning', f'PyMCNP cannot parse this file: {message} {stop}')

    def fix(self, output: pathlib.Path | str | None = None):
        """
        Fixes the input file at ``path``.

        Rewrites the file as PyMCNP prints it, which wraps card lines wider
        than 80 columns, or writes it to ``output`` and leaves the file as it
        is. Lines it cannot shorten, e.g., long comments, stay as they are.
        The file is written as UTF-8, also a file read as Latin-1. A file PyMCNP cannot parse completely is not rewritten,
        since the part it cannot parse would be lost.

        Parameters:
            output: Path to write the fixed file to, or None to rewrite the
                file at ``path``.

        Returns:
            List of ``Problem`` left in the fixed file, as ``problems`` finds
            them; empty if the file is clean.

        Raises:
            Error: PyMCNP cannot parse the file completely; the file is left
                as it is, and ``output`` is not written.
        """

        assert isinstance(self.path, pathlib.Path)

        for problem in self.problems():
            if problem.kind == 'warning':
                raise abc.Error(f'File not rewritten: PyMCNP cannot parse line {problem.line}.', f'{self.path=}\n{problem.message}')

        with _quiet(read_again=True):
            file = Inp.from_file(self.path)[0]
        if output is None:
            file.to_file(self.path)
            return self.problems()

        file.to_file(output)
        return Check(output).problems()
