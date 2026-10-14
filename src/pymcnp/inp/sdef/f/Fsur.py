import re

from ... import _field
from . import _option
from .... import types


class Fsur(_field.Fields, _option.FOption):
    """
    Represents INP `fsur` elements.
    """

    _KEYWORD = 'fsur'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afsur( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
