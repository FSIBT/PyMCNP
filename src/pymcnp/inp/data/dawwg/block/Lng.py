import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Lng(BlockOption):
    """
    Represents INP lng elements.

    Attributes:
        setting: Number of the last neutron group.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Alng( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Lng``.

        Parameters:
            setting: Number of the last neutron group.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class LngBuilder:
    """
    Builds ``Lng``.

    Attributes:
        setting: Number of the last neutron group.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``LngBuilder`` into ``Lng``.

        Returns:
            ``Lng`` for ``LngBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Lng(
            setting=setting,
        )
