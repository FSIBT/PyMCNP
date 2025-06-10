import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Tsaepsi(_option.BlockOption):
    """
    Represents INP tsaepsi elements.

    Attributes:
        setting: Convergence criteria for TSA sweeps.
    """

    _KEYWORD = 'tsaepsi'

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(rf'\Atsaepsi( {types.Real._REGEX.pattern[2:-2]})\Z')

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
class TsaepsiBuilder(_option.BlockOptionBuilder):
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

        return TsaepsiBuilder(
            setting=copy.deepcopy(ast.setting),
        )
