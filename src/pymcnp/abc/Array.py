from __future__ import annotations

import re
import types
import typing
import itertools
import collections

from .Error import Error
from .Symbol import Symbol
from .Symbol import _parse
from .Terminal import Terminal


def _parse_hint(hint: typing.Any) -> tuple[type[Symbol], ...]:
    """
    Evaluates `Nonterminal` annotations.

    Parameters:
        hint: `Nonterminal` annotation type hint.

    Returns:
        Tuple of evaluated type hints.
    """

    origin = typing.get_origin(hint)
    args = typing.get_args(hint)

    if origin is typing.Annotated:
        # Processing type hints for `Array` and `Terminal`.
        assert len(args) > 1

        # `Annotated[Array, (<Symbol>, ...), (<Space>, ...)] -> Array[(<Symbol>, ...), (<Space>, ...)]`
        if args[0] is Array:
            assert len(args) == 3
            kind, space = args[1:]
            return (args[0][kind, space],)

        # `Annotated[Terminal, <Pattern>] -> Terminal[<Pattern>]`
        if args[0] is Terminal:
            assert len(args) == 2
            pattern = args[1]
            return (args[0][pattern],)

        assert False

    # Processing unions.
    if origin is typing.Union or isinstance(hint, types.UnionType):
        return tuple(itertools.chain(*map(_parse_hint, args)))

    # Processing nonterminals.
    if isinstance(hint, type) and issubclass(hint, Symbol):
        return (hint,)

    return tuple()


class Space(Terminal):
    """
    Represents spaces for array items.
    """

    _pattern = re.compile(r'( *(?:\$.+)?\n {1,5} *| +&\n +| *\n +| +)([\s\S]*)', re.IGNORECASE)
    _default = ' '


CACHE: dict[tuple[typing.Any, typing.Any], type[Array]] = {}


class Array(Symbol, list):
    """
    Represents arrays of symbols.

    Attributes:
        spaces: Whitespaces between constituents.
    """

    spaces: list[Terminal]
    _space: typing.ClassVar[tuple[type[Terminal], ...]] = (Space,)
    _kind: typing.ClassVar[tuple[type[Symbol], ...]] = (Symbol,)

    def __init_subclass__(cls) -> None:
        """
        Validates subclasses.

        Raises:
            Errors: Invalid `Array` subclass.
        """

        if len(cls._kind) == 0:
            raise Error('`Array._kind` must be nonempty.', f'{cls._kind=}')

        if len(cls._space) == 0:
            raise Error('`Array._space` must be nonempty.', f'{cls._space=}')

    def __init__(self, *items: Symbol, spaces: collections.abc.Sequence[Symbol] | None = None) -> None:
        """
        Constructs `Array`.

        Parameters:
            items: Items in array.
            spaces: Whitespaces between constituents.

        Raises:
            Error: Invalid spaces.
        """

        assert isinstance(items, tuple)
        assert all(isinstance(item, Symbol) for item in items)
        assert isinstance(spaces, (collections.abc.Sequence, type(None)))
        assert not isinstance(spaces, collections.abc.Sequence) or all(isinstance(space, Symbol) for space in spaces)

        super().__init__(items)

        # Validates `spaces`.
        if spaces is not None:
            if not ((len(spaces) == 0 and len(items) == 0) or len(spaces) == len(items) - 1):
                raise Error('Invalid spaces.', f'{items=}\n{spaces=}')
        else:
            space = type(self)._space[0](type(self)._space[0]._default or '' if len(type(self)._space) > 0 else '')
            spaces = [space] * (len(items) - 1)
        self.spaces = list(spaces)

    @classmethod
    def __class_getitem__(cls, parameters: tuple[typing.Any, typing.Any]) -> type[Array]:  # ty: ignore[invalid-method-override]
        """
        Gets subclasses of `Array` representing arrays of `kind`s.

        Parameters:
            parameters: Type of symbols in array and type of spaces.

        Returns:
            Subclasses of `Array` representing arrays of `kind`s.
        """

        assert isinstance(parameters, tuple)
        assert len(parameters) == 2

        if parameters not in CACHE:
            kind, space = parameters
            space = space or Space

            CACHE[parameters] = type(
                f'Array[{kind}]',
                (cls,),
                {'_kind': _parse_hint(kind), '_space': _parse_hint(space)},
            )

        return CACHE[parameters]

    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into their corresponding arrays of symbols.

        Parameters:
            source: Source string to compile.

        Returns:
            List of symbols corresponding to `source`.
        """

        assert isinstance(source, str)

        spaces: list[Terminal] = []
        parameters: list[Symbol] = []
        while True:
            try:
                parse = _parse(cls._kind, source)
            except Error:
                if spaces:
                    source = spaces.pop(-1).to_mcnp() + source
                break

            parameters.append(parse[0])
            source = parse[1]

            if cls._space is not None:
                try:
                    parse = _parse(cls._space, source)
                except Error:
                    break
                spaces.append(typing.cast(Terminal, parse[0]))
                source = parse[1]

        return cls(*parameters, spaces=spaces), source

    def to_mcnp(self) -> str:
        """
        Decompiles arrays of symbols into their corresponding source strings.

        Returns:
            Source string corresponding to `self`.
        """

        return ''.join(itertools.chain.from_iterable(itertools.zip_longest((item.to_mcnp() for item in self), self.spaces, fillvalue='')))

    def append(self, item: typing.Any) -> None:
        """
        Appends to array.

        Parameters:
            item: Item to append.
        """

        super().append(item)
        space = type(self)._space[0](type(self)._space[0]._default or '' if len(type(self)._space) > 0 else '')
        self.spaces.append(space)
