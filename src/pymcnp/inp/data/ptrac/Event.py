import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Event(PtracOption_, keyword='event'):
    """
    Represents INP event elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'settings': types.Tuple[types.String],
    }

    _REGEX = re.compile(rf'\Aevent ((?:{types.String._REGEX.pattern})+?)\Z')

    def __init__(self, settings: types.Tuple[types.String]):
        """
        Initializes ``Event``.

        Parameters:
            settings: Specifies the type of events written to the PTRAC file.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if settings is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, settings)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                settings,
            ]
        )

        self.settings: typing.Final[types.Tuple[types.String]] = settings
