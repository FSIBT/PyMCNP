import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Ntichi(BlockOption_, keyword='ntichi'):
    """
    Represents INP ntichi elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Antichi( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ntichi``.

        Parameters:
            setting: MENDF fission fraction.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting
