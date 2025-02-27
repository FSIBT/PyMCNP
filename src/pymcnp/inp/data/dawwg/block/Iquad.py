import re
import typing


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Iquad(BlockOption_, keyword='iquad'):
    """
    Represents INP iquad elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(r'iquad( \S+)')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Iquad``.

        Parameters:
            setting: Quadrature.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting
