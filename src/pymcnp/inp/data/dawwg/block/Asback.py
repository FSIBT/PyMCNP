import re
import typing
import dataclasses


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Asback(BlockOption_, keyword='asback'):
    """
    Represents INP asback elements.

    Attributes:
        setting: Front-going flux at plane k.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aasback( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Asback``.

        Parameters:
            setting: Front-going flux at plane k.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class AsbackBuilder:
    """
    Builds ``Asback``.

    Attributes:
        setting: Front-going flux at plane k.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``AsbackBuilder`` into ``Asback``.

        Returns:
            ``Asback`` for ``AsbackBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Asback(
            setting=setting,
        )
