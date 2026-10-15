import re

from .. import _field
from . import _option
from ... import types


class Xs_2(_field.Fields, _option.MplotOption):
    """
    Represents INP `xs` elements variation #2.
    """

    _KEYWORD = 'xs'

    m = _field.Field(types.String, 'Material question mark', required=True, numeric=(), invalid=lambda self, value: value != '?')

    _REGEX = re.compile(rf'\Axs( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
