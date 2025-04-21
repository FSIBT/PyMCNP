import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Balp(BlockOption, keyword='balp'):
    """
    Represents INP balp elements.

    Attributes:
        setting: Print coarse-mesh balance tables on/off.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Abalp( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Balp``.

        Parameters:
            setting: Print coarse-mesh balance tables on/off.

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
class BalpBuilder:
    """
    Builds ``Balp``.

    Attributes:
        setting: Print coarse-mesh balance tables on/off.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``BalpBuilder`` into ``Balp``.

        Returns:
            ``Balp`` for ``BalpBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Balp(
            setting=setting,
        )
