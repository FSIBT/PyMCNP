import re

from .. import _field
from . import matcell
from . import _option


class Matcell(_field.Fields, _option.EmbedOption):
    """
    Represents INP `matcell` elements.
    """

    _KEYWORD = 'matcell'

    pairs = _field.Field.tuple(matcell.Entry, 'Tuple of material-cell paris', required=True, numeric=())

    _REGEX = re.compile(rf'\Amatcell((?: {matcell.Entry._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
