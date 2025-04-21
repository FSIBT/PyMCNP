import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Nosolv(BlockOption, keyword='nosolv'):
    """
    Represents INP nosolv elements.

    Attributes:
        setting: Suppress solver module on/off.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Anosolv( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Nosolv``.

        Parameters:
            setting: Suppress solver module on/off.

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
class NosolvBuilder:
    """
    Builds ``Nosolv``.

    Attributes:
        setting: Suppress solver module on/off.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``NosolvBuilder`` into ``Nosolv``.

        Returns:
            ``Nosolv`` for ``NosolvBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Nosolv(
            setting=setting,
        )
