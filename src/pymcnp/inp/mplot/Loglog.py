import re

from .. import _field
from . import _option


class Loglog(_field.Fields, _option.MplotOption):
    """
    Represents INP `loglog` elements.
    """

    _KEYWORD = 'loglog'

    _REGEX = re.compile(r'\Aloglog\Z', re.IGNORECASE)
