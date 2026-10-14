import re

from .. import _field
from . import _option
from ... import types


class Rxn(_field.Fields, _option.KpertOption):
    """
    Represents INP `rxn` elements.
    """

    _KEYWORD = 'rxn'

    numbers = _field.Field.tuple(types.Integer, 'List of reaction numbers for pertubation', required=True, numeric=int)

    _REGEX = re.compile(rf'\Arxn((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
