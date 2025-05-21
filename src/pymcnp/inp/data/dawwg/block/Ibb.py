import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ibb(BlockOption):
    """
    Represents INP ibb elements.

    Attributes:
        setting: Bottom  boudary condition.
    """

    _KEYWORD = 'ibb'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aibb( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ibb``.

        Parameters:
            setting: Bottom  boudary condition.

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
class IbbBuilder:
    """
    Builds ``Ibb``.

    Attributes:
        setting: Bottom  boudary condition.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``IbbBuilder`` into ``Ibb``.

        Returns:
            ``Ibb`` for ``IbbBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Ibb(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Ibb):
        """
        Unbuilds ``Ibb`` into ``IbbBuilder``

        Returns:
            ``IbbBuilder`` for ``Ibb``.
        """

        return Ibb(
            setting=copy.deepcopy(ast.setting),
        )
