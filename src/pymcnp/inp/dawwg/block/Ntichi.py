import re

from ... import _field
from . import _option
from .... import types
from .... import errors


class Ntichi(_field.Fields, _option.BlockOption):
    """
    Represents INP `ntichi` elements.
    """

    _KEYWORD = 'ntichi'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.Integer, 'MENDF fission fraction', required=True, numeric=int)

    _REGEX = re.compile(rf'\Antichi( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
