import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Rmflux(_option.BlockOption):
    """
    Represents INP rmflux elements.

    Attributes:
        setting: Prepare flux moments file on/off.
    """

    _KEYWORD = 'rmflux'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Armflux( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Rmflux``.

        Parameters:
            setting: Prepare flux moments file on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class RmfluxBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Rmflux``.

    Attributes:
        setting: Prepare flux moments file on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``RmfluxBuilder`` into ``Rmflux``.

        Returns:
            ``Rmflux`` for ``RmfluxBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Rmflux(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Rmflux):
        """
        Unbuilds ``Rmflux`` into ``RmfluxBuilder``

        Returns:
            ``RmfluxBuilder`` for ``Rmflux``.
        """

        return RmfluxBuilder(
            setting=copy.deepcopy(ast.setting),
        )
