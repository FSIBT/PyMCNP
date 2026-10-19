import typing
import decimal
import collections
import dataclasses

from .Error import Error
from .Array import Array
from .Array import _parse_hint
from .Symbol import Symbol
from .Symbol import _parse
from .Symbol import _excerpt
from .Terminal import Terminal


def _space_null(fields: dict[str, tuple[type[Symbol], ...]]) -> set[str]:
    s = {'colon', 'prefix'}
    if 'colon' in fields:
        s.add('keyword')
        s.add('suffix')
        s.add('suffix_a')
    if 'suffix' in fields:
        s.add('keyword')
    if 'particle' in fields:
        s.add('colon')
    if fields:
        s.add(next(reversed(fields.keys())))
    return s


def _space_nullable(fields: dict[str, tuple[type[Symbol], ...]]) -> set[str]:
    s = {'equals', 'parenthesis_open', 'parenthesis_close'}
    if 'equals' in fields:
        s.add('particle')
        s.add('suffix')
        s.add('suffix_a')
        s.add('keyword')
    if 'parenthesis_close' in fields:
        names = list(fields.keys())
        index = names.index('parenthesis_close')
        for name in reversed(names[:index]):
            s.add(name)
            if Terminal[r''] not in fields[name]:
                break
    if fields:
        for name, kinds in reversed(fields.items()):
            s.add(name)
            if Terminal[r''] not in kinds:
                break
    return s


def _space_end(fields: dict[str, tuple[type[Symbol], ...]]) -> set[str]:
    s = set()
    if fields:
        for name, kinds in reversed(fields.items()):
            s.add(name)
            if Terminal[r''] not in kinds:
                break
    if 'equals' in fields:
        if 'equals' in s:
            s.remove('equals')
        if 'keyword' in s:
            s.remove('keyword')

    return s


def _parse_value(kinds: tuple[type[Symbol], ...], value: typing.Any) -> Symbol:
    assert isinstance(kinds, tuple)
    assert all(isinstance(kind, type) and issubclass(kind, Symbol) for kind in kinds)

    # Skipping valid Symbols.
    if any(isinstance(value, kind) for kind in kinds):
        return value

    # Compiling `str`s into symbols
    if isinstance(value, str):
        match, _ = _parse(kinds, value, 0)
        return match

    # Compiling `int`s, `float`d, `decimal.Decimal`s into symbols.
    if isinstance(value, (int, float, decimal.Decimal)):
        match, _ = _parse(kinds, str(value), 0)
        return match

    # Compiling non-string sequences into symbols.
    if isinstance(value, collections.abc.Sequence):
        error: Error | None = None
        for kind in kinds:
            if not issubclass(kind, Array):
                continue

            space = kind._space[0](kind._space[0]._default or '')

            try:
                match = [_parse_value(kind._kind, item) for item in value]
                return kind(*match, spaces=tuple([space] * (len(match) - 1)))
            except Error as err:
                if error is None:
                    error = err

        raise error or Error(f'Expected {"` `".join(kind.__name__ for kind in kinds)}`', f'{value=}')

    assert False


def _field(name: str, kinds: tuple[type[Symbol], ...]) -> property:
    """
    Constructs fields.

    Parameters:
        name: Name of field to construct.
        kinds: Type of field to construct.
    """

    assert isinstance(name, str)
    assert isinstance(kinds, tuple)
    assert all(isinstance(kind, type) and issubclass(kind, Symbol) for kind in kinds)

    name_private: str = f'_{name}'
    missing = dataclasses.MISSING

    def getter(self) -> typing.Any:
        return getattr(self, name_private)

    def setter(self, value: typing.Any) -> None:
        value = _parse_value(kinds, value)
        setattr(self, name_private, value)

        # Validating if complete.
        for private in type(self)._privates:
            if getattr(self, private) is missing:
                return
        self.__post_init__()

    return property(getter, setter)


@typing.dataclass_transform(kw_only=True)
class Nonterminal(Symbol):
    """
    Represents nonterminal symbols.

    Properties:
        spaces: Whitespaces between constituents.
    """

    spaces: dict[str, Terminal] = dataclasses.field(default_factory=dict)

    _space: typing.ClassVar[tuple[type[Terminal], ...]] = (Terminal[r''],)
    _forms: typing.ClassVar[tuple[type[typing.Self], ...]] = ()
    _fields: typing.ClassVar[dict[str, tuple[type[Symbol], ...]]] = {}
    _privates: typing.ClassVar[tuple[str, ...]] = ()
    _null: typing.ClassVar[frozenset[str]] = frozenset()
    _nullable: typing.ClassVar[frozenset[str]] = frozenset()
    _end: typing.ClassVar[frozenset[str]] = frozenset()

    def __post_init__(self) -> None:
        # Checks `__init__` if multi-form nonterminal.
        if len(type(self)._forms) != 0:
            raise NotImplementedError

    def __init_subclass__(cls) -> None:
        """
        Constructs cutsom dataclasses.
        """

        # Processing annotations.
        annotations = typing.get_type_hints(cls, include_extras=True)
        fields_ordered = {}
        fields_missing = {}
        fields_default = {}
        for name, hint in annotations.items():
            # Skipping private and class variables.
            origin = typing.get_origin(hint)
            if name.startswith('_') or origin is typing.ClassVar:
                continue

            # Storing evaluated type hints in order.
            if name != 'spaces':
                hint = _parse_hint(hint)
                fields_ordered[name] = hint

            # Collecting evaluated type hints with defaults.
            if name in cls.__dict__:
                fields_default[name] = hint
            else:
                fields_missing[name] = hint

        cls.spaces = dataclasses.field(default_factory=dict)
        cls._space = cls._space if cls._space is not dataclasses.MISSING else (Terminal[r''],)
        cls._forms = ()
        cls._fields = fields_ordered
        cls._privates = tuple(f'_{name}' for name in fields_ordered)
        cls._null = frozenset(_space_null(fields_ordered))
        cls._nullable = frozenset(_space_nullable(fields_ordered))
        cls._end = frozenset(_space_end(fields_ordered))

        # Creating `dataclasses.Dataclass`.
        cls.__annotations__ = fields_missing | fields_default | {'spaces': dict[str, Symbol]}
        datacls = dataclasses.dataclass(kw_only=True)(cls)

        # Adding `property`, i.e., getters and setters.
        for name, hint in cls._fields.items():
            if hasattr(datacls, name):
                setattr(datacls, f'_{name}', getattr(datacls, name))
            else:
                setattr(datacls, f'_{name}', dataclasses.MISSING)
            setattr(datacls, name, _field(name, hint))

        # Adding this nonterminal to multi-form nonterminals.
        for base in cls.__bases__:
            if isinstance(base, type) and issubclass(base, Nonterminal):
                base._forms = (*base._forms, datacls)

    def __class_getitem__(cls, index: int) -> type[typing.Self]:
        """
        Gets forms of nonterminal symbols at `index`.

        Parameters:
            index: Index of form to get.

        Returns:
            Forms of nonterminal symbols at `index`.
        """

        assert isinstance(index, int)

        return cls._forms[index]

    @classmethod
    def _from(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        # Compiling mono-form nonterminal.
        if len(cls._forms) == 0:
            spaces: dict[str, Terminal] = {}
            parameters: dict[str, Symbol] = {}
            end = len(source)
            space_end: dict[str, int] = {}

            # Iterating over consituents.
            for name, kinds in cls._fields.items():
                try:
                    parse = _parse(kinds, source, pos)
                    parameters[name] = parse[0]
                    pos = parse[1]
                except Error as err:
                    err.append(Error(f'Expected `{cls.__name__}.{name}`.', _excerpt(source, pos)))
                    raise err

                if (
                    pos != end  # Checking match is not complete.
                    and not isinstance(parameters[name], Terminal[r''])  # Checking parameter is not empty.
                    and cls._space is not None  # Checking if this consituent has spaces.
                    and name not in cls._null
                ):
                    try:
                        before = pos
                        parse = _parse(cls._space, source, pos)
                        spaces[name] = typing.cast(Terminal, parse[0])
                        space_end[name] = before
                        pos = parse[1]
                    except Error as err:
                        if name not in cls._nullable:  # Checking consituent is not space null.
                            err.append(Error(f'Expected `{"` `".join(Space.__name__ for Space in cls._space)}.{name}`.', _excerpt(source, pos)))
                            raise err
                        else:
                            if name in cls._end:  # Checking consituent is not last when null.
                                break
                            else:
                                spaces[name] = typing.cast(Terminal, '')

            last: str | None = None
            for field in reversed(cls._fields.keys()):
                if field not in parameters:
                    continue
                if parameters[field] != '' and parameters[field] != []:
                    last = field
                    break

            try:
                if last is not None and last in spaces:
                    spaces.pop(last)
                    if last in space_end:
                        pos = space_end[last]
                return cls(**(parameters | {'spaces': spaces})), pos
            except TypeError:
                raise Error(f'Expected `{cls.__name__}.{name}`.', _excerpt(source, pos))

        # Compiling multi-form nonterminal.
        else:
            try:
                parse = _parse(cls._forms, source, pos)
                return typing.cast(tuple[typing.Self, int], parse)
            except Error as err:
                err.append(Error(f'Expected `{cls.__name__}`.', _excerpt(source, pos)))
                raise err

    def to_mcnp(self) -> str:
        """
        Decompiles nonterminal symbols into their corresponding source strings.

        Returns:
            Source string corresponding to `self`.
        """

        Space = type(self)._space[0]
        null = type(self)._null

        last: str | None = None
        for field in reversed(type(self)._fields.keys()):
            if getattr(self, field) != '' and getattr(self, field) != []:
                last = field
                break

        return ''.join(
            f'{value.to_mcnp()}{self.spaces.get(name, Space(Space._default or "") if name not in null and name != last else "")}' for name in type(self)._fields if (value := getattr(self, name)) != ''
        )
