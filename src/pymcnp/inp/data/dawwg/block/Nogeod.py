import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Nogeod(_option.BlockOption):
    """
    Represents INP nogeod elements.

    Attributes:
        setting: Suppress writing GEODST on/off.
    """

    _KEYWORD = 'nogeod'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Anogeod( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Nogeod``.

        Parameters:
            setting: Suppress writing GEODST on/off.

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
class NogeodBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Nogeod``.

    Attributes:
        setting: Suppress writing GEODST on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NogeodBuilder`` into ``Nogeod``.

        Returns:
            ``Nogeod`` for ``NogeodBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Nogeod(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Nogeod):
        """
        Unbuilds ``Nogeod`` into ``NogeodBuilder``

        Returns:
            ``NogeodBuilder`` for ``Nogeod``.
        """

        return NogeodBuilder(
            setting=copy.deepcopy(ast.setting),
        )
