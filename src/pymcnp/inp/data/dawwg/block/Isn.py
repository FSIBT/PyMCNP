import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Isn(BlockOption, keyword='isn'):
    """
    Represents INP isn elements.

    Attributes:
        setting: Sn order.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aisn( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Isn``.

        Parameters:
            setting: Sn order.

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

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class IsnBuilder:
    """
    Builds ``Isn``.

    Attributes:
        setting: Sn order.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IsnBuilder`` into ``Isn``.

        Returns:
            ``Isn`` for ``IsnBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Isn(
            setting=setting,
        )
