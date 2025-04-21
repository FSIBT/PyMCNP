import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ibl(BlockOption, keyword='ibl'):
    """
    Represents INP ibl elements.

    Attributes:
        setting: Left boundary condition.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aibl( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ibl``.

        Parameters:
            setting: Left boundary condition.

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
class IblBuilder:
    """
    Builds ``Ibl``.

    Attributes:
        setting: Left boundary condition.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IblBuilder`` into ``Ibl``.

        Returns:
            ``Ibl`` for ``IblBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ibl(
            setting=setting,
        )
