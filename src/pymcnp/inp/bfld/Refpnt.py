import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Refpnt(_field.Fields, _option.BfldOption):
    """
    Represents INP `refpnt` elements.
    """

    _KEYWORD = 'refpnt'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    point = _field.Field.tuple(types.Real, 'Point anywhere on the quadrapole beam', required=True)

    _REGEX = re.compile(rf'\Arefpnt((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
