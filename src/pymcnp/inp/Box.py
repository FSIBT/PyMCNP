import re

import numpy

from . import _field
from . import _card
from .. import _show
from .. import types
from .. import errors


class Box(_field.Fields, _card.Card):
    """
    Represents INP `box` surface cards.
    """

    _KEYWORD = 'box'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('vx', 'vy', 'vz', 'a1x', 'a1y', 'a1z', 'a2x', 'a2y', 'a2z', 'a3x', 'a3y', 'a3z', 'number', 'transform', 'prefix')
    _SET = ('vx', 'vy', 'vz', 'a1x', 'a1y', 'a1z', 'a2x', 'a2y', 'a2z', 'a3x', 'a3y', 'a3z', 'transform', 'number', 'prefix')

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
    vx = _field.Field(types.Real, 'Box macrobody position vector x component', required=True)
    vy = _field.Field(types.Real, 'Box macrobody position vector y component', required=True)
    vz = _field.Field(types.Real, 'Box macrobody position vector z component', required=True)
    a1x = _field.Field(types.Real, 'Box macrobody vector #1 x component', required=True)
    a1y = _field.Field(types.Real, 'Box macrobody vector #1 y component', required=True)
    a1z = _field.Field(types.Real, 'Box macrobody vector #1 z component', required=True)
    a2x = _field.Field(types.Real, 'Box macrobody vector #2 x component', required=True)
    a2y = _field.Field(types.Real, 'Box macrobody vector #2 y component', required=True)
    a2z = _field.Field(types.Real, 'Box macrobody vector #2 z component', required=True)
    a3x = _field.Field(types.Real, 'Box macrobody vector #3 x component', required=True)
    a3y = _field.Field(types.Real, 'Box macrobody vector #3 y component', required=True)
    a3z = _field.Field(types.Real, 'Box macrobody vector #3 z component', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? box( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Box`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Box`.
        """

        v = numpy.array((float(self.vx), float(self.vy), float(self.vz)))
        a1 = numpy.array((float(self.a1x), float(self.a1y), float(self.a1z)))
        a2 = numpy.array((float(self.a2x), float(self.a2y), float(self.a2z)))
        a3 = numpy.array((float(self.a3x), float(self.a3y), float(self.a3z)))

        cross = numpy.cross(numpy.array((1, 0, 0)), a1)
        angle = numpy.degrees(numpy.arccos(a1[0] / numpy.linalg.norm(a1)))

        vis = shapes.Box(numpy.linalg.norm(a1), numpy.linalg.norm(a2), numpy.linalg.norm(a3))
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(v + 0.5 * (a1 + a2 + a3))

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
        Generates INP from `Box`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.vx} {self.vy} {self.vz} {self.a1x} {self.a1y} {self.a1z} {self.a2x} {self.a2y} {self.a2z} {self.a3x} {self.a3y} {self.a3z}'
        source = _card.Card._postprocess(source)

        return source
