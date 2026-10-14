import re

from .. import _field
from . import _option
from ... import types


class Mgeoin(_field.Fields, _option.EmbedOption):
    """
    Represents INP `mgeoin` elements.
    """

    _KEYWORD = 'mgeoin'

    filename = _field.Field(types.String, 'Name of the input file containing the mesh description', required=True, numeric=())

    _REGEX = re.compile(rf'\Amgeoin( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
