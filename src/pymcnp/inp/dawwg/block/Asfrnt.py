import re

from ... import _field
from . import _option
from .... import types


class Asfrnt(_field.Fields, _option.BlockOption):
    """
    Represents INP `asfrnt` elements.
    """

    _KEYWORD = 'asfrnt'

    setting = _field.Field(types.Integer, 'Back-going flux at plane k', required=True, numeric=int)

    _REGEX = re.compile(rf'\Aasfrnt( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)
