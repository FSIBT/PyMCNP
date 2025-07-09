import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Noasg(_option.BlockOption):
    """
    Represents INP noasg elements.

    Attributes:
        setting: Suppress writing ASGMAT on/off.
    """

    _KEYWORD = 'noasg'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Anoasg( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Noasg``.

        Parameters:
            setting: Suppress writing ASGMAT on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class NoasgBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Noasg``.

    Attributes:
        setting: Suppress writing ASGMAT on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NoasgBuilder`` into ``Noasg``.

        Returns:
            ``Noasg`` for ``NoasgBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Noasg(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Noasg):
        """
        Unbuilds ``Noasg`` into ``NoasgBuilder``

        Returns:
            ``NoasgBuilder`` for ``Noasg``.
        """

        return NoasgBuilder(
            setting=copy.deepcopy(ast.setting),
        )
