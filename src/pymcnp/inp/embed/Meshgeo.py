import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Meshgeo(_field.Fields, _option.EmbedOption):
    """
    Represents INP `meshgeo` elements.
    """

    _KEYWORD = 'meshgeo'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    form = _field.Field(
        types.String, 'Format specification of the embedded mesh input file', required=True, numeric=(), invalid=lambda self, value: value.value.lower() not in {'lnk3dnt', 'abaqus', 'mcnpum'}
    )

    _REGEX = re.compile(rf'\Ameshgeo( {types.String._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
