import re

from .. import _field
from . import _option
from ... import types


class Event(_field.Fields, _option.PtracOption):
    """
    Represents INP `event` elements.
    """

    _KEYWORD = 'event'

    settings = _field.Field.tuple(types.String, 'Specifies the type of events written to the PTRAC file', required=True, numeric=())

    _REGEX = re.compile(rf'\Aevent((?: {types.String._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
