import typing
import dataclasses


from .... import abc
from ..Data import Data
from ... import literal


class Tf(Data):
    """
    Represents tf data cards.

    Attributes:
        keyword: tf data card `TF` symbol.
        suffix: tf data card `n` parameter.
        if1: tf data card `if1` parameter.
        id1: tf data card `id1` parameter.
        iu1: tf data card `iu1` parameter.
        is1: tf data card `is1` parameter.
        im1: tf data card `im1` parameter.
        ic1: tf data card `ic1` parameter.
        ie1: tf data card `ie1` parameter.
        it1: tf data card `it1` parameter.
        if2: tf data card `if2` parameter.
        id2: tf data card `id2` parameter.
        iu2: tf data card `iu2` parameter.
        is2: tf data card `is2` parameter.
        im2: tf data card `im2` parameter.
        ic2: tf data card `ic2` parameter.
        ie2: tf data card `ie2` parameter.
        it2: tf data card `it2` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TF'] | str = abc.Terminal[r'TF']('TF')
    suffix: literal.Integer | int | str
    if1: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    id1: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    iu1: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    is1: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    im1: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    ic1: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    ie1: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    it1: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    if2: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    id2: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    iu2: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    is2: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    im2: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    ic2: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    ie2: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    it2: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates tf data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
