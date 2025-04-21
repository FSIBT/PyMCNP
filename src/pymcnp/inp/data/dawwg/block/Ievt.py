import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ievt(BlockOption, keyword='ievt'):
    """
    Represents INP ievt elements.

    Attributes:
        setting: Calculation type.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aievt( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ievt``.

        Parameters:
            setting: Calculation type.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {0, 1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class IevtBuilder:
    """
    Builds ``Ievt``.

    Attributes:
        setting: Calculation type.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``IevtBuilder`` into ``Ievt``.

        Returns:
            ``Ievt`` for ``IevtBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ievt(
            setting=setting,
        )
