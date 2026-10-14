import re

from .. import _field
from . import _option
from ... import types


class Pnlib(_field.Fields, _option.MOption_0):
    """
    Represents INP `pnlib` elements.
    """

    _KEYWORD = 'pnlib'

    abx = _field.Field(types.String, 'Default photonuclear table identifier', required=True, numeric=())

    _REGEX = re.compile(rf'\Apnlib( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
