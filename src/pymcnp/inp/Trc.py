import re

import numpy

from . import _field
from . import _card
from .. import _show
from .. import types
from .. import errors


class Trc(_field.Fields, _card.Card):
    """
    Represents INP `trc` surface cards.
    """

    _KEYWORD = 'trc'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('vx', 'vy', 'vz', 'hx', 'hy', 'hz', 'r1', 'r2', 'number', 'transform', 'prefix')
    _SET = ('vx', 'vy', 'vz', 'hx', 'hy', 'hz', 'r1', 'r2', 'transform', 'number', 'prefix')

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
    vx = _field.Field(types.Real, 'Truncated cone position vector x component', required=True)
    vy = _field.Field(types.Real, 'Truncated cone position vector y component', required=True)
    vz = _field.Field(types.Real, 'Truncated cone position vector z component', required=True)
    hx = _field.Field(types.Real, 'Truncated cone height vector x component', required=True)
    hy = _field.Field(types.Real, 'Truncated cone height vector y component', required=True)
    hz = _field.Field(types.Real, 'Truncated cone height vector z component', required=True)
    r1 = _field.Field(types.Real, 'Truncated cone lower cone radius', required=True)
    r2 = _field.Field(types.Real, 'Truncated cone upper cone radius', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? trc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Trc`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Trc`
        """

        h = numpy.array((float(self.hx), float(self.hy), float(self.hz)))

        cross = numpy.cross(h, numpy.array((0, 0, 1)))
        angle = numpy.degrees(numpy.arccos(h[2] / numpy.linalg.norm(h)))

        vis = shapes.ConeTruncated(numpy.linalg.norm(h), float(self.r1), float(self.r2))
        vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(numpy.array((float(self.vx), float(self.vy), float(self.vz))))

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
        Generates INP from `Trc`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.vx} {self.vy} {self.vz} {self.hx} {self.hy} {self.hz} {self.r1} {self.r2}'
        source = _card.Card._postprocess(source)

        return source
