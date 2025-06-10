import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Shift(_option.FmultOption):
    """
    Represents INP shift elements.

    Attributes:
        setting: Shift method setting.
    """

    _KEYWORD = 'shift'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Ashift( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Shift``.

        Parameters:
            setting: Shift method setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class ShiftBuilder(_option.FmultOptionBuilder):
    """
    Builds ``Shift``.

    Attributes:
        setting: Shift method setting.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``ShiftBuilder`` into ``Shift``.

        Returns:
            ``Shift`` for ``ShiftBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Shift(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Shift):
        """
        Unbuilds ``Shift`` into ``ShiftBuilder``

        Returns:
            ``ShiftBuilder`` for ``Shift``.
        """

        return ShiftBuilder(
            setting=copy.deepcopy(ast.setting),
        )
