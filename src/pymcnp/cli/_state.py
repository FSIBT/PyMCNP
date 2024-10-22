import inspect
import os
from pathlib import Path
import sys
from typing import Callable


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

        with self.path.open('w') as f:
            f.write(f"command = '{self.command}'\n" + '\n' + prehook + '\n' + posthook + '\n')
            f.flush()
            os.fsync(f.fileno())


run = RunConfig()._sync_up()
