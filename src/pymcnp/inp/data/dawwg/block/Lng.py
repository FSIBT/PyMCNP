import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Lng(BlockOption):
    """
    Represents INP lng elements.

    Attributes:
        setting: Number of the last neutron group.
    """

    _KEYWORD = 'lng'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Alng( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Lng``.

        Parameters:
            setting: Number of the last neutron group.

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
class LngBuilder:
    """
    Builds ``Lng``.

    Attributes:
        setting: Number of the last neutron group.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``LngBuilder`` into ``Lng``.

        Returns:
            ``Lng`` for ``LngBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Lng(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Lng):
        """
        Unbuilds ``Lng`` into ``LngBuilder``

        Returns:
            ``LngBuilder`` for ``Lng``.
        """

        return Lng(
            setting=copy.deepcopy(ast.setting),
        )
