import re

from .. import _field
from . import _option
from ... import errors


class Loglog(_field.Fields, _option.MplotOption):
    """
    Represents INP `loglog` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'loglog'

    _REGEX = re.compile(r'\Aloglog\Z', re.IGNORECASE)
