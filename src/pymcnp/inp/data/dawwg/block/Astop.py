import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Astop(BlockOption, keyword='astop'):
    """
    Represents INP astop elements.

    Attributes:
        setting: Bottom-going flux at plane j.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aastop( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Astop``.

        Parameters:
            setting: Bottom-going flux at plane j.

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
class AstopBuilder:
    """
    Builds ``Astop``.

    Attributes:
        setting: Bottom-going flux at plane j.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``AstopBuilder`` into ``Astop``.

        Returns:
            ``Astop`` for ``AstopBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Astop(
            setting=setting,
        )
