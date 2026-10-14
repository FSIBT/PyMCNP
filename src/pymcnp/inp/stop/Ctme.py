import re

from .. import _field
from . import _option
from ... import types


class Ctme(_field.Fields, _option.StopOption):
    """
    Represents INP `ctme` elements.
    """

    _KEYWORD = 'ctme'

    tme = _field.Field(types.Real, 'Computer time before stop', required=True)

    _REGEX = re.compile(rf'\Actme( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
