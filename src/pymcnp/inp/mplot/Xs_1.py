import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Xs_1(_field.Fields, _option.MplotOption):
    """
    Represents INP `xs` elements variation #1.
    """

    _KEYWORD = 'xs'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    m = _field.Field(types.Zaid, 'Material ZAID', required=True, numeric=())

    _REGEX = re.compile(rf'\Axs( {types.Zaid._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
