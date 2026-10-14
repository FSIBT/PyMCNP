import re

from .. import _field
from . import _option
from ... import types


class Kinetics(_field.Fields, _option.KoptsOption):
    """
    Represents INP `kinetics` elements.
    """

    _KEYWORD = 'kinetics'

    setting = _field.Field(types.String, 'Yes/No calculate point-kinetics parameters', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Akinetics( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
