from __future__ import annotations

import re
import types
import copy
import typing
import itertools
import collections
import collections.abc

from .Error import Error
from .Symbol import Symbol
from .Symbol import _parse_at
from .Terminal import Terminal
from ._path import get_path


def _parse_hint(hint: typing.Any) -> tuple[type[Symbol], ...]:
    """
    Evaluates ``Nonterminal`` annotations.

    Parameters:
        hint: ``Nonterminal`` annotation type hint.

    Returns:
        Tuple of evaluated type hints.
    """

    origin = typing.get_origin(hint)
    args = typing.get_args(hint)

    if origin is typing.Annotated:
        # Processing type hints for ``Array`` and ``Terminal``.
        assert len(args) > 1

        # ``Annotated[Array, (<Symbol>, ...), (<Space>, ...)] -> Array[(<Symbol>, ...), (<Space>, ...)]``
        if args[0] is Array:
            assert len(args) == 3
            kind, space = args[1:]
            kind = _parse_hint(kind)
            if len(kind) != 0:
                kind = typing.Union[kind]
            if space is not None:
                space = _parse_hint(space)
                if len(space) != 0:
                    space = typing.Union[space]
            return (Array[kind, space],)

        # ``Annotated[Terminal, <Pattern>] -> Terminal[<Pattern>]``
        if args[0] is Terminal:
            assert len(args) == 2
            pattern = args[1]
            return (Terminal[pattern],)

        assert False

    # Processing unions.
    if origin is typing.Union or isinstance(hint, types.UnionType):
        return tuple(itertools.chain(*map(_parse_hint, args)))

    # Processing nonterminals.
    if isinstance(hint, type) and issubclass(hint, Symbol):
        return (hint,)

    assert False


class ArraySpace(Terminal):
    """
    Represents spaces for array items.
    """

    _pattern = re.compile(r'( *(?:\$.+)?\n {1,5} *| +&\n *| *\n +| +)', re.IGNORECASE)
    _default = ' '


CACHE: dict[tuple[typing.Any, typing.Any], type[Array]] = {}


class Array(Symbol, list):
    """
    Represents arrays of symbols.

    Attributes:
        spaces: Whitespaces between constituents.
    """

    _space: typing.ClassVar[tuple[type[Terminal], ...]] = (ArraySpace,)
    _kind: typing.ClassVar[tuple[type[Symbol], ...]] = (Symbol,)

    spaces: list[Terminal]

    def __init_subclass__(cls) -> None:
        """
        Validates subclasses.

        Raises:
            Errors: Invalid ``Array`` subclass.
        """

        super().__init_subclass__()

        if len(cls._kind) == 0:
            raise Error('``Array._kind`` must be nonempty.', f'{cls._kind=}')

        if len(cls._space) == 0:
            raise Error('``Array._space`` must be nonempty.', f'{cls._space=}')

    @classmethod
    def __class_getitem__(cls, parameters: tuple[typing.Any, typing.Any]) -> type[Array]:  # ty: ignore[invalid-method-override]
        """
        Gets subclasses of ``Array`` representing arrays of ``kind``s.

        Parameters:
            parameters: Type of symbols in array and type of spaces.

        Returns:
            Subclasses of ``Array`` representing arrays of ``kind``s.
        """

        if parameters[1] is None:
            parameters = (parameters[0], ArraySpace)

        if parameters not in CACHE:
            kind, space = parameters

            CACHE[parameters] = type(
                f'Array[{kind}]',
                (cls,),
                {'_kind': _parse_hint(kind), '_space': _parse_hint(space)},
            )

        return CACHE[parameters]

    def __init__(self, *items: Symbol, spaces: collections.abc.Sequence[Terminal] | None = None) -> None:
        """
        Constructs ``Array``.

        Parameters:
            items: Items in array.
            spaces: Whitespaces between constituents.

        Raises:
            Error: Invalid spaces.
        """

        super().__init__(items)

        # Validates ``spaces``.
        if spaces is not None:
            if not ((len(spaces) == 0 and len(items) == 0) or len(spaces) == len(items) - 1):
                raise Error('Invalid spaces.', f'\n{items=}\n{spaces=}')
        else:
            space = type(self)._space[0](type(self)._space[0]._default or '' if len(type(self)._space) > 0 else '')
            spaces = [space] * (len(items) - 1)

        self.spaces = list(spaces)

    def __deepcopy__(self, memo: dict[int, typing.Any]) -> typing.Self:
        """
        Deep copies arrays of symbols.

        Parameters:
            memo: Memory for copy objects.
        """

        if id(self) in memo:  # pragma: no cover
            return memo[id(self)]

        clone = type(self)(*(copy.deepcopy(item, memo) for item in self), spaces=[copy.deepcopy(space, memo) for space in self.spaces])

        memo[id(self)] = clone

        return clone

    @classmethod
    def _from_mcnp_at(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        """
        Compiles source strings at positions into their corresponding arrays of symbols.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.

        Returns:
            List of symbols corresponding to ``source`` at ``pos`` and the position where it ends.
        """

        spaces: list[Terminal] = []
        parameters: list[Symbol] = []
        while True:
            try:
                item, pos = _parse_at(cls._kind, source, pos)
            except Error:
                if spaces:
                    # Giving back the space after the last item.
                    pos -= len(spaces.pop(-1))
                break

            parameters.append(item)

            if cls._space is not None:
                try:
                    space, pos = _parse_at(cls._space, source, pos)
                except Error:
                    break
                spaces.append(typing.cast(Terminal, space))

        return cls(*parameters, spaces=spaces), pos

    def to_mcnp(self) -> str:
        """
        Decompiles arrays of symbols into their corresponding source strings.

        Returns:
            Source string corresponding to ``self``.
        """

        return ''.join(itertools.chain.from_iterable(itertools.zip_longest((item.to_mcnp() for item in self), self.spaces, fillvalue='')))

    def _space_default(self) -> Terminal:
        """
        Returns the default space between items.
        """

        return type(self)._space[0](type(self)._space[0]._default or '')

    def _convert(self, value: typing.Any) -> Symbol:
        """
        Converts values to the array's item type as fields do, e.g., ``3`` to ``inp.literal.Real('3')``.

        Raises:
            Error: Invalid value.
        """

        from .Nonterminal import _parse_value

        return _parse_value(type(self)._kind, value)

    def _splice(self, start: int, stop: int, count: int) -> None:
        """
        Keeps ``spaces`` in step when the items ``start`` to ``stop`` become ``count`` items.

        Spaces between kept items stay; spaces next to the replaced items are reused, then the default space fills in.

        Parameters:
            start: First replaced item.
            stop: Item after the last replaced item.
            count: Number of new items.
        """

        length = len(self)
        stop = max(start, stop)
        prefix = self.spaces[: max(start - 1, 0)]
        suffix = self.spaces[stop:]
        needed = max(length - (stop - start) + count - 1, 0) - len(prefix) - len(suffix)
        middle = self.spaces[max(start - 1, 0) : stop][:needed]
        middle += [self._space_default() for _ in range(needed - len(middle))]
        self.spaces = prefix + middle + suffix

    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        """
        Sets items, converting values to the array's item type as fields do, e.g., ``3`` to ``inp.literal.Real('3')``.

        A slice may change the length; the spaces between items are kept in step.

        Parameters:
            key: Index or slice.
            value: Item, or items for a slice.

        Raises:
            Error: Invalid value.
        """

        if isinstance(key, slice):
            value = [self._convert(item) for item in value]
            start, stop, step = key.indices(len(self))
            if step == 1:
                self._splice(start, stop, len(value))
        else:
            value = self._convert(value)

        super().__setitem__(key, value)

    def __delitem__(self, key: typing.Any) -> None:
        """
        Deletes items, keeping the spaces between items in step.

        Parameters:
            key: Index or slice.
        """

        if isinstance(key, slice):
            indices = sorted(range(*key.indices(len(self))), reverse=True)
        else:
            indices = [range(len(self))[key]]

        for index in indices:
            self._splice(index, index + 1, 0)
            super().__delitem__(index)

    def insert(self, index: typing.SupportsIndex, item: typing.Any) -> None:
        """
        Inserts into arrays, converting the item.

        Parameters:
            index: Position to insert at.
            item: Item to insert.

        Raises:
            Error: Invalid value.
        """

        self[slice(index, index)] = [item]

    def append(self, item: typing.Any) -> None:
        """
        Appends to arrays, converting the item.

        Parameters:
            item: Item to append.

        Raises:
            Error: Invalid value.
        """

        self[len(self) :] = [item]

    def extend(self, items: typing.Iterable[typing.Any]) -> None:
        """
        Extends arrays, converting the items.

        Parameters:
            items: Items to append.

        Raises:
            Error: Invalid value.
        """

        self[len(self) :] = list(items)

    def __iadd__(self, items: typing.Iterable[typing.Any]) -> typing.Self:  # ty: ignore[invalid-method-override]
        """
        Extends arrays in place, converting the items.

        Parameters:
            items: Items to append.

        Raises:
            Error: Invalid value.
        """

        self.extend(items)
        return self

    def __imul__(self, count: typing.SupportsIndex) -> typing.Self:
        """
        Repeats arrays in place, keeping the spaces between items in step.

        Parameters:
            count: Number of repeats.
        """

        items = list(self)
        del self[:]
        for _ in range(count.__index__()):
            self.extend(items)
        return self

    def pop(self, index: typing.SupportsIndex = -1) -> typing.Any:
        """
        Removes and returns items, keeping the spaces between items in step.

        Parameters:
            index: Position to remove.
        """

        item = self[index]
        del self[index]
        return item

    def remove(self, item: typing.Any) -> None:
        """
        Removes the first equal item, keeping the spaces between items in step.

        Parameters:
            item: Item to remove.
        """

        del self[self.index(item)]

    def clear(self) -> None:
        """
        Removes all items and spaces.
        """

        super().clear()
        self.spaces = []

    def filter(self, *kinds: typing.Type, **fields: typing.Any) -> Array:
        """
        Filters arrays.

        Parameters:
            kinds: Types to filter items with.
            fields: Fields to filter items with.

        Returns:
            Subarray of items with the given fields. Items missing a field are skipped.
        """

        array: Array = CACHE[typing.Union[self._kind], typing.Union[self._space]]()

        for item in self:
            if kinds and not isinstance(item, kinds):
                continue

            matches: bool = True
            for path, value in fields.items():
                try:
                    actual = get_path(item, path)
                except (AttributeError, IndexError, KeyError):
                    matches = False
                    break

                if actual != value:
                    matches = False
                    break

            if matches:
                array.append(item)

        return array
