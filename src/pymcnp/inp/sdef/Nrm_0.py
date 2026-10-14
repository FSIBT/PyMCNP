import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Nrm_0(_field.Fields, _option.SdefOption):
    """
    Represents INP `nrm` elements variation #0.
    """

    _KEYWORD = 'nrm'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    sign = _field.Field(types.Integer, 'Sign of the surface normal', required=True, numeric=int)

    _REGEX = re.compile(rf'\Anrm( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
