import re

from .. import _field
from . import _option
from ... import types


class Nonfiss(_field.Fields, _option.ActOption):
    """
    Represents INP `nonfiss` elements.
    """

    _KEYWORD = 'nonfiss'

    kind = _field.Field(
        types.String,
        'Type of delayed particle(s) to be produced by simple multi-particle reaction',
        required=True,
        numeric=(),
        invalid=lambda self, value: value.value.lower() not in {'none', 'n,p,e,f,a', 'all'},
    )

    _REGEX = re.compile(rf'\Anonfiss( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
