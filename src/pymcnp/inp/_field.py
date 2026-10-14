import typing

from .. import _fields
from .. import errors
from .. import types


class Field(_fields.Descriptor):
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
        super().__init__(type_, doc, required=required, default=default)
        self.item = item
        self.numeric = numeric
        self.invalid = invalid
        self.before = before
        self.code = code

    @classmethod
    def tuple(cls, item, doc: str, **kwargs):
        return cls(types.Tuple(item), doc, item=item, **kwargs)

    @property
    def annotation(self):
        numeric = (self.numeric,) if isinstance(self.numeric, type) else (self.numeric or ())
        if self.item:
            return typing.Union[(list[str], *(list[n] for n in numeric), list[self.item], self.type)]
        return typing.Union[(str, *numeric, self.type)]

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


Fields = _fields.Fields
