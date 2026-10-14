import re

import numpy

from . import _field
from . import _card
from .. import _show
from .. import types
from .. import errors


class Ell(_field.Fields, _card.Card):
    """
    Represents INP `ell` surface cards.
    """

    _KEYWORD = 'ell'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('v1x', 'v1y', 'v1z', 'v2x', 'v2y', 'v2z', 'rm', 'number', 'transform', 'prefix')
    _SET = ('v1x', 'v1y', 'v1z', 'v2x', 'v2y', 'v2z', 'rm', 'transform', 'number', 'prefix')

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
    v1x = _field.Field(types.Real, 'Ellipsoid focus #1 or center x component', required=True)
    v1y = _field.Field(types.Real, 'Ellipsoid focus #1 or center y component', required=True)
    v1z = _field.Field(types.Real, 'Ellipsoid focus #1 or center z component', required=True)
    v2x = _field.Field(types.Real, 'Ellipsoid focus #2 or major axis x component', required=True)
    v2y = _field.Field(types.Real, 'Ellipsoid focus #2 or major axis y component', required=True)
    v2z = _field.Field(types.Real, 'Ellipsoid focus #2 or major axis z component', required=True)
    rm = _field.Field(types.Real, 'Ellipsoid major/minor axis radius length', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? ell( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Ell`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Ell`.
        """

        v1 = numpy.array((float(self.v1x), float(self.v1y), float(self.v1z)))
        v2 = numpy.array((float(self.v2x), float(self.v2y), float(self.v2z)))

        if self.rm > 0:
            center = numpy.array(((v2 - v1)[0] / 2 + v1[0], (v2 - v1)[1] / 2 + v1[1], (v2 - v1)[2] / 2 + v1[2]))
            major_length = float(self.rm)
            minor_length = 2 * (((major_length / 2) ** 2 - (numpy.linalg.norm(v2 - v1) / 2) ** 2) ** 0.5)

            if numpy.linalg.norm(v2 - v1):
                cross = numpy.cross(v2 - v1, numpy.array((1, 0, 0)))
                angle = numpy.degrees(numpy.arccos((v2 - v1)[0] / numpy.linalg.norm(v2 - v1)))
            else:
                cross = None
                angle = 0
        if self.rm < 0:
            center = v1
            major_length = numpy.linalg.norm(v2)
            minor_length = -float(self.rm)
            cross = numpy.cross(v2, numpy.array((1, 0, 0)))
            angle = numpy.degrees(numpy.arccos(v2[0] / numpy.linalg.norm(v2)))

        vis = shapes.Ellipsoid(major_length, minor_length)
        if cross is not None:
            vis = vis.rotate(cross, angle, (0, 0, 0))
        vis = vis.translate(center)

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
        Generates INP from `Ell`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.v1x} {self.v1y} {self.v1z} {self.v2x} {self.v2y} {self.v2z} {self.rm}'
        source = _card.Card._postprocess(source)

        return source
