import inspect


class Descriptor:
    """
    Base of attribute descriptors usable with `Fields`.

    Parameters:
        type_: MCNP type of the attribute.
        doc: Attribute description.
        required: Argument has no default in `__init__`.
        default: Callable `(obj) -> value`, used by `__init__` when the argument is `None`.
    """

    def __init__(self, type_, doc: str, *, required: bool = False, default=None):
        self.type = type_
        self.required = required
        self.default = default
        self.__doc__ = doc

    @property
    def annotation(self):
        return self.type

    def __set_name__(self, owner, name):
        self.name = name
        self.private = '_' + name

    def __get__(self, obj, owner=None):
        return self if obj is None else getattr(obj, self.private)


class Field(Descriptor):
    """
    Describes one parsed (OUTP, PTRAC, MESHTAL) attribute: validates and stores it.

    Parameters:
        type_: MCNP type of the attribute.
        doc: Attribute description.
        optional: Argument may be omitted, defaults to `None`.
        nullable: Argument is positional but may be `None`.
        many: Reject `None` elements.
        code: Error code, overrides `_CODE` of the owner.
    """

    def __init__(self, type_, doc: str, *, optional: bool = False, nullable: bool = False, many: bool = False, code=None):
        super().__init__(type_, doc, required=not optional)
        self.checked = not (optional or nullable)
        self.many = many
        self.code = code

    def __set__(self, obj, value):
        if (value is None and self.checked) or (self.many and value is not None and None in value):
            raise obj._ERROR(self.code or obj._CODE, value)

        setattr(obj, self.private, value)


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
        fields = {name: field for klass in chain for name, field in vars(klass).items() if isinstance(field, Descriptor)}
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
