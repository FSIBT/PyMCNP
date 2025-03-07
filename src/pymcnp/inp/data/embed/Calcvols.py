import re
import typing


from .option_ import EmbedOption_
from ....utils import types
from ....utils import errors


class Calcvols(EmbedOption_, keyword='calcvols'):
    """
    Represents INP calcvols elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'calcvols( {types.String._REGEX.pattern})')

    def __init__(self, setting: types.String):
        """
        Initializes ``Calcvols``.

        Parameters:
            setting: Yes/no calculate the inferred geometry cell information.

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
