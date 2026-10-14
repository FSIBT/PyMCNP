import re

from . import _field
from . import _card
from .. import _show
from .. import types
from .. import errors


class Py(_field.Fields, _card.Card):
    """
    Represents INP `py` surface cards.
    """

    _KEYWORD = 'py'

    _ORDER = ('d', 'number', 'transform', 'prefix')
    _SET = ('d', 'transform', 'number', 'prefix')

    prefix = _field.Field(types.String, 'Surface whitebody/reflecting flag', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*', '+'})
    number = _field.Field(
        types.Integer, 'Surface number', required=True, default=lambda card: next(_card.NUMBER), numeric=int, invalid=lambda self, value: not 1 <= value <= (99999999 if not self.transform else 999)
    )
    transform = _field.Field(types.Integer, 'Surface transform', numeric=int, invalid=lambda self, value: value is not None and (not 0 <= value <= 999))
    d = _field.Field(types.Real, 'Normal-to-the-y-axis plane D coefficent', required=True, code=errors.InpCode.SEMANTICS_OPTION)

    _REGEX = re.compile(rf'\A(\+|\*)?(\S+)( \S+)? py( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Py`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Py`
        """

        vis = shapes.Plane(0, 1, 0, float(self.d))

        return vis

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

    def to_mcnp(self):
        """
        Generates INP from `Py`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.d}'
        source = _card.Card._postprocess(source)

        return source
