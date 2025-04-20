import re
import typing
import dataclasses


from .option_ import PertOption_
from ....utils import types
from ....utils import errors


class Method(PertOption_, keyword='method'):
    """
    Represents INP method elements.

    Attributes:
        setting: Printing and specifies setting.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Amethod( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Method``.

        Parameters:
            setting: Printing and specifies setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {+1, -1, +2, -2, +3, -3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class MethodBuilder:
    """
    Builds ``Method``.

    Attributes:
        setting: Printing and specifies setting.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``MethodBuilder`` into ``Method``.

        Returns:
            ``Method`` for ``MethodBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Method(
            setting=setting,
        )
