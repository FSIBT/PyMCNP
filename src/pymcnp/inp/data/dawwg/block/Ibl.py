import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Ibl(_option.BlockOption):
    """
    Represents INP ibl elements.

    Attributes:
        setting: Left boundary condition.
    """

    _KEYWORD = 'ibl'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aibl( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ibl``.

        Parameters:
            setting: Left boundary condition.

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
class IblBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Ibl``.

    Attributes:
        setting: Left boundary condition.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``IblBuilder`` into ``Ibl``.

        Returns:
            ``Ibl`` for ``IblBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Ibl(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Ibl):
        """
        Unbuilds ``Ibl`` into ``IblBuilder``

        Returns:
            ``IblBuilder`` for ``Ibl``.
        """

        return IblBuilder(
            setting=copy.deepcopy(ast.setting),
        )
