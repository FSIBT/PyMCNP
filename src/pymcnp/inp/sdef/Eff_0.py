import re

from .. import _field
from . import _option
from ... import types


class Eff_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `eff` elements variation #0.
    """

    _KEYWORD = 'eff'

    criterion = _field.Field(types.Real, 'Rejection efficiency criterion for position sampling', required=True)

    _REGEX = re.compile(rf'\Aeff( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
