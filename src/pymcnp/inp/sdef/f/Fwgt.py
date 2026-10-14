import re

from ... import _field
from . import _option
from .... import types


class Fwgt(_field.Fields, _option.FOption):
    """
    Represents INP `fwgt` elements.
    """

    _KEYWORD = 'fwgt'

    distribution = _field.Field(types.Distribution, 'Dependent distribution', required=True, numeric=())

    _REGEX = re.compile(rf'\Afwgt( {types.Distribution._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
