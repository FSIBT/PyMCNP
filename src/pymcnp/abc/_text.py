"""
Reads text files the same way on every OS: UTF-8 (a byte order mark is skipped), or Latin-1 with a warning.

MCNP files are ASCII by the format's definition, so a character outside ASCII is almost always in a comment or a
title. A file saved as Latin-1 or cp1252, e.g., by a Windows editor, is read rather than rejected; Latin-1 decodes
every byte. A file with a NUL byte, which no text file holds, e.g., a binary PTRAC file, raises ``UnicodeDecodeError``.
"""

import typing
import pathlib
import warnings

from .Warning import Warning

# Start of the warning for a file read as Latin-1, e.g., to ignore it when a file is read again.
NOT_UTF8 = 'File is not UTF-8 text'

# Bytes checked at a time, so a large file, e.g., PTRAC, is checked with flat memory.
_CHUNK = 1 << 20


def _encoding(path: pathlib.Path | str, warn: bool) -> str:
    """
    Finds the encoding of a text file: ``utf-8-sig``, or ``latin-1`` if the file is not UTF-8.

    Parameters:
        path: Path of the file.
        warn: Flag to issue a ``Warning`` naming the first line that is not UTF-8.

    Raises:
        UnicodeDecodeError: The file holds a NUL byte, so it is not text.
    """

    line = 1
    offset = 0
    pending = b''
    with open(path, 'rb') as file:
        while True:
            chunk = file.read(_CHUNK)
            data = pending + chunk

            nul = data.find(b'\x00')
            if nul >= 0:
                raise UnicodeDecodeError('utf-8', data, offset + nul, offset + nul + 1, 'a NUL byte, so not a text file')

            # Only whole lines are decoded, so a character is not cut by the end of a chunk.
            cut = data.rfind(b'\n') + 1 if chunk else len(data)
            complete, pending = data[:cut], data[cut:]
            try:
                complete.decode('utf-8')
            except UnicodeDecodeError as err:
                if warn:
                    number = line + complete.count(b'\n', 0, err.start)
                    warnings.warn(Warning(f'{NOT_UTF8}, so PyMCNP reads it as Latin-1.', f'{path}, line {number}'), stacklevel=4)
                return 'latin-1'

            line += complete.count(b'\n')
            offset += len(complete)
            if not chunk:
                return 'utf-8-sig'


def read_text(path: pathlib.Path | str, warn: bool = True) -> str:
    """
    Reads a text file, with its line ends translated to ``\\n``.

    Parameters:
        path: Path of the file.
        warn: Flag to warn if the file is read as Latin-1.

    Raises:
        UnicodeDecodeError: The file holds a NUL byte, so it is not text.
    """

    return pathlib.Path(path).read_text(encoding=_encoding(path, warn))


def open_text(path: pathlib.Path | str) -> typing.TextIO:
    """
    Opens a text file for reading line by line, with its line ends translated to ``\\n``.

    Parameters:
        path: Path of the file.

    Raises:
        UnicodeDecodeError: The file holds a NUL byte, so it is not text.
    """

    return open(path, encoding=_encoding(path, True))
