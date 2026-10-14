import re

from .. import _field
from . import f
from . import _option


class Tme_2(_field.Fields, _option.SdefOption):
    """
    Represents INP `tme` elements variation #2.
    """

    _KEYWORD = 'tme'

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Atme( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
