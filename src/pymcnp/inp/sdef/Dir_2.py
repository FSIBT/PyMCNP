import re

from .. import _field
from . import f
from . import _option


class Dir_2(_field.Fields, _option.SdefOption):
    """
    Represents INP `dir` elements variation #2.
    """

    _KEYWORD = 'dir'

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Adir( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
