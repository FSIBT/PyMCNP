import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Fission(_field.Fields, _option.ActOption):
    """
    Represents INP `fission` elements.
    """

    _KEYWORD = 'fission'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    kind = _field.Field(
        types.String,
        'Type of delayed particle(s) to be produced from residuals created by fission',
        required=True,
        numeric=(),
        invalid=lambda self, value: value.value.lower() not in {'none', 'n,p,e,f,a', 'all'},
    )

    _REGEX = re.compile(rf'\Afission( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
