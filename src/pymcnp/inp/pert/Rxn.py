import re

from .. import _field
from . import _option
from ... import types


class Rxn(_field.Fields, _option.PertOption):
    """
    Represents INP `rxn` elements.
    """

    _KEYWORD = 'rxn'

    numbers = _field.Field.tuple(types.Integer, 'ENDF/B reaction number', required=True, numeric=int)

    _REGEX = re.compile(rf'\Arxn((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
