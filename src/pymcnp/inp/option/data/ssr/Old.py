import typing


from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Old(Ssr):
    """
    Represents old ssr data options.

    Attributes:
        keyword: old ssr data option ``r'OLD'`` symbol.
        equals: old ssr data option ``r'='`` symbol.
        s: old ssr data option ``s`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'OLD'] = abc.Terminal[r'OLD']('OLD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates old ssr data options.

        Raises:
            Error: Invalid value.
        """

        if not isinstance(self.s, abc.Terminal) and not all(sk != 0 for sk in self.s):
            raise abc.Error('Invalid value.', f'{self.s=}')
