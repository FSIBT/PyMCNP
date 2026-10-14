import re

from .. import _field
from . import dgeb
from . import _option


class Dgeb(_field.Fields, _option.ActOption):
    """
    Represents INP `dgeb` elements.
    """

    _KEYWORD = 'dgeb'

    biases = _field.Field.tuple(dgeb.Bias, 'Delayed neutron energy biases', required=True, numeric=())

    _REGEX = re.compile(rf'\Adgeb((?: {dgeb.Bias._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
