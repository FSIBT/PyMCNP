import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Isn(_option.BlockOption):
    """
    Represents INP isn elements.

    Attributes:
        setting: Sn order.
    """

    _KEYWORD = 'isn'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aisn( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Isn``.

        Parameters:
            setting: Sn order.

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
class IsnBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Isn``.

    Attributes:
        setting: Sn order.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``IsnBuilder`` into ``Isn``.

        Returns:
            ``Isn`` for ``IsnBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Isn(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Isn):
        """
        Unbuilds ``Isn`` into ``IsnBuilder``

        Returns:
            ``IsnBuilder`` for ``Isn``.
        """

        return IsnBuilder(
            setting=copy.deepcopy(ast.setting),
        )
