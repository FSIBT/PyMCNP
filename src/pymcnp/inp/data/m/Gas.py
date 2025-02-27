import re
import typing


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Gas(MOption_, keyword='gas'):
    """
    Represents INP gas elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'gas( \S+)')

    def __init__(self, setting: types.String):
        """
        Initializes ``Gas``.

        Parameters:
            setting: Flag for density-effect correction to electron stopping power.

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
