import re

import numpy

from . import _field
from . import _card
from .. import _show
from .. import types
from .. import errors


class K_y(_field.Fields, _card.Card):
    """
    Represents INP `k/y` surface cards.
    """

    _KEYWORD = 'k/y'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('x', 'y', 'z', 't_squared', 'plusminus_1', 'number', 'transform', 'prefix')
    _SET = ('x', 'y', 'z', 't_squared', 'plusminus_1', 'transform', 'number', 'prefix')

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
    x = _field.Field(types.Real, 'Parallel-to-y-axis cone center x component', required=True)
    y = _field.Field(types.Real, 'Parallel-to-y-axis cone center y component', required=True)
    z = _field.Field(types.Real, 'Parallel-to-y-axis cone center z component', required=True)
    t_squared = _field.Field(types.Real, 'Parallel-to-y-axis cone t^2 coefficent', required=True)
    plusminus_1 = _field.Field(types.Real, 'Parallel-to-y-axis cone sheet selector', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? k/y( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `K_y`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `K_y`.
        """

        vis = shapes.ConeUnbounded(float(self.t_squared) ** (1 / 2), float(self.plusminus_1))
        vis = vis.rotate(numpy.array((1, 0, 0)), 90, (0, 0, 0))
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
        Generates INP from `K_y`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.x} {self.y} {self.z} {self.t_squared} {self.plusminus_1}'
        source = _card.Card._postprocess(source)

        return source
