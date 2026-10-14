import re

from .. import _field
from . import contour
from . import _option
from ... import types


class Contour(_field.Fields, _option.MplotOption):
    """
    Represents INP `contour` elements.
    """

    _KEYWORD = 'contour'

    cmin = _field.Field(types.Real, 'Contour lower limit', required=True)
    cmax = _field.Field(types.Real, 'Contour upper limit', required=True)
    cstep = _field.Field(types.Real, 'Contour interval', required=True)
    options = _field.Field.tuple(contour.ContourOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(
        rf'\Acontour( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})((?: (?:{contour.ContourOption._REGEX.pattern[2:-2]}))+?)?\Z',
        re.IGNORECASE,
    )
