import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Niso(BlockOption):
    """
    Represents INP niso elements.

    Attributes:
        setting: Number of isotopes.
    """

    _KEYWORD = 'niso'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aniso( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Niso``.

        Parameters:
            setting: Number of isotopes.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class NisoBuilder:
    """
    Builds ``Niso``.

    Attributes:
        setting: Number of isotopes.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NisoBuilder`` into ``Niso``.

        Returns:
            ``Niso`` for ``NisoBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Niso(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Niso):
        """
        Unbuilds ``Niso`` into ``NisoBuilder``

        Returns:
            ``NisoBuilder`` for ``Niso``.
        """

        return Niso(
            setting=copy.deepcopy(ast.setting),
        )
