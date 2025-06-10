import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Raflux(_option.BlockOption):
    """
    Represents INP raflux elements.

    Attributes:
        setting: Prepare angular flux file on/off.
    """

    _KEYWORD = 'raflux'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Araflux( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Raflux``.

        Parameters:
            setting: Prepare angular flux file on/off.

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
class RafluxBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Raflux``.

    Attributes:
        setting: Prepare angular flux file on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``RafluxBuilder`` into ``Raflux``.

        Returns:
            ``Raflux`` for ``RafluxBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Raflux(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Raflux):
        """
        Unbuilds ``Raflux`` into ``RafluxBuilder``

        Returns:
            ``RafluxBuilder`` for ``Raflux``.
        """

        return RafluxBuilder(
            setting=copy.deepcopy(ast.setting),
        )
