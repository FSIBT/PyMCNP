import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Epsi(BlockOption):
    """
    Represents INP epsi elements.

    Attributes:
        setting: Convergence precision.
    """

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(rf'\Aepsi( {types.Real._REGEX.pattern})\Z')

    def __init__(self, setting: types.Real):
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

        self.setting: typing.Final[types.Real] = setting


@dataclasses.dataclass
class EpsiBuilder:
    """
    Builds ``Epsi``.

    Attributes:
        setting: Convergence precision.
    """

    setting: str | float | types.Real

    def build(self):
        """
        Builds ``EpsiBuilder`` into ``Epsi``.

        Returns:
            ``Epsi`` for ``EpsiBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Real):
            setting = self.setting
        elif isinstance(self.setting, float) or isinstance(self.setting, int):
            setting = types.Real(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Real.from_mcnp(self.setting)

        return Epsi(
            setting=setting,
        )
