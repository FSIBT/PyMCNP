import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Oitm(_option.BlockOption):
    """
    Represents INP oitm elements.

    Attributes:
        setting: Maximum outer iteration count.
    """

    _KEYWORD = 'oitm'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aoitm( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Oitm``.

        Parameters:
            setting: Maximum outer iteration count.

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
class OitmBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Oitm``.

    Attributes:
        setting: Maximum outer iteration count.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``OitmBuilder`` into ``Oitm``.

        Returns:
            ``Oitm`` for ``OitmBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Oitm(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Oitm):
        """
        Unbuilds ``Oitm`` into ``OitmBuilder``

        Returns:
            ``OitmBuilder`` for ``Oitm``.
        """

        return OitmBuilder(
            setting=copy.deepcopy(ast.setting),
        )
