import re
import typing
import dataclasses


from .option_ import RandOption_
from ....utils import types
from ....utils import errors


class Gen(RandOption_, keyword='gen'):
    """
    Represents INP gen elements.

    Attributes:
        setting: Type of pseudorandom number generator.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Agen( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Gen``.

        Parameters:
            setting: Type of pseudorandom number generator.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class GenBuilder:
    """
    Builds ``Gen``.

    Attributes:
        setting: Type of pseudorandom number generator.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``GenBuilder`` into ``Gen``.

        Returns:
            ``Gen`` for ``GenBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Gen(
            setting=setting,
        )
