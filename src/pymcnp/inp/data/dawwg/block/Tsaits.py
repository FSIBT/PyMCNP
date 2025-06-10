import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Tsaits(_option.BlockOption):
    """
    Represents INP tsaits elements.

    Attributes:
        setting: Maximum TSA iteration count.
    """

    _KEYWORD = 'tsaits'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Atsaits( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Tsaits``.

        Parameters:
            setting: Maximum TSA iteration count.

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
class TsaitsBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Tsaits``.

    Attributes:
        setting: Maximum TSA iteration count.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``TsaitsBuilder`` into ``Tsaits``.

        Returns:
            ``Tsaits`` for ``TsaitsBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Tsaits(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Tsaits):
        """
        Unbuilds ``Tsaits`` into ``TsaitsBuilder``

        Returns:
            ``TsaitsBuilder`` for ``Tsaits``.
        """

        return TsaitsBuilder(
            setting=copy.deepcopy(ast.setting),
        )
