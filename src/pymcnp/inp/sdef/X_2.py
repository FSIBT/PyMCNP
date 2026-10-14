import re

from .. import _field
from . import f
from . import _option


class X_2(_field.Fields, _option.SdefOption):
    """
    Represents INP `x` elements variation #2.
    """

    _KEYWORD = 'x'

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Ax( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
