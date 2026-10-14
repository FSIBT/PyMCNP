import re

from .. import _field
from . import f
from . import _option


class Axs_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `axs` elements variation #1.
    """

    _KEYWORD = 'axs'

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Aaxs( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
