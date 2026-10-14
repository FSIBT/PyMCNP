import re

from . import _field
from . import _card
from .. import types


class Hsrc(_field.Fields, _card.Card):
    """
    Represents INP `hsrc` cards.
    """

    _KEYWORD = 'hsrc'

    x_number = _field.Field(types.Integer, 'Number of mesh intervals in x direction', required=True, numeric=int, invalid=lambda self, value: not value > 0)
    x_minimum = _field.Field(types.Real, 'Minimum x-value for mesh', required=True)
    x_maximum = _field.Field(types.Real, 'Maximum x-value for mesh', required=True)
    y_number = _field.Field(types.Integer, 'Number of mesh intervals in y direction', required=True, numeric=int, invalid=lambda self, value: not value > 0)
    y_minimum = _field.Field(types.Real, 'Minimum y-value for mesh', required=True)
    y_maximum = _field.Field(types.Real, 'Maximum y-value for mesh', required=True)
    z_number = _field.Field(types.Integer, 'Number of mesh intervals in z direction', required=True, numeric=int, invalid=lambda self, value: not value > 0)
    z_minimum = _field.Field(types.Real, 'Minimum z-value for mesh', required=True)
    z_maximum = _field.Field(types.Real, 'Maximum z-value for mesh', required=True)

    _REGEX = re.compile(
        rf'\Ahsrc( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )
