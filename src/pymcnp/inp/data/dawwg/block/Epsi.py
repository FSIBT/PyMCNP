import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Epsi(BlockOption, keyword='epsi'):
    """
    Represents INP epsi elements.

    Attributes:
        setting: Convergence precision.
    """

    _ATTRS = {
        'setting': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Aepsi( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.RealOrJump):
        """
        Initializes ``Epsi``.

        Parameters:
            setting: Convergence precision.

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
class EpsiBuilder:
    """
    Builds ``Epsi``.

    Attributes:
        setting: Convergence precision.
    """

    setting: str | float | types.RealOrJump

    def build(self):
        """
        Builds ``EpsiBuilder`` into ``Epsi``.

        Returns:
            ``Epsi`` for ``EpsiBuilder``.
        """

        if isinstance(self.setting, types.Real):
            setting = self.setting
        elif isinstance(self.setting, float) or isinstance(self.setting, int):
            setting = types.RealOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.RealOrJump.from_mcnp(self.setting)

        return Epsi(
            setting=setting,
        )
