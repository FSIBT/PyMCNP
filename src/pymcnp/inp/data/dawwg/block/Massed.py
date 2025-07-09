import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Massed(_option.BlockOption):
    """
    Represents INP massed elements.

    Attributes:
        setting: Mass edits on/off.
    """

    _KEYWORD = 'massed'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Amassed( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Massed``.

        Parameters:
            setting: Mass edits on/off.

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
class MassedBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Massed``.

    Attributes:
        setting: Mass edits on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``MassedBuilder`` into ``Massed``.

        Returns:
            ``Massed`` for ``MassedBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Massed(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Massed):
        """
        Unbuilds ``Massed`` into ``MassedBuilder``

        Returns:
            ``MassedBuilder`` for ``Massed``.
        """

        return MassedBuilder(
            setting=copy.deepcopy(ast.setting),
        )
