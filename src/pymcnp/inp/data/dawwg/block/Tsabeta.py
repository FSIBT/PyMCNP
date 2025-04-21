import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Tsabeta(BlockOption, keyword='tsabeta'):
    """
    Represents INP tsabeta elements.

    Attributes:
        setting: Scattering cross-section reduction for TSA.
    """

    _ATTRS = {
        'setting': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Atsabeta( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.RealOrJump):
        """
        Initializes ``Tsabeta``.

        Parameters:
            setting: Scattering cross-section reduction for TSA.

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
class TsabetaBuilder:
    """
    Builds ``Tsabeta``.

    Attributes:
        setting: Scattering cross-section reduction for TSA.
    """

    setting: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``TsabetaBuilder`` into ``Tsabeta``.

        Returns:
            ``Tsabeta`` for ``TsabetaBuilder``.
        """

        if isinstance(self.setting, types.Real):
            setting = self.setting
        elif isinstance(self.setting, float) or isinstance(self.setting, int):
            setting = types.RealOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.RealOrJump.from_mcnp(self.setting)

        return Tsabeta(
            setting=setting,
        )
