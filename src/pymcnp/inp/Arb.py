import re

from . import _field
from . import _card
from .. import types
from .. import errors


class Arb(_field.Fields, _card.Card):
    """
    Represents INP `arb` surface cards.
    """

    _KEYWORD = 'arb'

    _CODE = errors.InpCode.SEMANTICS_OPTION
    _ORDER = (
        'ax',
        'ay',
        'az',
        'bx',
        'by',
        'bz',
        'cx',
        'cy',
        'cz',
        'dx',
        'dy',
        'dz',
        'ex',
        'ey',
        'ez',
        'fx',
        'fy',
        'fz',
        'gx',
        'gy',
        'gz',
        'hx',
        'hy',
        'hz',
        'n1',
        'n2',
        'n3',
        'n4',
        'n5',
        'n6',
        'number',
        'transform',
        'prefix',
    )
    _SET = (
        'ax',
        'ay',
        'az',
        'bx',
        'by',
        'bz',
        'cx',
        'cy',
        'cz',
        'dx',
        'dy',
        'dz',
        'ex',
        'ey',
        'ez',
        'fx',
        'fy',
        'fz',
        'gx',
        'gy',
        'gz',
        'hx',
        'hy',
        'hz',
        'n1',
        'n2',
        'n3',
        'n4',
        'n5',
        'n6',
        'transform',
        'number',
        'prefix',
    )

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
    ax = _field.Field(types.Real, 'Polyhedron corner #1 x component', required=True)
    ay = _field.Field(types.Real, 'Polyhedron corner #1 y component', required=True)
    az = _field.Field(types.Real, 'Polyhedron corner #1 z component', required=True)
    bx = _field.Field(types.Real, 'Polyhedron corner #2 x component', required=True)
    by = _field.Field(types.Real, 'Polyhedron corner #2 y component', required=True)
    bz = _field.Field(types.Real, 'Polyhedron corner #2 z component', required=True)
    cx = _field.Field(types.Real, 'Polyhedron corner #3 x component', required=True)
    cy = _field.Field(types.Real, 'Polyhedron corner #3 y component', required=True)
    cz = _field.Field(types.Real, 'Polyhedron corner #3 z component', required=True)
    dx = _field.Field(types.Real, 'Polyhedron corner #4 x component', required=True)
    dy = _field.Field(types.Real, 'Polyhedron corner #4 y component', required=True)
    dz = _field.Field(types.Real, 'Polyhedron corner #4 z component', required=True)
    ex = _field.Field(types.Real, 'Polyhedron corner #5 x component', required=True)
    ey = _field.Field(types.Real, 'Polyhedron corner #5 y component', required=True)
    ez = _field.Field(types.Real, 'Polyhedron corner #5 z component', required=True)
    fx = _field.Field(types.Real, 'Polyhedron corner #6 x component', required=True)
    fy = _field.Field(types.Real, 'Polyhedron corner #6 y component', required=True)
    fz = _field.Field(types.Real, 'Polyhedron corner #6 z component', required=True)
    gx = _field.Field(types.Real, 'Polyhedron corner #7 x component', required=True)
    gy = _field.Field(types.Real, 'Polyhedron corner #7 y component', required=True)
    gz = _field.Field(types.Real, 'Polyhedron corner #7 z component', required=True)
    hx = _field.Field(types.Real, 'Polyhedron corner #8 x component', required=True)
    hy = _field.Field(types.Real, 'Polyhedron corner #8 y component', required=True)
    hz = _field.Field(types.Real, 'Polyhedron corner #8 z component', required=True)
    n1 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #1', required=True)
    n2 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #2', required=True)
    n3 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #3', required=True)
    n4 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #4', required=True)
    n5 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #5', required=True)
    n6 = _field.Field(types.Real, 'Polyhedron four-digit side specificer #6', required=True)

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? arb( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def to_mcnp(self):
        """
        Generates INP from `Arb`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.ax} {self.ay} {self.az} {self.bx} {self.by} {self.bz} {self.cx} {self.cy} {self.cz} {self.dx} {self.dy} {self.dz} {self.ex} {self.ey} {self.ez} {self.fx} {self.fy} {self.fz} {self.gx} {self.gy} {self.gz} {self.hx} {self.hy} {self.hz} {self.n1} {self.n2} {self.n3} {self.n4} {self.n5} {self.n6}'
        source = _card.Card._postprocess(source)

        return source

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
