import re

from .. import _field
from . import _option
from ... import types
from ... import errors


class Par(_field.Fields, _option.MplotOption):
    """
    Represents INP `par` elements.
    """

    _KEYWORD = 'par'

    _CODE = errors.InpCode.SEMANTICS_OPTION

    particle = _field.Field(types.Designator, 'Particle type to plot', required=True, numeric=())

    _REGEX = re.compile(rf'\Apar( {types.Designator._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
