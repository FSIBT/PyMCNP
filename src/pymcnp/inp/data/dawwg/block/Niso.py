import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Niso(BlockOption):
    """
    Represents INP niso elements.

    Attributes:
        setting: Number of isotopes.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aniso( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Niso``.

        Parameters:
            setting: Number of isotopes.

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
class NisoBuilder:
    """
    Builds ``Niso``.

    Attributes:
        setting: Number of isotopes.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``NisoBuilder`` into ``Niso``.

        Returns:
            ``Niso`` for ``NisoBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Niso(
            setting=setting,
        )
