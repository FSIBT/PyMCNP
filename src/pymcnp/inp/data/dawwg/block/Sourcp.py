import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Sourcp(BlockOption):
    """
    Represents INP sourcp elements.

    Attributes:
        setting: Source print flag.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Asourcp( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Sourcp``.

        Parameters:
            setting: Source print flag.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {0, 1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class SourcpBuilder:
    """
    Builds ``Sourcp``.

    Attributes:
        setting: Source print flag.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``SourcpBuilder`` into ``Sourcp``.

        Returns:
            ``Sourcp`` for ``SourcpBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Sourcp(
            setting=setting,
        )
