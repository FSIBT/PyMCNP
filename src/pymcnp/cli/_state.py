import inspect
from pathlib import Path
import sys
from typing import Final, Callable


DIR = Path.cwd() / '.pymcnp/'


def init():
    if not DIR.is_dir():
        DIR.mkdir()

    if not FileTable.PATH.is_file():
        FileTable.PATH.write_text('table = {}')

    if not RunConfig.PATH.is_file():
        RunConfig.PATH.write_text(
            "command = 'mcnp'\n\ndef prehook():\n    return\n\ndef posthook():\n    return\n"
        )


class FileTable:
    DIR: Final[Path] = Path.cwd() / '.pymcnp'
    PATH: Final[Path] = DIR / '_files.py'

    def append(self, alias, path):
        self = self._sync_up()

        if alias in self._table:
            raise ValueError

        self._table[alias] = path
        self._sync_down()

    def remove(self, alias):
        self = self._sync_up()

        if alias not in self._table:
            raise ValueError

        path = self._table.pop(alias)
        self._sync_down()

        return path

    def access(self, alias):
        self = self._sync_up()

        if alias not in self._table:
            raise ValueError

        return self._table[alias]

    @classmethod
    def _sync_up(cls):
        """
        ``_sync_up`` updates ``self._table``.

        ``_sync_up`` syncronizes this class's state with the state stored in
        ``./pymcnp/state.py``.
        """

        init()

        path = sys.path
        sys.path.append(FileTable.DIR)
        import _files

        sys.path = path

        table_cls = cls()
        table_cls._table = _files.table

        return table_cls

    def _sync_down(self):
        """
        ``_sync_down`` updates ``./pymcnp/state.py``.

        ``_sync_down`` syncronizes this class's state with the state stored in
        ``./pymcnp/state.py``.
        """

        init()

        FileTable.PATH.write_text(f'table = {self._table.__repr__()}')

    def __iter__(self):
        self = self._sync_up()
        return iter(self._table.items())


class RunConfig:
    DIR: Final[Path] = Path.cwd() / '.pymcnp'
    PATH: Final[Path] = DIR / '_run.py'

    def set_command(self, command: str):
        self.command = command
        self._sync_down()

    def set_prehook(self, prehook: Callable):
        self.prehook = prehook
        self._sync_down()

    def set_posthook(self, posthook: Callable):
        self.posthook = posthook
        self._sync_down()

    @classmethod
    def _sync_up(cls):
        """
        ``_sync_up`` updates ``self.command``, ``self.prehook``, and
        ``self.posthook``.

        ``_sync_up`` syncronizes this class's state with the state stored in
        ``./pymcnp/run.py``.
        """

        init()

        path = sys.path
        sys.path.append(FileTable.DIR)
        import _run

        sys.path = path

        run_cls = cls()
        run_cls.command: str = _run.command
        run_cls.prehook: Callable = _run.prehook
        run_cls.posthook: Callable = _run.posthook

        return run_cls

    def _sync_down(self):
        """
        ``_sync_down`` updates ``./pymcnp/run.py``.

        ``_sync_down`` syncronizes this class's state with the state stored in
        ``./pymcnp/run.py``.
        """

        init()

        prehook = 'def prehook():\n' + ''.join(inspect.getsourcelines(self.prehook)[0][1:])
        posthook = 'def posthook():\n' + ''.join(inspect.getsourcelines(self.posthook)[0][1:])

        RunConfig.PATH.write_text(
            f'command = {self.command.__repr__()}\n' + '\n' + prehook + '\n' + posthook + '\n'
        )


table = FileTable()._sync_up()
run = RunConfig()._sync_up()
