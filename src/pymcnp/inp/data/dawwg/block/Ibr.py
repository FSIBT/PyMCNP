import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ibr(BlockOption):
    """
    Represents INP ibr elements.

    Attributes:
        setting: Right boudary condition.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aibr( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ibr``.

        Parameters:
            setting: Right boudary condition.

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
class IbrBuilder:
    """
    Builds ``Ibr``.

    Attributes:
        setting: Right boudary condition.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IbrBuilder`` into ``Ibr``.

        Returns:
            ``Ibr`` for ``IbrBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ibr(
            setting=setting,
        )
