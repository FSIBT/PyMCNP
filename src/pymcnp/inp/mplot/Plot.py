import re

from .. import _field
from . import _option


class Plot(_field.Fields, _option.MplotOption):
    """
    Represents INP `plot` elements.
    """

    _KEYWORD = 'plot'

    _REGEX = re.compile(r'\Aplot\Z', re.IGNORECASE)
