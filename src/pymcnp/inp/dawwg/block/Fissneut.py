import re

from ... import _field
from . import _option
from .... import types


class Fissneut(_field.Fields, _option.BlockOption):
    """
    Represents INP `fissneut` elements.
    """

    _KEYWORD = 'fissneut'

    setting = _field.Field(types.Integer, 'Fission neutron flag', required=True, numeric=int)

    _REGEX = re.compile(rf'\Afissneut( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
