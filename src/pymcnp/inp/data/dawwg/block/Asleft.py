import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Asleft(BlockOption, keyword='asleft'):
    """
    Represents INP asleft elements.

    Attributes:
        setting: Right-going flux at plane i.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aasleft( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Asleft``.

        Parameters:
            setting: Right-going flux at plane i.

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
class AsleftBuilder:
    """
    Builds ``Asleft``.

    Attributes:
        setting: Right-going flux at plane i.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``AsleftBuilder`` into ``Asleft``.

        Returns:
            ``Asleft`` for ``AsleftBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Asleft(
            setting=setting,
        )
