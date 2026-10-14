import re

from .. import _field
from . import filter
from . import _option


class Filter(_field.Fields, _option.PtracOption):
    """
    Represents INP `filter` elements.
    """

    _KEYWORD = 'filter'

    variables = _field.Field.tuple(filter.Entry, 'MCNP6 variables for filtering', required=True, numeric=())

    _REGEX = re.compile(rf'\Afilter((?: {filter.Entry._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
