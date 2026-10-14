import re

from .. import _field
from . import _option
from ... import types


class Debug(_field.Fields, _option.EmbedOption):
    """
    Represents INP `debug` elements.
    """

    _KEYWORD = 'debug'

    parameter = _field.Field(types.String, 'Debug parameter', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'echomesh'})

    _REGEX = re.compile(rf'\Adebug( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
