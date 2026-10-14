import re

from .. import _field
from . import f
from . import _option
from ... import errors


class Sur_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `sur` elements variation #1.
    """

    _KEYWORD = 'sur'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    option = _field.Field(f.FOption, 'Dependent distribution option', required=True, numeric=())

    _REGEX = re.compile(rf'\Asur( (?:{f.FOption._REGEX.pattern[2:-2]}))\Z', re.IGNORECASE)
