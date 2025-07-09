import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Pted(_option.BlockOption):
    """
    Represents INP pted elements.

    Attributes:
        setting: Edits by fine mesh on/off.
    """

    _KEYWORD = 'pted'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Apted( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Pted``.

        Parameters:
            setting: Edits by fine mesh on/off.

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
class PtedBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Pted``.

    Attributes:
        setting: Edits by fine mesh on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``PtedBuilder`` into ``Pted``.

        Returns:
            ``Pted`` for ``PtedBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Pted(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Pted):
        """
        Unbuilds ``Pted`` into ``PtedBuilder``

        Returns:
            ``PtedBuilder`` for ``Pted``.
        """

        return PtedBuilder(
            setting=copy.deepcopy(ast.setting),
        )
