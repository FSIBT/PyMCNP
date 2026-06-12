import typing
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Lca(Data):
    """
    Represents lca data cards.

    Attributes:
        keyword: lca data card `LCA` symbol.
        ielas: lca data card `ielas` parameter.
        ipreg: lca data card `ipreg` parameter.
        iexisa: lca data card `iexisa` parameter.
        ichoic: lca data card `ichoic` parameter.
        jcoul: lca data card `jcoul` parameter.
        nexite: lca data card `nexite` parameter.
        npidk: lca data card `npidk` parameter.
        noact: lca data card `noact` parameter.
        icem: lca data card `icem` parameter.
        ilaq: lca data card `ilaq` parameter.
        nevtype: lca data card `nevtype` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LCA'] | str = abc.Terminal[r'LCA']('LCA')
    ielas: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    ipreg: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    iexisa: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    ichoic: typing.Annotated[abc.Terminal, r'(?:-2|[01])\d[012345][123456]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    jcoul: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    nexite: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    npidk: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    noact: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    icem: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    ilaq: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    nevtype: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates lca data cards.

        Raises:
            Error: Invalid value.
        """

        if isinstance(self.ielas, literal.Integer) and self.ielas not in {0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.ielas=}')

        if isinstance(self.ipreg, literal.Integer) and self.ipreg not in {0, 1, 2, 3}:
            raise abc.Error('Invalid value.', f'{self.ipreg=}')

        if isinstance(self.iexisa, literal.Integer) and self.iexisa not in {0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.iexisa=}')

        if isinstance(self.jcoul, literal.Integer) and self.jcoul not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.jcoul=}')

        if isinstance(self.nexite, literal.Integer) and self.nexite not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.nexite=}')

        if isinstance(self.npidk, literal.Integer) and self.npidk not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.npidk=}')

        if isinstance(self.noact, literal.Integer) and self.noact not in {-2, -1, 0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.noact=}')

        if isinstance(self.icem, literal.Integer) and self.icem not in {0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.icem=}')

        if isinstance(self.ilaq, literal.Integer) and self.ilaq not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.ilaq=}')
