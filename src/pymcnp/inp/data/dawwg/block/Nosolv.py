import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Nosolv(_option.BlockOption):
    """
    Represents INP nosolv elements.

    Attributes:
        setting: Suppress solver module on/off.
    """

    _KEYWORD = 'nosolv'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Anosolv( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Nosolv``.

        Parameters:
            setting: Suppress solver module on/off.

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
class NosolvBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Nosolv``.

    Attributes:
        setting: Suppress solver module on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NosolvBuilder`` into ``Nosolv``.

        Returns:
            ``Nosolv`` for ``NosolvBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Nosolv(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Nosolv):
        """
        Unbuilds ``Nosolv`` into ``NosolvBuilder``

        Returns:
            ``NosolvBuilder`` for ``Nosolv``.
        """

        return NosolvBuilder(
            setting=copy.deepcopy(ast.setting),
        )
