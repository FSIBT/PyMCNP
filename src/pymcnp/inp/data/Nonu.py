import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Nonu(DataOption_, keyword='nonu'):
    """
    Represents INP nonu elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'settings': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Anonu((?: {types.IntegerOrJump._REGEX.pattern})+?)?\Z')

    def __init__(self, settings: types.Tuple[types.IntegerOrJump] = None):
        """
        Initializes ``Nonu``.

        Parameters:
            settings: Tuple of fission settings.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if settings is not None and not (
            filter(lambda entry: not (entry == 0 or entry == 1 or entry == 2), settings)
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, settings)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                settings,
            ]
        )

        self.settings: typing.Final[types.Tuple[types.IntegerOrJump]] = settings
