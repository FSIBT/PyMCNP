import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Norm(BlockOption):
    """
    Represents INP norm elements.

    Attributes:
        setting: Norm.
    """

    _ATTRS = {
        'setting': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Anorm( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.RealOrJump):
        """
        Initializes ``Norm``.

        Parameters:
            setting: Norm.

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

        self.setting: typing.Final[types.RealOrJump] = setting


@dataclasses.dataclass
class NormBuilder:
    """
    Builds ``Norm``.

    Attributes:
        setting: Norm.
    """

    setting: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``NormBuilder`` into ``Norm``.

        Returns:
            ``Norm`` for ``NormBuilder``.
        """

        if isinstance(self.setting, types.Real):
            setting = self.setting
        elif isinstance(self.setting, float) or isinstance(self.setting, int):
            setting = types.RealOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.RealOrJump.from_mcnp(self.setting)

        return Norm(
            setting=setting,
        )
