import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Zlev(_field.Fields, _option.MplotOption):
    """
    Represents INP `zlev` elements.
    """

    _KEYWORD = 'zlev'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    n = _field.Field.tuple(types.String, 'Scales of tally plots', required=True, numeric=())

    _REGEX = re.compile(rf'\Azlev((?: {types.String._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
