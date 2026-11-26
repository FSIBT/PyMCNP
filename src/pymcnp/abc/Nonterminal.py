import re
import sys
import copy
import typing
import collections.abc
import decimal
import numbers
import itertools
import collections
import inspect
import dataclasses

from .Error import Error
from .Array import Array
from .Array import _parse_hint
from .Symbol import Symbol
from .Symbol import _parse
from .Symbol import _parse_at
from .Terminal import Terminal
from ._path import get_path
from ._path import set_path


EMPTY_STRING_TYPE: type[Terminal] = Terminal[r'']


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
            if EMPTY_STRING_TYPE not in fields[name]:
                break
    if fields:
        for name, kinds in reversed(fields.items()):
            s.add(name)
            if EMPTY_STRING_TYPE not in kinds:
                break
    return s


def _space_end(fields: dict[str, tuple[type[Symbol], ...]]) -> set[str]:
    s = set()
    if fields:
        for name, kinds in reversed(fields.items()):
            s.add(name)
            if EMPTY_STRING_TYPE not in kinds:
                break
    if 'equals' in fields:
        if 'equals' in s:
            s.remove('equals')
        if 'keyword' in s:
            s.remove('keyword')

    return s


def _parse_value(kinds: tuple[type[Symbol], ...], value: typing.Any) -> Symbol:
    # Skipping valid Symbols.
    if any(isinstance(value, kind) for kind in kinds):
        return value

    # Compiling ``str``s into symbols
    if isinstance(value, str):
        match, _ = _parse(kinds, value)
        return match

    # Compiling numbers, e.g., ``int``, ``float``, ``decimal.Decimal`` or NumPy scalars, into symbols.
    if isinstance(value, (numbers.Real, decimal.Decimal)):
        match, _ = _parse(kinds, str(value))
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

        raise error or Error(f'Expected {"`` ``".join(kind.__name__ for kind in kinds)}``', f'{value=}')

    raise Error('Invalid value.', f'{value=}')


def _field(name: str, kinds: tuple[type[Symbol], ...]) -> property:
    """
    Constructs fields.

    Parameters:
        name: Name of field to construct.
        kinds: Type of field to construct.
    """

    name_private: str = f'_{name}'

    def getter(self) -> typing.Any:
        return getattr(self, name_private)

    def setter(self, value: typing.Any) -> None:
        value = _parse_value(kinds, value)

        setattr(self, name_private, value)

        # Validating if complete.
        if all(getattr(self, field) is not dataclasses.MISSING for field in type(self)._fields):
            self.__post_init__()

    return property(getter, setter)


# A subclass's own annotations, with names that are not defined (yet) left as references from Python 3.14 on, where
# annotations are evaluated lazily; one branch runs per Python version.
if sys.version_info >= (3, 14):  # pragma: no cover
    import annotationlib

    def _own_annotations(cls: type) -> dict[str, typing.Any]:
        return annotationlib.get_annotations(cls, format=annotationlib.Format.FORWARDREF)

else:  # pragma: no cover

    def _own_annotations(cls: type) -> dict[str, typing.Any]:
        return inspect.get_annotations(cls)


@typing.dataclass_transform(kw_only_default=True)
class Nonterminal(Symbol):
    """
    Represents nonterminal symbols.

    Properties:
        spaces: Whitespaces between constituents.
    """

    spaces: dict[str, Terminal] = dataclasses.field(default_factory=dict)
    _space: typing.ClassVar[tuple[type[Terminal], ...]] = (EMPTY_STRING_TYPE,)
    _forms: typing.ClassVar[tuple[type[typing.Self], ...]] = ()
    _fields: typing.ClassVar[dict[str, tuple[type[Symbol], ...]]] = {}
    # ``_build`` steps in ``__init__`` order: ``(None, None, False)`` sets ``spaces``, ``(name, '_name', validate)`` sets a field.
    _build_steps: typing.ClassVar[tuple[tuple[str | None, str | None, bool], ...]] = ()

    if typing.TYPE_CHECKING:

        def __init__(
            self,
            *,
            spaces: dict[str, Terminal] = ...,
            **kwargs: typing.Any,
        ) -> None: ...

    def __post_init__(self) -> None:
        """
        Validates the constituents.

        Must be free of side effects: it may run several times during construction.
        """
        # Checks ``__init__`` if multi-form nonterminal.
        if len(type(self)._forms) != 0:
            raise NotImplementedError

    def __init_subclass__(cls) -> None:
        """
        Constructs cutsom dataclasses.
        """

        super().__init_subclass__()

        # Subclassing a nonterminal with fields: inheriting its dataclass as is, without adding a form.
        bases = [base for base in cls.__bases__ if issubclass(base, Nonterminal) and base._fields]
        if bases:
            inherited = set().union(*(base._fields for base in bases))
            for name in sorted(set(vars(cls)) & inherited):
                raise Error(f'Subclasses of ``{bases[0].__name__}`` cannot redefine fields.', f'{cls.__name__}.{name}')
            for name, hint in _own_annotations(cls).items():
                text = hint if isinstance(hint, str) else getattr(hint, '__forward_arg__', None)
                if name.startswith('_') or typing.get_origin(hint) is typing.ClassVar:
                    continue
                if text is not None and re.match(r'\s*(typing\s*\.\s*)?ClassVar\b', text):
                    continue
                raise Error(f'Subclasses of ``{bases[0].__name__}`` cannot add fields.', f'{cls.__name__}.{name}: {text or hint}')
            cls._forms = ()
            return

        # Processing annotations.
        annotations = typing.get_type_hints(cls, include_extras=True)
        fields = {}
        for name, hint in annotations.items():
            # Skipping private and class variables.
            origin = typing.get_origin(hint)
            if name.startswith('_') or origin is typing.ClassVar:
                continue

            # Storing evaluated type hints in order.
            if name != 'spaces':
                fields[name] = _parse_hint(hint)

        cls.spaces = dataclasses.field(default_factory=dict)
        cls._space = cls._space if cls._space is not dataclasses.MISSING else (EMPTY_STRING_TYPE,)
        cls._forms = ()
        cls._fields = fields

        # Creating ``dataclasses.Dataclass``.
        cls.__annotations__ = fields | {'spaces': dict[str, Symbol]}
        datacls = dataclasses.dataclass(kw_only=True)(cls)

        # Adding ``property``, i.e., getters and setters.
        for name, hint in cls._fields.items():
            if hasattr(datacls, name):
                setattr(datacls, f'_{name}', getattr(datacls, name))
            else:
                setattr(datacls, f'_{name}', dataclasses.MISSING)
            setattr(datacls, name, _field(name, hint))

        # Planning ``_build``: the setters validate once every field is set (fields with defaults count
        # as set), and ``__init__`` validates again at the end, which ``_build`` does once instead.
        names = [field.name for field in dataclasses.fields(datacls) if field.name != 'spaces']
        required = [index for index, name in enumerate(names) if getattr(datacls, f'_{name}') is dataclasses.MISSING]
        first = required[-1] if required else 0
        steps = []
        for field in dataclasses.fields(datacls):
            if field.name == 'spaces':
                steps.append((None, None, False))
            else:
                index = names.index(field.name)
                steps.append((field.name, f'_{field.name}', first <= index < len(names) - 1))
        cls._build_steps = tuple(steps)

        # Adding this nonterminal to multi-form nonterminals.
        for base in cls.__bases__:
            if isinstance(base, type) and issubclass(base, Nonterminal):
                base._forms = (*base._forms, datacls)

    @classmethod
    def _build(cls, spaces: dict[str, Terminal], parameters: dict[str, Symbol]) -> typing.Self:
        """
        Constructs nonterminal symbols from already compiled constituents.

        Equivalent to ``cls(spaces=spaces, **parameters)`` for constituents of ``cls._fields`` kinds, without
        recompiling them, and validating with ``__post_init__`` the same way except for one repeated last call.

        Parameters:
            spaces: Whitespaces between constituents.
            parameters: Every constituent, already compiled.

        Returns:
            Nonterminal symbol with ``spaces`` and ``parameters``.

        Raises:
            Error: Invalid value.
        """

        self = object.__new__(cls)
        attributes = self.__dict__

        for name, name_private, validate in cls._build_steps:
            if name is None:
                attributes['spaces'] = spaces
            else:
                attributes[name_private] = parameters[name]
                if validate:
                    self.__post_init__()

        self.__post_init__()

        return self

    def __class_getitem__(cls, index: int) -> type[typing.Self]:
        """
        Gets forms of nonterminal symbols at ``index``.

        Parameters:
            index: Index of form to get.

        Returns:
            Forms of nonterminal symbols at ``index``.
        """

        return cls._forms[index]

    def __deepcopy__(self, memo: dict[int, typing.Any]) -> typing.Self:
        """
        Deep copies nonterminal symbols.

        Parameters:
            memo: Memory for copy objects.
        """

        if id(self) in memo:  # pragma: no cover
            return memo[id(self)]

        clone = type(self).from_mcnp(self.to_mcnp())[0]

        memo[id(self)] = clone

        return clone

    @classmethod
    def _from_mcnp_at(cls, source: str, pos: int) -> tuple[typing.Self, int]:
        """
        Compiles source strings at positions into their corresponding nonterminal symbols.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.

        Returns:
            Nonterminal symbol corresponding to ``source`` at ``pos`` and the position where it ends.

        Raises:
            Error: Expected symbol.
            Error: Expected space.
        """

        # Compiling mono-form nonterminal.
        if len(cls._forms) == 0:
            spaces: dict[str, Terminal] = {}
            parameters: dict[str, Symbol] = {}
            length = len(source)

            # Iterating over consituents.
            for name, kinds in cls._fields.items():
                try:
                    parameters[name], pos = _parse_at(kinds, source, pos)
                except Error as err:
                    err.append(Error(f'Expected ``{cls.__name__}.{name}``.', f'source={source[pos : pos + 80]!r}'))
                    # print(err)
                    raise err

                if (
                    pos != length  # Checking match is not complete.
                    and not isinstance(parameters[name], EMPTY_STRING_TYPE)  # Checking parameter is not empty.
                    and cls._space != (EMPTY_STRING_TYPE,)  # Checking if this consituent has spaces.
                    and name not in _space_null(cls._fields)
                ):
                    try:
                        space, pos = _parse_at(cls._space, source, pos)
                        spaces[name] = typing.cast(Terminal, space)
                    except Error as err:
                        if name not in _space_nullable(cls._fields):  # Checking consituent is not space null.
                            err.append(Error(f'Expected ``{"`` ``".join(Space.__name__ for Space in cls._space)}.{name}``.', f'source={source[pos : pos + 80]!r}'))
                            raise err
                        else:
                            if name in _space_end(cls._fields):  # Checking consituent is not last when null.
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
                    # Giving back the space after the last nonempty constituent.
                    pos -= len(spaces.pop(last))
                if len(parameters) == len(cls._fields):
                    return cls._build(spaces, parameters), pos
                return cls(spaces=spaces, **parameters), pos
            except TypeError:
                raise Error(f'Expected ``{cls.__name__}.{name}``.', f'source={source[pos : pos + 80]!r}')

        # Compiling multi-form nonterminal.
        else:
            try:
                return typing.cast(tuple[typing.Self, int], _parse_at(cls._forms, source, pos))
            except Error as err:
                err.append(Error(f'Expected ``{cls.__name__}``.', f'source={source[pos : pos + 80]!r}'))
                raise err

    def to_mcnp(self) -> str:
        """
        Decompiles nonterminal symbols into their corresponding source strings.

        Returns:
            Source string corresponding to ``self``.
        """

        Space = type(self)._space[0]
        null = _space_null(type(self)._fields)

        names = list(type(self)._fields)
        end = 0
        for index in range(len(names), 0, -1):
            if getattr(self, names[index - 1]) != '' and getattr(self, names[index - 1]) != []:
                end = index
                break

        # Nothing follows the last nonempty constituent, e.g., after an array emptied by ``clear``, so no space is written
        # after it or after the empty constituents behind it, as when parsing.
        return ''.join(
            f'{value.to_mcnp()}{self.spaces.get(name, Space(Space._default or "") if name not in null else "") if index < end - 1 else ""}'
            for index, name in enumerate(names)
            if (value := getattr(self, name)) != ''
        )

    def scan(self, **parameters: tuple[typing.Any, ...]) -> typing.Generator[typing.Self, None, None]:
        """
        Scans over nonterminals: yields deep copies for every combination of the values of the given fields or settable properties.

        Values are converted to the type of the field, as when setting it, e.g., ``5`` to ``inp.literal.Real('5')``, which
        compares and computes as a number.

        Parameters:
            parameters: Fields or settable properties, e.g., ``nps`` of ``Inp``, with their values, or paths to nested values,
                e.g., ``'surfaces[99].r'`` (dotted attributes and integer indices). In ``Inp`` paths, the index into
                ``cells`` or ``surfaces`` is the card number, e.g., surface 99, and the index into ``data`` is the list
                position, comment cards included. With several, the last one varies fastest.

        Yields:
            Independent copies with the given values set.

        Raises:
            Error: Missing parameters.
        """

        if not parameters:
            raise Error('Missing parameters.', f'{parameters=}')

        paths = []
        for path in parameters:
            try:
                paths.append(self._scan_path(path))
                get_path(self, paths[-1])
            except (AttributeError, LookupError):
                raise Error('Invalid value.', f'``self`` does not have parameter {path=}')

        for combination in itertools.product(*parameters.values()):
            clone = copy.deepcopy(self)
            for path, value in zip(paths, combination):
                set_path(clone, path, value)
            yield clone

    def _scan_path(self, path: str) -> str:
        """
        Translates ``scan`` paths into paths of ``self``; subclasses may renumber indices.

        Parameters:
            path: Path given to ``scan``.

        Returns:
            Path into ``self``.
        """

        return path

    def scan_with(self, values: collections.abc.Iterable[typing.Any], apply: collections.abc.Callable[[typing.Self, typing.Any], None]) -> typing.Generator[typing.Self, None, None]:
        """
        Scans over nonterminals: yields one deep copy per value, changed by ``apply``.

        Parameters:
            values: Values to scan.
            apply: Function that changes a copy for one value, e.g., ``lambda inp, r: setattr(inp.surface_cards(1)[0], 'r', r)``.

        Yields:
            Independent copies, in the order of ``values``.
        """

        for value in values:
            nonterminal = copy.deepcopy(self)
            apply(nonterminal, value)
            yield nonterminal
