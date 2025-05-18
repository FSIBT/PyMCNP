import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ibback(BlockOption):
    """
    Represents INP ibback elements.

    Attributes:
        setting: Back boudary condition.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aibback( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ibback``.

        Parameters:
            setting: Back boudary condition.

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
class IbbackBuilder:
    """
    Builds ``Ibback``.

    Attributes:
        setting: Back boudary condition.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IbbackBuilder`` into ``Ibback``.

        Returns:
            ``Ibback`` for ``IbbackBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ibback(
            setting=setting,
        )
