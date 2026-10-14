import re

from . import _field
from . import _card
from .. import _show
from .. import types
from .. import errors


class Rpp(_field.Fields, _card.Card):
    """
    Represents INP `rpp` surface cards.
    """

    _KEYWORD = 'rpp'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = ('xmin', 'xmax', 'ymin', 'ymax', 'zmin', 'zmax', 'number', 'transform', 'prefix')
    _SET = ('xmin', 'xmax', 'ymin', 'ymax', 'zmin', 'zmax', 'transform', 'number', 'prefix')

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
    xmin = _field.Field(types.Real, 'Parallelepiped x termini minimum', required=True)
    xmax = _field.Field(types.Real, 'Parallelepiped x termini maximum', required=True)
    ymin = _field.Field(types.Real, 'Parallelepiped y termini minimum', required=True)
    ymax = _field.Field(types.Real, 'Parallelepiped y termini maximum', required=True)
    zmin = _field.Field(types.Real, 'Parallelepiped z termini minimum')
    zmax = _field.Field(types.Real, 'Parallelepiped z termini maximum')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? rpp( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `Rpp`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `Rpp`
        """

        vis = shapes.Parallelipiped(
            float(self.xmin),
            float(self.xmax),
            float(self.ymin),
            float(self.ymax),
            float(self.zmin),
            float(self.zmax),
        )

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
        Generates INP from `Rpp`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.xmin} {self.xmax} {self.ymin} {self.ymax} {self.zmin if self.zmin is not None else ""} {self.zmax if self.zmax is not None else ""}'
        source = _card.Card._postprocess(source)

        return source
