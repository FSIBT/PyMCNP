import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Isct(BlockOption):
    """
    Represents INP isct elements.

    Attributes:
        setting: Legendre order.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aisct( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Isct``.

        Parameters:
            setting: Legendre order.

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
class IsctBuilder:
    """
    Builds ``Isct``.

    Attributes:
        setting: Legendre order.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IsctBuilder`` into ``Isct``.

        Returns:
            ``Isct`` for ``IsctBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Isct(
            setting=setting,
        )
