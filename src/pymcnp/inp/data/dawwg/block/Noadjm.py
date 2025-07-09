import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Noadjm(_option.BlockOption):
    """
    Represents INP noadjm elements.

    Attributes:
        setting: Suppress writing ADJMAC on/off.
    """

    _KEYWORD = 'noadjm'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Anoadjm( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Noadjm``.

        Parameters:
            setting: Suppress writing ADJMAC on/off.

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
class NoadjmBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Noadjm``.

    Attributes:
        setting: Suppress writing ADJMAC on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NoadjmBuilder`` into ``Noadjm``.

        Returns:
            ``Noadjm`` for ``NoadjmBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Noadjm(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Noadjm):
        """
        Unbuilds ``Noadjm`` into ``NoadjmBuilder``

        Returns:
            ``NoadjmBuilder`` for ``Noadjm``.
        """

        return NoadjmBuilder(
            setting=copy.deepcopy(ast.setting),
        )
