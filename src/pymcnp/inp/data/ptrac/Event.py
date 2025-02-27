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
        'setting': types.String,
    }

    _REGEX = re.compile(r'event( \S+)')

    def __init__(self, setting: types.String):
        """
        Initializes ``Event``.

        Parameters:
            setting: Specifies the type of events written to the PTRAC file.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'src', 'bnk', 'sur', 'col', 'ter', 'cap'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting
