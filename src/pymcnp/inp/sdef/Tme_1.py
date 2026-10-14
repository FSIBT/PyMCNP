import re

from .. import _field
from . import tme_1
from . import _option
from ... import errors


class Tme_1(_field.Fields, _option.SdefOption):
    """
    Represents INP `tme` elements variation #1.
    """

    _KEYWORD = 'tme'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    time = _field.Field(tme_1.Embedded, 'Time in shakes', required=True, numeric=())

    _REGEX = re.compile(rf'\Atme( {tme_1.Embedded._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
