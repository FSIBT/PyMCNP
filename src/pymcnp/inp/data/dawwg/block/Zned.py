import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Zned(BlockOption):
    """
    Represents INP zned elements.

    Attributes:
        setting: Edits by zone on/off.
    """

    _KEYWORD = 'zned'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Azned( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Zned``.

        Parameters:
            setting: Edits by zone on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class ZnedBuilder:
    """
    Builds ``Zned``.

    Attributes:
        setting: Edits by zone on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``ZnedBuilder`` into ``Zned``.

        Returns:
            ``Zned`` for ``ZnedBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Zned(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Zned):
        """
        Unbuilds ``Zned`` into ``ZnedBuilder``

        Returns:
            ``ZnedBuilder`` for ``Zned``.
        """

        return Zned(
            setting=copy.deepcopy(ast.setting),
        )
