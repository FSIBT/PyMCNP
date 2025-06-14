import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Noslnp(_option.BlockOption):
    """
    Represents INP noslnp elements.

    Attributes:
        setting: Suppress writing SOLINP on/off.
    """

    _KEYWORD = 'noslnp'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Anoslnp( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Noslnp``.

        Parameters:
            setting: Suppress writing SOLINP on/off.

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
class NoslnpBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Noslnp``.

    Attributes:
        setting: Suppress writing SOLINP on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NoslnpBuilder`` into ``Noslnp``.

        Returns:
            ``Noslnp`` for ``NoslnpBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Noslnp(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Noslnp):
        """
        Unbuilds ``Noslnp`` into ``NoslnpBuilder``

        Returns:
            ``NoslnpBuilder`` for ``Noslnp``.
        """

        return NoslnpBuilder(
            setting=copy.deepcopy(ast.setting),
        )
