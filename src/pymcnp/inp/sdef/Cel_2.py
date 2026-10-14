import re

from .. import _field
from . import f
from . import _option


class Cel_2(_field.Fields, _option.SdefOption):
    """
    Represents INP `cel` elements variation #2.
    """

    _KEYWORD = 'cel'

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Acel( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
