import re

from . import _option
from ...utils import types
from ...utils import errors


class Files(_option.DataOption):
    """
    Represents INP files elements.
    """

    _KEYWORD = 'files'

    _ATTRS = {
        'creations': types.Tuple[types.File],
    }

    _REGEX = re.compile(rf'\Afiles((?: {types.File._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, creations: list[str] | list[types.File]):
        """
        Initializes ``Files``.

        Parameters:
            creations: Files to create.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.creations: types.Tuple[types.File] = creations

    @property
    def creations(self) -> types.Tuple[types.File]:
        """
        Files to create

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._creations

    @creations.setter
    def creations(self, creations: list[str] | list[types.File]) -> None:
        """
        Sets ``creations``.

        Parameters:
            creations: Files to create.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if creations is not None:
            array = []
            for item in creations:
                if isinstance(item, types.File):
                    array.append(item)
                elif isinstance(item, str):
                    array.append(types.File.from_mcnp(item))
            creations = types.Tuple(array)

        if creations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, creations)

        self._creations: types.Tuple[types.File] = creations
