import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Dn(_field.Fields, _option.ActOption):
    """
    Represents INP `dn` elements.
    """

    _KEYWORD = 'dn'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    source = _field.Field(types.String, 'Delayed neutron data source', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'model', 'library', 'both', 'prompt'})

    _REGEX = re.compile(rf'\Adn( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
