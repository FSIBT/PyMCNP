import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Meeout(_field.Fields, _option.EmbedOption):
    """
    Represents INP `meeout` elements.
    """

    _KEYWORD = 'meeout'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    filename = _field.Field(types.String, 'Name assigned to EEOUT, the elemental edit output file', required=True, numeric=())

    _REGEX = re.compile(rf'\Ameeout( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
