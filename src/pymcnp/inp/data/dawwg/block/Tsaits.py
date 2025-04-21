import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Tsaits(BlockOption, keyword='tsaits'):
    """
    Represents INP tsaits elements.

    Attributes:
        setting: Maximum TSA iteration count.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Atsaits( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Tsaits``.

        Parameters:
            setting: Maximum TSA iteration count.

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
class TsaitsBuilder:
    """
    Builds ``Tsaits``.

    Attributes:
        setting: Maximum TSA iteration count.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``TsaitsBuilder`` into ``Tsaits``.

        Returns:
            ``Tsaits`` for ``TsaitsBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Tsaits(
            setting=setting,
        )
