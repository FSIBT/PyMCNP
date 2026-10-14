import re

from . import _field
from . import df_1
from . import _card
from .. import types


class Df_1(_field.Fields, _card.Card):
    """
    Represents INP df cards variation #1.
    """

    _KEYWORD = 'df'

    suffix = _field.Field(types.Integer, 'Data card option suffix', required=True, numeric=int, invalid=lambda self, value: not value <= 99999999)
    options = _field.Field.tuple(df_1.DfOption_1, 'Dictionary of options', required=True, numeric=())

    _REGEX = re.compile(rf'\Adf(\d+)((?: (?:{df_1.DfOption_1._REGEX.pattern[2:-2]}))+?)\Z', re.IGNORECASE)
