import re

from .. import _field
from . import dneb
from . import _option


class Dneb(_field.Fields, _option.ActOption):
    """
    Represents INP `dneb` elements.
    """

    _KEYWORD = 'dneb'

    biases = _field.Field.tuple(dneb.Bias, 'Delayed neutron energy biases', required=True, numeric=())

    _REGEX = re.compile(rf'\Adneb((?: {dneb.Bias._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
