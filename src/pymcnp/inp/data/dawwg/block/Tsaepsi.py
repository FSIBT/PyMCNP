import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Tsaepsi(BlockOption):
    """
    Represents INP tsaepsi elements.

    Attributes:
        setting: Convergence criteria for TSA sweeps.
    """

    _KEYWORD = 'tsaepsi'

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(rf'\Atsaepsi( {types.Real._REGEX.pattern})\Z')

    def __init__(self, setting: types.Real):
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

        self.setting: typing.Final[types.Real] = setting


@dataclasses.dataclass
class TsaepsiBuilder:
    """
    Builds ``Tsaepsi``.

    Attributes:
        setting: Convergence criteria for TSA sweeps.
    """

    setting: str | float | types.Real

    def build(self):
        """
        Builds ``TsaepsiBuilder`` into ``Tsaepsi``.

        Returns:
            ``Tsaepsi`` for ``TsaepsiBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Real):
            setting = self.setting
        elif isinstance(self.setting, float) or isinstance(self.setting, int):
            setting = types.Real(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Real.from_mcnp(self.setting)

        return Tsaepsi(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Tsaepsi):
        """
        Unbuilds ``Tsaepsi`` into ``TsaepsiBuilder``

        Returns:
            ``TsaepsiBuilder`` for ``Tsaepsi``.
        """

        return Tsaepsi(
            setting=copy.deepcopy(ast.setting),
        )
