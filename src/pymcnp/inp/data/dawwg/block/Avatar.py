import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Avatar(_option.BlockOption):
    """
    Represents INP avatar elements.

    Attributes:
        setting: Prepare special XMFLUXA file on/off.
    """

    _KEYWORD = 'avatar'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aavatar( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Avatar``.

        Parameters:
            setting: Prepare special XMFLUXA file on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class AvatarBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Avatar``.

    Attributes:
        setting: Prepare special XMFLUXA file on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``AvatarBuilder`` into ``Avatar``.

        Returns:
            ``Avatar`` for ``AvatarBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Avatar(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Avatar):
        """
        Unbuilds ``Avatar`` into ``AvatarBuilder``

        Returns:
            ``AvatarBuilder`` for ``Avatar``.
        """

        return AvatarBuilder(
            setting=copy.deepcopy(ast.setting),
        )
