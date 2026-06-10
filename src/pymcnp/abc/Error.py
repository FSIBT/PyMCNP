from __future__ import annotations

import typing
import dataclasses


@dataclasses.dataclass
class Error(Exception):
    """
    Represents errors.
    """

    message: str
    source: typing.Any
    stack: list[Error] = dataclasses.field(default_factory=list)

    def append(self, error: Error) -> None:
        """
        Appends errors into stack.
        """

        self.stack.append(error)

    def __str__(self) -> str:
        """
        Stringifies errors.
        """

        stack = '\n'.join(error.message for error in reversed(self.stack))
        return stack + ('\n' if stack else '') + f'{self.message}\n ' + '\n '.join(self.source.split('\n'))
