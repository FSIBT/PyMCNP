import re

from . import _field
from . import pikmt
from . import _card


class Pikmt(_field.Fields, _card.Card):
    """
    Represents INP `pikmt` cards.
    """

    _KEYWORD = 'pikmt'

    biases = _field.Field.tuple(pikmt.Photonbias, 'Biases for proton production', required=True, numeric=())

    _REGEX = re.compile(rf'\Apikmt((?: {pikmt.Photonbias._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
