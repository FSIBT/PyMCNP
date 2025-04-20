import re
import typing
import dataclasses


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Cond(MOption_, keyword='cond'):
    """
    Represents INP cond elements.

    Attributes:
        setting: Conduction state for EL03 electron-transport evaluation.
    """

    _ATTRS = {
        'setting': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Acond( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.RealOrJump):
        """
        Initializes ``Cond``.

        Parameters:
            setting: Conduction state for EL03 electron-transport evaluation.

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

        self.setting: typing.Final[types.RealOrJump] = setting


@dataclasses.dataclass
class CondBuilder:
    """
    Builds ``Cond``.

    Attributes:
        setting: Conduction state for EL03 electron-transport evaluation.
    """

    setting: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``CondBuilder`` into ``Cond``.

        Returns:
            ``Cond`` for ``CondBuilder``.
        """

        if isinstance(self.setting, types.Real):
            setting = self.setting
        elif isinstance(self.setting, float) or isinstance(self.setting, int):
            setting = types.RealOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.RealOrJump.from_mcnp(self.setting)

        return Cond(
            setting=setting,
        )
