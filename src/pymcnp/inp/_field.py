import inspect
import typing

from .. import errors
from .. import types


class Field:
    """
    Describes one INP attribute: coerces, validates and stores it.

    Parameters:
        type_: MCNP type of the attribute.
        doc: Attribute description.
        required: Reject `None`.
        numeric: Python types converted with `type_(value)`.
        item: Element type, for tuple attributes (see `Field.tuple`).
        invalid: Callable `(self, value) -> bool`, truthy values are rejected.
        default: Callable `(card) -> value`, used by `__init__` when the argument is `None`.
        before: Callable `value -> value`, applied before coercion (e.g., to accept related objects).
    """

    def __init__(self, type_, doc: str, *, required: bool = False, numeric=(int, float), item=None, invalid=None, default=None, before=None, code=None):
        self.type = type_
        self.item = item
        self.required = required
        self.numeric = numeric
        self.invalid = invalid
        self.default = default
        self.before = before
        self.code = code
        self.__doc__ = doc

    @classmethod
    def tuple(cls, item, doc: str, **kwargs):
        return cls(types.Tuple(item), doc, item=item, **kwargs)

    @property
    def annotation(self):
        numeric = (self.numeric,) if isinstance(self.numeric, type) else (self.numeric or ())
        if self.item:
            return typing.Union[(list[str], *(list[n] for n in numeric), list[self.item], self.type)]
        return typing.Union[(str, *numeric, self.type)]

    def __set_name__(self, owner, name):
        self.name = name
        self.private = '_' + name

    def __get__(self, obj, owner=None):
        return self if obj is None else getattr(obj, self.private)

    def __set__(self, obj, value):
        if value is not None and self.before:
            value = self.before(value)
        if value is not None:
            value = self._coerce_all(value) if self.item else self._coerce(self.type, value)

        if (value is None and self.required) or (self.invalid and self.invalid(obj, value)):
            raise errors.InpError(self.code or obj._CODE, value)

        setattr(obj, self.private, value)

    def _coerce(self, type_, value):
        if isinstance(value, type_):
            return value
        if self.numeric and isinstance(value, self.numeric):
            return type_(value)
        if isinstance(value, str):
            return type_.from_mcnp(value)
        return value

    def _coerce_all(self, values):
        items = []
        for value in values:
            if isinstance(value, self.item):
                items.append(value)
            elif self.numeric and isinstance(value, self.numeric):
                items.append(self.item(value))
            elif isinstance(value, str):
                items.append(self.item.from_mcnp(value))
        return self.type(items)


class Fields:
    """
    Mixin building `_ATTRS`, the signature and `__init__` from `Field` attributes.

    Fields are declared in `_ATTRS` order (the order of the regular expression groups), inherited ones first.
    `_ORDER` overrides the order of `__init__` arguments and `_SET` the order in
    which they are assigned (validators may depend on other fields).
    """

    def __init_subclass__(cls, **kwargs):
        super().__init_subclass__(**kwargs)

        # Multiple bases (e.g. `types.Union`) must not merge the fields of unrelated classes.
        chain = reversed(cls.__mro__) if len(cls.__bases__) == 1 else (cls,)
        fields = {name: field for klass in chain for name, field in vars(klass).items() if isinstance(field, Field)}
        cls._ATTRS = {name: field.type for name, field in fields.items()}
        cls._ORDER = tuple(vars(cls).get('_ORDER', fields))
        cls._SET = tuple(vars(cls).get('_SET', fields))
        cls.__signature__ = inspect.Signature(
            [
                inspect.Parameter(
                    name,
                    inspect.Parameter.POSITIONAL_OR_KEYWORD,
                    default=inspect.Parameter.empty if fields[name].required and not fields[name].default else None,
                    annotation=fields[name].annotation,
                )
                for name in cls._ORDER
            ]
        )

    def __init__(self, *args, **kwargs):
        names = self._ORDER

        if len(args) > len(names):
            raise TypeError(f'{type(self).__name__} takes at most {len(names)} positional arguments, got {len(args)}')

        kwargs.update(zip(names, args))
        for name in self._SET:
            value = kwargs.pop(name, None)
            field = getattr(type(self), name)
            if value is None and field.default:
                value = field.default(self)
            setattr(self, name, value)

        if kwargs:
            raise TypeError(f'{type(self).__name__} got unexpected arguments: {sorted(kwargs)}')
