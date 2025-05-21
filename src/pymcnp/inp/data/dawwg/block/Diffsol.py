import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Diffsol(BlockOption):
    """
    Represents INP diffsol elements.

    Attributes:
        setting: Diffusion operator solver.
    """

    _KEYWORD = 'diffsol'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Adiffsol( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Diffsol``.

        Parameters:
            setting: Diffusion operator solver.

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

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class DiffsolBuilder:
    """
    Builds ``Diffsol``.

    Attributes:
        setting: Diffusion operator solver.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``DiffsolBuilder`` into ``Diffsol``.

        Returns:
            ``Diffsol`` for ``DiffsolBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Diffsol(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Diffsol):
        """
        Unbuilds ``Diffsol`` into ``DiffsolBuilder``

        Returns:
            ``DiffsolBuilder`` for ``Diffsol``.
        """

        return Diffsol(
            setting=copy.deepcopy(ast.setting),
        )
