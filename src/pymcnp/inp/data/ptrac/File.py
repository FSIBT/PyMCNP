import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class File(PtracOption_, keyword='file'):
    """
    Represents INP file elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'file( {types.String._REGEX.pattern})')

    def __init__(self, setting: types.String):
        """
        Initializes ``File``.

        Parameters:
            setting: PTRAC file type.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'asc', 'bin', 'aov', 'bov'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting
