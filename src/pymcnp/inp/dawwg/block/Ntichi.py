import re

from ... import _field
from . import _option
from .... import types


class Ntichi(_field.Fields, _option.BlockOption):
    """
    Represents INP `ntichi` elements.
    """

    _KEYWORD = 'ntichi'

    setting = _field.Field(types.Integer, 'MENDF fission fraction', required=True, numeric=int)

    _REGEX = re.compile(rf'\Antichi( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
