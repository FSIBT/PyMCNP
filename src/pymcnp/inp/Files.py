import re

from . import _field
from . import files
from . import _card


class Files(_field.Fields, _card.Card):
    """
    Represents INP `files` cards.
    """

    _KEYWORD = 'files'

    creations = _field.Field.tuple(files.File, 'Files to create', required=True, numeric=())

    _REGEX = re.compile(rf'\Afiles((?: {files.File._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)
