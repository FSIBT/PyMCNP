import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Noedit(BlockOption):
    """
    Represents INP noedit elements.

    Attributes:
        setting: Suppress edit module on/off.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Anoedit( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Noedit``.

        Parameters:
            setting: Suppress edit module on/off.

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

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class NoeditBuilder:
    """
    Builds ``Noedit``.

    Attributes:
        setting: Suppress edit module on/off.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``NoeditBuilder`` into ``Noedit``.

        Returns:
            ``Noedit`` for ``NoeditBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Noedit(
            setting=setting,
        )
