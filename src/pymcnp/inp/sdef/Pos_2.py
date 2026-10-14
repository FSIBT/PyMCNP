import re

from .. import _field
from . import f
from . import _option


class Pos_2(_field.Fields, _option.SdefOption):
    """
    Represents INP `pos` elements variation #2.
    """

    _KEYWORD = 'pos'

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Apos( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
