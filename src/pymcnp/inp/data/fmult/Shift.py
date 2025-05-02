import re
import typing
import dataclasses


from ._option import FmultOption
from ....utils import types
from ....utils import errors


class Shift(FmultOption):
    """
    Represents INP shift elements.

    Attributes:
        setting: Shift method setting.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Ashift( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Shift``.

        Parameters:
            setting: Shift method setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class ShiftBuilder:
    """
    Builds ``Shift``.

    Attributes:
        setting: Shift method setting.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``ShiftBuilder`` into ``Shift``.

        Returns:
            ``Shift`` for ``ShiftBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Shift(
            setting=setting,
        )
