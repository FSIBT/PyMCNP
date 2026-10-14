import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Elib(_field.Fields, _option.MOption_0):
    """
    Represents INP `elib` elements.
    """

    _KEYWORD = 'elib'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    abx = _field.Field(types.String, 'Default electron table identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Aelib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
