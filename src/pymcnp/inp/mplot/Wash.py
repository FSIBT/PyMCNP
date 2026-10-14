import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Wash(_field.Fields, _option.MplotOption):
    """
    Represents INP `wash` elements.
    """

    _KEYWORD = 'wash'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    aa = _field.Field(types.String, 'Color-wash on/offs', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'on', 'off'})

    _REGEX = re.compile(rf'\Awash( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
