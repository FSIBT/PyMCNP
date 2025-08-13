import re

from . import files
from . import _card
from .. import types
from .. import errors


class Files(_card.Card):
    """
    Represents INP `files` cards.
    """

    _KEYWORD = 'files'

    _ATTRS = {
        'creations': types.Tuple(files.File),
    }

    _REGEX = re.compile(rf'\Afiles((?: {files.File._REGEX.pattern[2:-2]})+?)\Z', re.IGNORECASE)

    def __init__(self, creations: list[str] | list[files.File]):
        """
        Initializes `Files`.

        Parameters:
            creations: Files to create.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.creations: types.Tuple(files.File) = creations

    @property
    def creations(self) -> types.Tuple(files.File):
        """
        Files to create

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._creations

    @creations.setter
    def creations(self, creations: list[str] | list[files.File]) -> None:
        """
        Sets `creations`.

        Parameters:
            creations: Files to create.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if creations is not None:
            array = []
            for item in creations:
                if isinstance(item, files.File):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(files.File.from_mcnp(item))
            creations = types.Tuple(files.File)(array)

        if creations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, creations)

        self._creations: types.Tuple(files.File) = creations
