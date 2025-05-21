import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Asbott(BlockOption):
    """
    Represents INP asbott elements.

    Attributes:
        setting: Top-going flux at plane j.
    """

    _KEYWORD = 'asbott'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aasbott( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Asbott``.

        Parameters:
            setting: Top-going flux at plane j.

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
class AsbottBuilder:
    """
    Builds ``Asbott``.

    Attributes:
        setting: Top-going flux at plane j.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``AsbottBuilder`` into ``Asbott``.

        Returns:
            ``Asbott`` for ``AsbottBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Asbott(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Asbott):
        """
        Unbuilds ``Asbott`` into ``AsbottBuilder``

        Returns:
            ``AsbottBuilder`` for ``Asbott``.
        """

        return Asbott(
            setting=copy.deepcopy(ast.setting),
        )
