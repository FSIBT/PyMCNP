import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Isct(BlockOption):
    """
    Represents INP isct elements.

    Attributes:
        setting: Legendre order.
    """

    _KEYWORD = 'isct'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aisct( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Isct``.

        Parameters:
            setting: Legendre order.

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
class IsctBuilder:
    """
    Builds ``Isct``.

    Attributes:
        setting: Legendre order.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``IsctBuilder`` into ``Isct``.

        Returns:
            ``Isct`` for ``IsctBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Isct(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Isct):
        """
        Unbuilds ``Isct`` into ``IsctBuilder``

        Returns:
            ``IsctBuilder`` for ``Isct``.
        """

        return Isct(
            setting=copy.deepcopy(ast.setting),
        )
