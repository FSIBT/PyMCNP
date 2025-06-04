import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Nomix(BlockOption):
    """
    Represents INP nomix elements.

    Attributes:
        setting: Suppress writing mixing on/off.
    """

    _KEYWORD = 'nomix'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Anomix( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Nomix``.

        Parameters:
            setting: Suppress writing mixing on/off.

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
class NomixBuilder:
    """
    Builds ``Nomix``.

    Attributes:
        setting: Suppress writing mixing on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NomixBuilder`` into ``Nomix``.

        Returns:
            ``Nomix`` for ``NomixBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Nomix(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Nomix):
        """
        Unbuilds ``Nomix`` into ``NomixBuilder``

        Returns:
            ``NomixBuilder`` for ``Nomix``.
        """

        return Nomix(
            setting=copy.deepcopy(ast.setting),
        )
