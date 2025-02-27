import re
import typing


from .option_ import FmultOption_
from ....utils import types
from ....utils import errors


class Data(FmultOption_, keyword='data'):
    """
    Represents INP data elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(r'data( \S+)')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Data``.

        Parameters:
            setting: Sampling method setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting
