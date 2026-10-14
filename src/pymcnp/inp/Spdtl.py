import re

from . import _field
from . import _card
from .. import types


class Spdtl(_field.Fields, _card.Card):
    """
    Represents INP `spdtl` cards.
    """

    _KEYWORD = 'spdtl'

    keyword = _field.Field(types.String, 'Keyword in {"force", "off"}', required=True, numeric=())

    _REGEX = re.compile(rf'\Aspdtl( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
