import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Gmvfile(_field.Fields, _option.EmbedOption):
    """
    Represents INP `gmvfile` elements.
    """

    _KEYWORD = 'gmvfile'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    filename = _field.Field(types.String, 'Name of the GMV output file', required=True, numeric=())

    _REGEX = re.compile(rf'\Agmvfile( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
