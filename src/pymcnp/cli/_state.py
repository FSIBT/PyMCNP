import inspect
from pathlib import Path
import sys
from typing import Callable


class FileTable:
    """Store information in a file, so that it can be used across multiple processes.

    We use this mechanism to store information that is needed when, for example,
    running MCNP simulations in parallel.
    """

    def __init__(self):
        self.table = {}
        self.path = Path.cwd() / '.pymcnp' / '_files.py'

        self.path.parent.mkdir(exist_ok=True, parents=True)

        if not self.path.is_file():
            self.path.write_text('table = {}')

    def append(self, alias, path):
        self._sync_up()

        if alias in self._table:
            raise ValueError

        self._table[alias] = path
        self._sync_down()

    def remove(self, alias):
        self._sync_up()

        if alias not in self._table:
            raise ValueError

        path = self._table.pop(alias)
        self._sync_down()

        return path

    def access(self, alias):
        self._sync_up()

        if alias not in self._table:
            raise ValueError

        return self._table[alias]

    def _sync_up(self):
        """Read information from `_files.py`."""

        path = sys.path
        sys.path.append(str(self.path.parent.absolute()))
        import _files

        sys.path = path

        self._table = _files.table

        return self

    def _sync_down(self):
        """Write information to `_files.py`."""

        self.path.write_text(f'table = {self._table.__repr__()}')

    def __iter__(self):
        self = self._sync_up()
        return iter(self._table.items())


class RunConfig:
    """Store pre and posthooks as well as the run command for parallel runs."""

    def __init__(self):
        self.path = Path.cwd() / '.pymcnp' / '_run.py'
        self.command = 'mcnp'

        self.path.parent.mkdir(exist_ok=True, parents=True)

        if not self.path.is_file():
            self._sync_down()

    def prehook(self):
        pass

    def posthook(self):
        pass

    def set_command(self, command: str):
        self.command = command
        self._sync_down()

    def set_prehook(self, prehook: Callable):
        self.prehook = prehook
        self._sync_down()

    def set_posthook(self, posthook: Callable):
        self.posthook = posthook
        self._sync_down()

    def _sync_up(self):
        """Read command, prehook, and posthook from `_run.py`."""

        path = sys.path
        sys.path.append(str(self.path.parent.absolute()))
        import _run

        sys.path = path

        self.command = _run.command
        self.prehook = _run.prehook
        self.posthook = _run.posthook

        return self

    def _sync_down(self):
        """Write command, prehook, and posthook to `_run.py`."""

        prehook = 'def prehook():\n' + ''.join(inspect.getsourcelines(self.prehook)[0][1:])
        posthook = 'def posthook():\n' + ''.join(inspect.getsourcelines(self.posthook)[0][1:])

        self.path.write_text(
            f"command = '{self.command}'\n" + '\n' + prehook + '\n' + posthook + '\n'
        )


table = FileTable()._sync_up()
run = RunConfig()._sync_up()
