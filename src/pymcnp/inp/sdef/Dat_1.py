import re

from .. import _field
from . import f
from . import _option


class Dat_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `dat` elements variation #1.
    """

    _KEYWORD = 'dat'

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Adat( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
