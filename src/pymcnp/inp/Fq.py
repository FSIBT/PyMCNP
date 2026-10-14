import re

from . import _field
from . import _card
from .. import types


class Fq(_field.Fields, _card.Card):
    """
    Represents INP `fq` cards.
    """

    _KEYWORD = 'fq'

    suffix = _field.Field(types.Integer, 'Data card option suffix', numeric=int, invalid=lambda self, value: value is not None and (not value <= 99999999))
    a1 = _field.Field(
        types.String, 'Letters representing tally bin types', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}
    )
    a2 = _field.Field(
        types.String, 'Letters representing tally bin types', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}
    )
    a3 = _field.Field(
        types.String, 'Letters representing tally bin types', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}
    )
    a4 = _field.Field(
        types.String, 'Letters representing tally bin types', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}
    )
    a5 = _field.Field(
        types.String, 'Letters representing tally bin types', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}
    )
    a6 = _field.Field(
        types.String, 'Letters representing tally bin types', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}
    )
    a7 = _field.Field(
        types.String, 'Letters representing tally bin types', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}
    )
    a8 = _field.Field(
        types.String, 'Letters representing tally bin types', numeric=(), invalid=lambda self, value: value is not None and value.value.lower() not in {'f', 'd', 'u', 's', 'm', 'c', 'e', 't'}
    )

    _REGEX = re.compile(
        rf'\Afq(\d+)?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?( {types.String._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )
