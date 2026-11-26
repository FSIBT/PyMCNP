"""
Writes stand-ins for ``mcnp6``: Python scripts that run on every OS.
"""

import os
import sys
import pathlib


def fake_executable(path: pathlib.Path, code: str) -> str:
    """
    Writes an executable at ``path`` that runs the Python ``code`` with this interpreter.

    On POSIX, ``path`` is the script, with a ``#!`` line. On Windows, which ignores ``#!``, the
    script is ``<path>-script.py`` and ``path.cmd`` runs it, as ``mcnp6.bat`` or ``mcnp6.exe``
    would be found for ``mcnp6``: the command is still ``path``, without an extension.

    Returns:
        Command that runs the stand-in, i.e., ``str(path)``.
    """

    if os.name == 'nt':  # pragma: no cover (Windows)
        script = path.with_name(f'{path.name}-script.py')
        script.write_text(code, encoding='utf-8')
        path.with_name(f'{path.name}.cmd').write_text(f'@"{sys.executable}" "%~dp0{script.name}" %*\n', encoding='utf-8')
    else:
        path.write_text(f'#!{sys.executable}\n{code}', encoding='utf-8')
        path.chmod(0o755)
    return str(path)
