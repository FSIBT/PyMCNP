import re

from . import _field
from . import _card
from .. import types


class Leb(_field.Fields, _card.Card):
    """
    Represents INP `leb` cards.
    """

    _KEYWORD = 'leb'

    yzere = _field.Field(types.Real, 'Y0 parameter in level-density formula for Z≤70', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value > 0)))
    bzere = _field.Field(types.Real, 'B0 parameter in level-density formula for Z≤70', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value > 0)))
    yzero = _field.Field(types.Real, 'Y0 parameter in level-density formula for Z≥71', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value > 0)))
    bzero = _field.Field(types.Real, 'B0 parameter in level-density formula for Z≥70', invalid=lambda self, value: value is not None and (not (isinstance(value.value, types.Jump) or value > 0)))

    _REGEX = re.compile(rf'\Aleb( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z', re.IGNORECASE)
