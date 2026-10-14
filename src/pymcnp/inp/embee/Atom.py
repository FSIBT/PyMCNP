import re

from .. import _field
from . import _option
from ... import types


class Atom(_field.Fields, _option.EmbeeOption):
    """
    Represents INP `atom` elements.
    """

    _KEYWORD = 'atom'

    setting = _field.Field(types.String, 'Flag to multiply by atom density', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Aatom( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
