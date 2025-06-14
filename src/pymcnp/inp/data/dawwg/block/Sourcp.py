import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Sourcp(_option.BlockOption):
    """
    Represents INP sourcp elements.

    Attributes:
        setting: Source print flag.
    """

    _KEYWORD = 'sourcp'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Asourcp( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Sourcp``.

        Parameters:
            setting: Source print flag.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class SourcpBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Sourcp``.

    Attributes:
        setting: Source print flag.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``SourcpBuilder`` into ``Sourcp``.

        Returns:
            ``Sourcp`` for ``SourcpBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Sourcp(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Sourcp):
        """
        Unbuilds ``Sourcp`` into ``SourcpBuilder``

        Returns:
            ``SourcpBuilder`` for ``Sourcp``.
        """

        return SourcpBuilder(
            setting=copy.deepcopy(ast.setting),
        )
