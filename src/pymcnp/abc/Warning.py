from __future__ import annotations

import typing
import warnings
import dataclasses


_Warning = Warning


@dataclasses.dataclass
class Warning(Warning):
    """
    Represents errors.

    Attributes:
        title: Warning title.
        body: Warning body.
    """

    title: str
    body: typing.Any

    def __str__(self) -> str:
        """
        Stringifies warnings.
        """

        return f'{self.title}\n ' + '\n '.join(self.body.split('\n'))


_showwarning = warnings.showwarning


def showwarning(message: _Warning | str, category: type[_Warning], filename: str, lineno: int, file: typing.TextIO | None = None, line: str | None = None) -> None:  # pragma: no cover
    if issubclass(category, Warning):
        return
    _showwarning(message, category, filename, lineno, file, line)


warnings.showwarning = showwarning  # ty: ignore[invalid-assignment]
