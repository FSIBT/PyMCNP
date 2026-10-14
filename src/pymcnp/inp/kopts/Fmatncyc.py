import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fmatncyc(_field.Fields, _option.KoptsOption):
    """
    Represents INP `fmatncyc` elements.
    """

    _KEYWORD = 'fmatncyc'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    fmat_ncyc = _field.Field(types.Real, 'Fmat_ncyc', required=True)

    _REGEX = re.compile(rf'\Afmatncyc( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
