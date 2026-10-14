import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Tme_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `tme` elements variation #0.
    """

    _KEYWORD = 'tme'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    time = _field.Field(types.Real, 'Time in shakes', required=True)

    _REGEX = re.compile(rf'\Atme( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
