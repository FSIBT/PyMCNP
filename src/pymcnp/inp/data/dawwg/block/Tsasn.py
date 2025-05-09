import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Tsasn(BlockOption):
    """
    Represents INP tsasn elements.

    Attributes:
        setting: Sn order for lower order TSA sweeps.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Atsasn( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Tsasn``.

        Parameters:
            setting: Sn order for lower order TSA sweeps.

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
class TsasnBuilder:
    """
    Builds ``Tsasn``.

    Attributes:
        setting: Sn order for lower order TSA sweeps.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``TsasnBuilder`` into ``Tsasn``.

        Returns:
            ``Tsasn`` for ``TsasnBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Tsasn(
            setting=setting,
        )
