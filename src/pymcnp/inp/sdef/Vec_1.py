import re

from .. import _field
from . import f
from . import _option


class Vec_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `vec` elements variation #1.
    """

    _KEYWORD = 'vec'

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Avec( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
