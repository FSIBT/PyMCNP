import re

from .. import _field
from . import f
from . import _option
from ... import errors


class Ccc_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `ccc` elements variation #1.
    """

    _KEYWORD = 'ccc'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Accc( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
