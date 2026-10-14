import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Nlib(_field.Fields, _option.MOption_0):
    """
    Represents INP `nlib` elements.
    """

    _KEYWORD = 'nlib'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    abx = _field.Field(types.String, 'Default neutron table identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Anlib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
