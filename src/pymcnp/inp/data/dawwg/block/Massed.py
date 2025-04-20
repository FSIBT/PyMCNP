import re
import typing
import dataclasses


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Massed(BlockOption_, keyword='massed'):
    """
    Represents INP massed elements.

    Attributes:
        setting: Mass edits on/off.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Amassed( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Massed``.

        Parameters:
            setting: Mass edits on/off.

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
class MassedBuilder:
    """
    Builds ``Massed``.

    Attributes:
        setting: Mass edits on/off.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``MassedBuilder`` into ``Massed``.

        Returns:
            ``Massed`` for ``MassedBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Massed(
            setting=setting,
        )
