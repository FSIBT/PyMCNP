import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Sample(_field.Fields, _option.ActOption):
    """
    Represents INP `sample` elements.
    """

    _KEYWORD = 'sample'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Flag for correlated or uncorrelated', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'correlate', 'nonfiss_cor'})

    _REGEX = re.compile(rf'\Asample( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
