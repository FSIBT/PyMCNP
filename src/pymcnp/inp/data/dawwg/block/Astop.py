import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Astop(BlockOption):
    """
    Represents INP astop elements.

    Attributes:
        setting: Bottom-going flux at plane j.
    """

    _KEYWORD = 'astop'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aastop( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Astop``.

        Parameters:
            setting: Bottom-going flux at plane j.

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
class AstopBuilder:
    """
    Builds ``Astop``.

    Attributes:
        setting: Bottom-going flux at plane j.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``AstopBuilder`` into ``Astop``.

        Returns:
            ``Astop`` for ``AstopBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Astop(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Astop):
        """
        Unbuilds ``Astop`` into ``AstopBuilder``

        Returns:
            ``AstopBuilder`` for ``Astop``.
        """

        return Astop(
            setting=copy.deepcopy(ast.setting),
        )
