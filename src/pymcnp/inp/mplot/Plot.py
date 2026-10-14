import re

from .. import _field
from . import _option
from ... import errors


class Plot(_field.Fields, _option.MplotOption):
    """
    Represents INP `plot` elements.
    """

    _CODE = errors.InpCode.SEMANTICS_CARD

    _KEYWORD = 'plot'

    _REGEX = re.compile(r'\Aplot\Z', re.IGNORECASE)
