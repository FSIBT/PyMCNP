import re
import typing
import pathlib
import collections.abc

from . import abc
from . import ptrac

_REGEX_HISTORY = re.compile(r' *\d+ +(?:[1345]000|-?20\d\d)(?: |$)')


def _events(file: 'Ptrac | pathlib.Path | str') -> collections.abc.Iterator[tuple[int, str, ptrac.block.Event]]:
    if isinstance(file, Ptrac):
        for history in file.histories:
            nps = int(history.i.nps)
            kind = str(history.i.event_type).strip()
            for event in history.events:
                yield nps, kind, event
                kind = str(event.j.type).strip()
    else:
        yield from Ptrac.iter_events(file)


class Ptrac(abc.File):
    """
    Represents ptrac files.

    Attributes:
        header: ptrac `header` parameter.
        histories: ptrac `histories` parameter.
    """

    header: ptrac.block.Header
    histories: typing.Annotated[abc.Array, ptrac.block.History, typing.Annotated[abc.Terminal, r'\n']]
    newline: typing.Annotated[abc.Terminal, r'\n?']

    @staticmethod
    def iter_histories(path: pathlib.Path | str) -> collections.abc.Iterator[ptrac.block.History]:
        """
        Parses ptrac files one history at a time, without holding the file or the histories in memory.

        Parameters:
            path: Path to ptrac file to read.

        Yields:
            History blocks in file order, each parsed once.

        Raises:
            Error: File not found.
            Error: Expected history.
        """

        path = pathlib.Path(path)
        if not path.is_file():
            raise abc.Error('File not found.', f'{path=}')

        def parse(lines: list[str], number: int) -> ptrac.block.History:
            history, remainder = ptrac.block.History.from_mcnp('\n'.join(lines))
            if remainder != '':
                raise abc.Error('Expected history.', f'line {number}: {remainder[:80]!r}')
            return history

        with path.open() as file:
            # Header: everything before the first history line.
            header: list[str] = []
            line = file.readline()
            while line and not (header and _REGEX_HISTORY.match(line) and len(header) >= 6):
                header.append(line.rstrip('\n'))
                line = file.readline()
            if not header:
                raise abc.Error('Expected header.', f'{path=}')
            _, remainder = ptrac.block.Header.from_mcnp('\n'.join(header) + '\n')
            if remainder != '':
                raise abc.Error('Expected header.', f'{remainder[:80]!r}')

            # Histories: one `i` line, then `j`/`p` line pairs up to the event announcing type 9000.
            number = len(header)
            while line:
                lines = [line.rstrip('\n')]
                while True:
                    j = file.readline()
                    p = file.readline() if j else ''
                    number += 2
                    if not j:
                        break
                    lines.extend((j.rstrip('\n'), p.rstrip('\n')))
                    if j[1:11].strip() == '9000':
                        break
                if len(lines) > 1 and lines[-1] == '':
                    lines.pop()
                yield parse(lines, number)
                line = file.readline()
                number += 1
                while line.strip() == '':
                    line = file.readline() if line else ''
                    if not line:
                        break

    @staticmethod
    def iter_events(path: pathlib.Path | str) -> collections.abc.Iterator[tuple[int, str, ptrac.block.Event]]:
        """
        Parses ptrac files one event at a time in a single pass.

        An event's `j` line announces the type of the next event, so each event is paired with its own type here.

        Parameters:
            path: Path to ptrac file to read.

        Yields:
            Tuples of history number (`nps`), event type (`'1000'`, `'3000'`, ...) and event.
        """

        for history in Ptrac.iter_histories(path):
            nps = int(history.i.nps)
            kind = str(history.i.event_type).strip()
            for event in history.events:
                yield nps, kind, event
                kind = str(event.j.type).strip()
