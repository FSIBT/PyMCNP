import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Files(DataOption):
    """
    Represents INP files elements.

    Attributes:
        creations: Files to create.
    """

    _KEYWORD = 'files'

    _ATTRS = {
        'creations': types.Tuple[types.File],
    }

    _REGEX = re.compile(rf'\Afiles((?: {types.File._REGEX.pattern})+?)\Z')

    def __init__(self, creations: types.Tuple[types.File]):
        """
        Initializes ``Files``.

        Parameters:
            creations: Files to create.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if creations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, creations)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                creations,
            ]
        )

        self.creations: typing.Final[types.Tuple[types.File]] = creations


@dataclasses.dataclass
class FilesBuilder:
    """
    Builds ``Files``.

    Attributes:
        creations: Files to create.
    """

    creations: list[str] | list[types.File]

    def build(self):
        """
        Builds ``FilesBuilder`` into ``Files``.

        Returns:
            ``Files`` for ``FilesBuilder``.
        """

        if self.creations:
            creations = []
            for item in self.creations:
                if isinstance(item, types.File):
                    creations.append(item)
                elif isinstance(item, str):
                    creations.append(types.File.from_mcnp(item))
                else:
                    creations.append(item.build())
            creations = types.Tuple(creations)
        else:
            creations = None

        return Files(
            creations=creations,
        )

    @staticmethod
    def unbuild(ast: Files):
        """
        Unbuilds ``Files`` into ``FilesBuilder``

        Returns:
            ``FilesBuilder`` for ``Files``.
        """

        return Files(
            creations=copy.deepcopy(ast.creations),
        )
