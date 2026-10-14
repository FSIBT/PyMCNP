import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Xs_2(_field.Fields, _option.MplotOption):
    """
    Represents INP `xs` elements variation #2.
    """

    _KEYWORD = 'xs'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    m = _field.Field(types.String, 'Material question mark', required=True, numeric=(), invalid=lambda self, value: not value == '?')

    _REGEX = re.compile(rf'\Axs( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
