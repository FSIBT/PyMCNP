import re

from .. import _field
from . import _option
from ... import types


class Mcnpumfile(_field.Fields, _option.EmbedOption):
    """
    Represents INP `mcnpumfile` elements.
    """

    _KEYWORD = 'mcnpumfile'

    filename = _field.Field(types.String, 'Name of the MCNPUM output file', required=True, numeric=())

    _REGEX = re.compile(rf'\Amcnpumfile( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
