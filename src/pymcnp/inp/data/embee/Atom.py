import re
import typing


from .option_ import EmbeeOption_
from ....utils import types
from ....utils import errors


class Atom(EmbeeOption_, keyword='atom'):
    """
    Represents INP atom elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'atom( {types.String._REGEX.pattern})')

    def __init__(self, setting: types.String):
        """
        Initializes ``Atom``.

        Parameters:
            setting: Flag to multiply by atom density.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting
