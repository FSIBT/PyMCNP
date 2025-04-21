import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Fluxone(BlockOption, keyword='fluxone'):
    """
    Represents INP fluxone elements.

    Attributes:
        setting: Flux override on/off.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Afluxone( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Fluxone``.

        Parameters:
            setting: Flux override on/off.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class FluxoneBuilder:
    """
    Builds ``Fluxone``.

    Attributes:
        setting: Flux override on/off.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``FluxoneBuilder`` into ``Fluxone``.

        Returns:
            ``Fluxone`` for ``FluxoneBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Fluxone(
            setting=setting,
        )
