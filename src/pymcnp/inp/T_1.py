import re

from . import _field
from . import t_1
from . import _card
from .. import types


class T_1(_field.Fields, _card.Card):
    """
    Represents INP `t` elements variation #1.
    """

    _KEYWORD = 't'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int)
    options = _field.Field.tuple(t_1.TOption_1, 'Dictionary of options', required=True, numeric=())

    _REGEX = re.compile(rf'\At(\d+)((?: (?:{t_1.TOption_1._REGEX.pattern[2:-2]}))+?)\Z', re.IGNORECASE)
