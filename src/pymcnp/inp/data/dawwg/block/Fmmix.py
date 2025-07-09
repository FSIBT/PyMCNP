import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Fmmix(_option.BlockOption):
    """
    Represents INP fmmix elements.

    Attributes:
        setting: Read composition from LNK3DNT on/off.
    """

    _KEYWORD = 'fmmix'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Afmmix( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Fmmix``.

        Parameters:
            setting: Read composition from LNK3DNT on/off.

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
class FmmixBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Fmmix``.

    Attributes:
        setting: Read composition from LNK3DNT on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``FmmixBuilder`` into ``Fmmix``.

        Returns:
            ``Fmmix`` for ``FmmixBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Fmmix(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Fmmix):
        """
        Unbuilds ``Fmmix`` into ``FmmixBuilder``

        Returns:
            ``FmmixBuilder`` for ``Fmmix``.
        """

        return FmmixBuilder(
            setting=copy.deepcopy(ast.setting),
        )
