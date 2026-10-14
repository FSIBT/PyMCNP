import re

from .. import _field
from . import f
from . import _option
from ... import errors


class Y_2(_field.Fields, _option.SdefOption):
    """
    Represents INP `y` elements variation #2.
    """

    _KEYWORD = 'y'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Ay( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
