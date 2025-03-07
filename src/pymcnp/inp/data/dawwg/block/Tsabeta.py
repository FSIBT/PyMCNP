import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Tsabeta(BlockOption_, keyword='tsabeta'):
    """
    Represents INP tsabeta elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(rf'tsabeta( {types.Real._REGEX.pattern})')

    def __init__(self, setting: types.Real):
        """
        Initializes ``Tsabeta``.

        Parameters:
            setting: Scattering cross-section reduction for TSA.

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

        self.setting: typing.Final[types.Real] = setting
