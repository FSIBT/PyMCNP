import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Mt(BlockOption):
    """
    Represents INP mt elements.

    Attributes:
        setting: Number of materials.
    """

    _KEYWORD = 'mt'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Amt( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Mt``.

        Parameters:
            setting: Number of materials.

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
class MtBuilder:
    """
    Builds ``Mt``.

    Attributes:
        setting: Number of materials.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``MtBuilder`` into ``Mt``.

        Returns:
            ``Mt`` for ``MtBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Mt(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Mt):
        """
        Unbuilds ``Mt`` into ``MtBuilder``

        Returns:
            ``MtBuilder`` for ``Mt``.
        """

        return Mt(
            setting=copy.deepcopy(ast.setting),
        )
