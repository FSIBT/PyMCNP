import re

import numpy

from . import _field
from . import _card
from .. import _show
from .. import types
from .. import errors


class Tx(_field.Fields, _card.Card):
    """
    Represents INP `tx` surface cards.
    """

    _KEYWORD = 'tx'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('x', 'y', 'z', 'a', 'b', 'c', 'number', 'transform', 'prefix')
    _SET = ('x', 'y', 'z', 'a', 'b', 'c', 'transform', 'number', 'prefix')

    prefix = _field.Field(
        types.String, 'Surface whitebody/reflecting flag', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*', '+'}, code=errors.InpCode.SEMANTICS_CARD
    )
    number = _field.Field(
        types.Integer,
        'Surface number',
        required=True,
        default=lambda card: next(_card.NUMBER),
        numeric=int,
        invalid=lambda self, value: not 1 <= value <= (99999999 if not self.transform else 999),
        code=errors.InpCode.SEMANTICS_CARD,
    )
    transform = _field.Field(types.Integer, 'Surface transform', numeric=int, invalid=lambda self, value: value is not None and (not 0 <= value <= 999), code=errors.InpCode.SEMANTICS_CARD)
    x = _field.Field(types.Real, 'Parallel-to-x-axis tori center x component', required=True)
    y = _field.Field(types.Real, 'Parallel-to-x-axis tori center y component', required=True)
    z = _field.Field(types.Real, 'Parallel-to-x-axis tori center z component', required=True)
    a = _field.Field(types.Real, 'Parallel-to-x-axis tori A coefficent', required=True)
    b = _field.Field(types.Real, 'Parallel-to-x-axis tori B coefficent', required=True)
    c = _field.Field(types.Real, 'Parallel-to-x-axis tori C coefficent', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? tx( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Tx`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Tx`
        """

        vis = shapes.Torus(float(self.b), float(self.c), float(self.a))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((float(self.x), float(self.y), float(self.z))))

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
        Generates INP from `Tx`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.x} {self.y} {self.z} {self.a} {self.b} {self.c}'
        source = _card.Card._postprocess(source)

        return source
