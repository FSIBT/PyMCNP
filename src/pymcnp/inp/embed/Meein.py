import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Meein(_field.Fields, _option.EmbedOption):
    """
    Represents INP `meein` elements.
    """

    _KEYWORD = 'meein'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    filename = _field.Field(types.String, 'Name of the EEOUT results file to read', required=True, numeric=())

    _REGEX = re.compile(rf'\Ameein( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
