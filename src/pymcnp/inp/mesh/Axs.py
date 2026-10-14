import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Axs(_field.Fields, _option.MeshOption):
    """
    Represents INP `axs` elements.
    """

    _KEYWORD = 'axs'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    vector = _field.Field.tuple(types.Real, 'Vector giving the direction of the polar axis', required=True)

    _REGEX = re.compile(rf'\Aaxs((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
