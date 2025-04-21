import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Tsaepsi(BlockOption, keyword='tsaepsi'):
    """
    Represents INP tsaepsi elements.

    Attributes:
        setting: Convergence criteria for TSA sweeps.
    """

    _ATTRS = {
        'setting': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Atsaepsi( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.RealOrJump):
        """
        Initializes ``Tsaepsi``.

        Parameters:
            setting: Convergence criteria for TSA sweeps.

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
class TsaepsiBuilder:
    """
    Builds ``Tsaepsi``.

    Attributes:
        setting: Convergence criteria for TSA sweeps.
    """

    setting: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``TsaepsiBuilder`` into ``Tsaepsi``.

        Returns:
            ``Tsaepsi`` for ``TsaepsiBuilder``.
        """

        if isinstance(self.setting, types.Real):
            setting = self.setting
        elif isinstance(self.setting, float) or isinstance(self.setting, int):
            setting = types.RealOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.RealOrJump.from_mcnp(self.setting)

        return Tsaepsi(
            setting=setting,
        )
