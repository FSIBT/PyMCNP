import re
import typing


from .option_ import TroptOption_
from ....utils import types
from ....utils import errors


class Nreact(TroptOption_, keyword='nreact'):
    """
    Represents INP nreact elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'nreact( \S+)')

    def __init__(self, setting: types.String):
        """
        Initializes ``Nreact``.

        Parameters:
            setting: Nuclear reactions setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'off', 'on', 'atten', 'remove'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting
