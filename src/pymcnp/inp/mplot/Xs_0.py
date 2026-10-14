import re

from .. import _field
from . import _option
from ... import types


class Xs_0(_field.Fields, _option.MplotOption):
    """
    Represents INP `xs` elements variation #0.
    """

    _KEYWORD = 'xs'

    m = _field.Field(types.Integer, 'Material number', required=True, numeric=int)

    _REGEX = re.compile(rf'\Axs( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
