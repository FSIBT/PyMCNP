import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Mcnpumfile(_field.Fields, _option.EmbedOption):
    """
    Represents INP `mcnpumfile` elements.
    """

    _KEYWORD = 'mcnpumfile'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    filename = _field.Field(types.String, 'Name of the MCNPUM output file', required=True, numeric=())

    _REGEX = re.compile(rf'\Amcnpumfile( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
