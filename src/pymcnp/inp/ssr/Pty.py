import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Pty(_field.Fields, _option.SsrOption):
    """
    Represents INP `pty` elements.
    """

    _KEYWORD = 'pty'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    particles = _field.Field.tuple(types.Designator, 'Tuple of designators', required=True, numeric=())

    _REGEX = re.compile(rf'\Apty((?: {types.Designator._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
