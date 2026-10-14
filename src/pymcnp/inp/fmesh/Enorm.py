import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Enorm(_field.Fields, _option.FmeshOption):
    """
    Represents INP `enorm` elements.
    """

    _KEYWORD = 'enorm'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    setting = _field.Field(types.String, 'Tally results divided by energy yes/no', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'yes', 'no'})

    _REGEX = re.compile(rf'\Aenorm( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
