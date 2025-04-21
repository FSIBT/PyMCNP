import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ith(BlockOption, keyword='ith'):
    """
    Represents INP ith elements.

    Attributes:
        setting: Direction/adjoint calculation control.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aith( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ith``.

        Parameters:
            setting: Direction/adjoint calculation control.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class IthBuilder:
    """
    Builds ``Ith``.

    Attributes:
        setting: Direction/adjoint calculation control.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IthBuilder`` into ``Ith``.

        Returns:
            ``Ith`` for ``IthBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ith(
            setting=setting,
        )
