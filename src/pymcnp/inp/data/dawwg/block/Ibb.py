import re
import typing
import dataclasses


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Ibb(BlockOption_, keyword='ibb'):
    """
    Represents INP ibb elements.

    Attributes:
        setting: Bottom  boudary condition.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aibb( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ibb``.

        Parameters:
            setting: Bottom  boudary condition.

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
class IbbBuilder:
    """
    Builds ``Ibb``.

    Attributes:
        setting: Bottom  boudary condition.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IbbBuilder`` into ``Ibb``.

        Returns:
            ``Ibb`` for ``IbbBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ibb(
            setting=setting,
        )
