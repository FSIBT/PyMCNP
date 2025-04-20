import re
import typing
import dataclasses


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Ibfrnt(BlockOption_, keyword='ibfrnt'):
    """
    Represents INP ibfrnt elements.

    Attributes:
        setting: Front boudary condition.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aibfrnt( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ibfrnt``.

        Parameters:
            setting: Front boudary condition.

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
class IbfrntBuilder:
    """
    Builds ``Ibfrnt``.

    Attributes:
        setting: Front boudary condition.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IbfrntBuilder`` into ``Ibfrnt``.

        Returns:
            ``Ibfrnt`` for ``IbfrntBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ibfrnt(
            setting=setting,
        )
