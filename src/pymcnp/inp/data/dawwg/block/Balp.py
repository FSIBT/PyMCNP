import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Balp(_option.BlockOption):
    """
    Represents INP balp elements.

    Attributes:
        setting: Print coarse-mesh balance tables on/off.
    """

    _KEYWORD = 'balp'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Abalp( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Balp``.

        Parameters:
            setting: Print coarse-mesh balance tables on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class BalpBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Balp``.

    Attributes:
        setting: Print coarse-mesh balance tables on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``BalpBuilder`` into ``Balp``.

        Returns:
            ``Balp`` for ``BalpBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Balp(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Balp):
        """
        Unbuilds ``Balp`` into ``BalpBuilder``

        Returns:
            ``BalpBuilder`` for ``Balp``.
        """

        return BalpBuilder(
            setting=copy.deepcopy(ast.setting),
        )
