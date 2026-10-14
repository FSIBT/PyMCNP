from . import _card
from . import _field
from .. import errors
from .. import types


class Surface(_field.Fields, _card.Card):
    """
    Represents generic INP surface cards.

    Subclasses declare their own geometry fields; `prefix`, `number` and `transform` are shared and
    follow them in `__init__` arguments.
    """

    prefix = _field.Field(
        types.String,
        'Surface whitebody/reflecting flag',
        numeric=(),
        invalid=lambda self, value: value is not None and value.value.lower() not in {'*', '+'},
        code=errors.InpCode.SEMANTICS_CARD,
    )
    number = _field.Field(
        types.Integer,
        'Surface number',
        required=True,
        default=lambda card: next(_card.NUMBER),
        numeric=int,
        invalid=lambda self, value: not 1 <= value <= (99_999_999 if not self.transform else 999),
        code=errors.InpCode.SEMANTICS_CARD,
    )
    transform = _field.Field(
        types.Integer,
        'Surface transform',
        numeric=int,
        invalid=lambda self, value: value is not None and not 0 <= value <= 999,
        code=errors.InpCode.SEMANTICS_CARD,
    )

    def __init_subclass__(cls, **kwargs):
        if len(cls.__bases__) == 1:
            own = [name for name, field in vars(cls).items() if isinstance(field, _field.Field)]
            cls._ORDER = (*own, 'number', 'transform', 'prefix')
            cls._SET = (*own, 'transform', 'number', 'prefix')

        super().__init_subclass__(**kwargs)

    def to_mcnp(self):
        """
        Generates INP from `Surface`.

        Returns:
            INP surface card.
        """

        names = [name for name in self._ATTRS if name not in {'prefix', 'number', 'transform'}]
        values = ' '.join('' if (value := getattr(self, name)) is None else str(value) for name in names)
        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {values}'

        return _card.Card._postprocess(source)

    def __and__(a, b):
        """
        Unites `Surface`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Surface` union.
        """

        return types.Geometry.from_mcnp(f'{a.number}:{b.number}')

    def __or__(a, b):
        """
        Intersects `Surface`.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            `Surface` intersection.
        """

        return types.Geometry.from_mcnp(f'{a.number} {b.number}')

    def __neg__(self):
        """
        Negatives `Surface`.

        Returns:
            `Surface` negative.
        """

        return types.Geometry.from_mcnp(f'-{self.number}')

    def __pos__(self):
        """
        Positives `Surface`.

        Returns:
            `Surface` positive.
        """

        return types.Geometry.from_mcnp(f'+{self.number}')

    def __invert__(self):
        """
        Inverts `Surface`.

        Returns:
            `Surface` complement.
        """

        return types.Geometry.from_mcnp(f'#{self.number}')
