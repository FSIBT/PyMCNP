import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Avatar(BlockOption, keyword='avatar'):
    """
    Represents INP avatar elements.

    Attributes:
        setting: Prepare special XMFLUXA file on/off.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aavatar( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Avatar``.

        Parameters:
            setting: Prepare special XMFLUXA file on/off.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class AvatarBuilder:
    """
    Builds ``Avatar``.

    Attributes:
        setting: Prepare special XMFLUXA file on/off.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``AvatarBuilder`` into ``Avatar``.

        Returns:
            ``Avatar`` for ``AvatarBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Avatar(
            setting=setting,
        )
