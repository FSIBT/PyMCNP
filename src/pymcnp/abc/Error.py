from __future__ import annotations

import typing
import dataclasses


@dataclasses.dataclass
class Error(Exception):
    """
    Represents errors.

    Attributes:
        title: Error title.
        body: Error body.
        stack: Stack of errors.
    """

    title: str
    body: typing.Any
    stack: list[Error] = dataclasses.field(default_factory=list)

    def append(self, error: Error) -> None:
        """
        Appends errors to the stack.

        Parameters:
            error: Error to append to the stack.
        """

        self.stack.append(error)

    def __str__(self) -> str:
        """
        Stringifies errors.
        """

        stack = '\n'.join(error.title for error in reversed(self.stack))
        return stack + ('\n' if stack else '') + f'{self.title}\n ' + '\n '.join(self.body.split('\n'))
