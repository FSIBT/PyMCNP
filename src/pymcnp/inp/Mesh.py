import re

from . import _field
from . import mesh
from . import _card


class Mesh(_field.Fields, _card.Card):
    """
    Represents INP `mesh` cards.
    """

    _KEYWORD = 'mesh'

    options = _field.Field.tuple(mesh.MeshOption, 'Dictionary of options', numeric=())

    _REGEX = re.compile(rf'\Amesh((?: (?:{mesh.MeshOption._REGEX.pattern[2:-2]}))+?)?\Z', re.IGNORECASE)
