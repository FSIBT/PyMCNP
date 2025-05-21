import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Tsabeta(BlockOption):
    """
    Represents INP tsabeta elements.

    Attributes:
        setting: Scattering cross-section reduction for TSA.
    """

    _KEYWORD = 'tsabeta'

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(rf'\Atsabeta( {types.Real._REGEX.pattern})\Z')

    def __init__(self, setting: types.Real):
        """
        Initializes ``Tsabeta``.

        Parameters:
            setting: Scattering cross-section reduction for TSA.

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
class TsabetaBuilder:
    """
    Builds ``Tsabeta``.

    Attributes:
        setting: Scattering cross-section reduction for TSA.
    """

    setting: str | float | types.Real

    def build(self):
        """
        Builds ``TsabetaBuilder`` into ``Tsabeta``.

        Returns:
            ``Tsabeta`` for ``TsabetaBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Real):
            setting = self.setting
        elif isinstance(self.setting, float) or isinstance(self.setting, int):
            setting = types.Real(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Real.from_mcnp(self.setting)

        return Tsabeta(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Tsabeta):
        """
        Unbuilds ``Tsabeta`` into ``TsabetaBuilder``

        Returns:
            ``TsabetaBuilder`` for ``Tsabeta``.
        """

        return Tsabeta(
            setting=copy.deepcopy(ast.setting),
        )
