import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Ibt(_field.Fields, _option.BlockOption):
    """
    Represents INP `ibt` elements.
    """

    _KEYWORD = 'ibt'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'Top boudary condition', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aibt( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
