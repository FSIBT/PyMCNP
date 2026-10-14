import re

from ... import _field
from . import _option
from .... import types


class Lng(_field.Fields, _option.BlockOption):
    """
    Represents INP `lng` elements.
    """

    _KEYWORD = 'lng'

    setting = _field.Field(types.Integer, 'Number of the last neutron group', required=True, numeric=int)

    _REGEX = re.compile(rf'\Alng( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
