import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Tsasn(_option.BlockOption):
    """
    Represents INP tsasn elements.

    Attributes:
        setting: Sn order for lower order TSA sweeps.
    """

    _KEYWORD = 'tsasn'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Atsasn( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Tsasn``.

        Parameters:
            setting: Sn order for lower order TSA sweeps.

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

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class TsasnBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Tsasn``.

    Attributes:
        setting: Sn order for lower order TSA sweeps.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``TsasnBuilder`` into ``Tsasn``.

        Returns:
            ``Tsasn`` for ``TsasnBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Tsasn(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Tsasn):
        """
        Unbuilds ``Tsasn`` into ``TsasnBuilder``

        Returns:
            ``TsasnBuilder`` for ``Tsasn``.
        """

        return TsasnBuilder(
            setting=copy.deepcopy(ast.setting),
        )
