import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Asrite(BlockOption):
    """
    Represents INP asrite elements.

    Attributes:
        setting: Left-going flux at plane i.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aasrite( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Asrite``.

        Parameters:
            setting: Left-going flux at plane i.

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

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class AsriteBuilder:
    """
    Builds ``Asrite``.

    Attributes:
        setting: Left-going flux at plane i.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``AsriteBuilder`` into ``Asrite``.

        Returns:
            ``Asrite`` for ``AsriteBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Asrite(
            setting=setting,
        )
