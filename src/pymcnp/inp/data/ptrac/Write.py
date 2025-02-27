import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Write(PtracOption_, keyword='write'):
    """
    Represents INP write elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'write( \S+)')

    def __init__(self, setting: types.String):
        """
        Initializes ``Write``.

        Parameters:
            setting: Controls what particle parameters are written.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'pos', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting
