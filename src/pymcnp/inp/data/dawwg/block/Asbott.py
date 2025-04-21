import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Asbott(BlockOption, keyword='asbott'):
    """
    Represents INP asbott elements.

    Attributes:
        setting: Top-going flux at plane j.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aasbott( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Asbott``.

        Parameters:
            setting: Top-going flux at plane j.

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
class AsbottBuilder:
    """
    Builds ``Asbott``.

    Attributes:
        setting: Top-going flux at plane j.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``AsbottBuilder`` into ``Asbott``.

        Returns:
            ``Asbott`` for ``AsbottBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Asbott(
            setting=setting,
        )
