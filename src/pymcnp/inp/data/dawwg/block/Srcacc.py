import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Srcacc(BlockOption_, keyword='srcacc'):
    """
    Represents INP srcacc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'srcacc( \S+)')

    def __init__(self, setting: types.String):
        """
        Initializes ``Srcacc``.

        Parameters:
            setting: Transport accelerations.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'dsa', 'tsa', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting
