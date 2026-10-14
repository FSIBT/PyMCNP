import re

from . import _field
from . import _card
from .. import types
from .. import errors


class Y(_field.Fields, _card.Card):
    """
    Represents INP `y` surface cards.
    """

    _KEYWORD = 'y'

    _ORDER = ('y1', 'r1', 'y2', 'r2', 'y3', 'r3', 'number', 'transform', 'prefix')
    _SET = ('y1', 'r1', 'y2', 'r2', 'y3', 'r3', 'transform', 'number', 'prefix')

    prefix = _field.Field(types.String, 'Surface whitebody/reflecting flag', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'*', '+'})
    number = _field.Field(
        types.Integer, 'Surface number', required=True, default=lambda card: next(_card.NUMBER), numeric=int, invalid=lambda self, value: not 1 <= value <= (99999999 if not self.transform else 999)
    )
    transform = _field.Field(types.Integer, 'Surface transform', numeric=int, invalid=lambda self, value: value is not None and (not 0 <= value <= 999))
    y1 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #1 y component', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    r1 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #1 radius', required=True, code=errors.InpCode.SEMANTICS_OPTION)
    y2 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #2 y component')
    r2 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #2 radius')
    y3 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #3 y component')
    r3 = _field.Field(types.Real, 'Y-axisymmetric point-defined surface point #3 radius')

    _REGEX = re.compile(
        rf'\A(\+|\*)?(\S+)( \S+)? y( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

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
        Generates INP from `Y`.

        Returns:
            INP surface card.
        """

        source = f'{self.prefix if self.prefix is not None else ""}{self.number} {self.transform if self.transform is not None else ""} {self._KEYWORD} {self.y1} {self.r1} {self.y2 if self.y2 is not None else ""} {self.r2 if self.r2 is not None else ""} {self.y3 if self.y3 is not None else ""} {self.r3 if self.r3 is not None else ""}'
        source = _card.Card._postprocess(source)

        return source
