import re
import typing
import dataclasses


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Balxs(BlockOption_, keyword='balxs'):
    """
    Represents INP balxs elements.

    Attributes:
        setting: Cross-section balance control.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Abalxs( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Balxs``.

        Parameters:
            setting: Cross-section balance control.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {-1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class BalxsBuilder:
    """
    Builds ``Balxs``.

    Attributes:
        setting: Cross-section balance control.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``BalxsBuilder`` into ``Balxs``.

        Returns:
            ``Balxs`` for ``BalxsBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Balxs(
            setting=setting,
        )
