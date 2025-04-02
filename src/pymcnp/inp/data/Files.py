import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Files(DataOption_, keyword='files'):
    """
    Represents INP files elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if creations is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, creations)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                creations,
            ]
        )

        self.creations: typing.Final[types.Tuple[types.File]] = creations
