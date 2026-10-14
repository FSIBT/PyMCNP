import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Filetype(_field.Fields, _option.EmbedOption):
    """
    Represents INP `filetype` elements.
    """

    _KEYWORD = 'filetype'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    kind = _field.Field(types.String, 'File type for the elemental edit output file', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'ascii', 'binary'})

    _REGEX = re.compile(rf'\Afiletype( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
