import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ibt(BlockOption, keyword='ibt'):
    """
    Represents INP ibt elements.

    Attributes:
        setting: Top boudary condition.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aibt( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ibt``.

        Parameters:
            setting: Top boudary condition.

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
class IbtBuilder:
    """
    Builds ``Ibt``.

    Attributes:
        setting: Top boudary condition.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IbtBuilder`` into ``Ibt``.

        Returns:
            ``Ibt`` for ``IbtBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ibt(
            setting=setting,
        )
