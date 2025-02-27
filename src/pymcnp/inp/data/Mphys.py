import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Mphys(DataOption_, keyword='mphys'):
    """
    Represents INP mphys elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'mphys( \S+)?')

    def __init__(self, setting: types.String = None):
        """
        Initializes ``Mphys``.

        Parameters:
            setting: Physics models on/off.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is not None and setting not in {'on', 'off'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting
