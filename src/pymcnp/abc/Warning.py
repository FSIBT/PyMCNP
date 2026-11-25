from __future__ import annotations

import typing
import dataclasses


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
