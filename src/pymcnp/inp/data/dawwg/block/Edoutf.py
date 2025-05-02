import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Edoutf(BlockOption):
    """
    Represents INP edoutf elements.

    Attributes:
        setting: ASCII output files control.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aedoutf( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Edoutf``.

        Parameters:
            setting: ASCII output files control.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {-3, -2, -1, 0, 1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class EdoutfBuilder:
    """
    Builds ``Edoutf``.

    Attributes:
        setting: ASCII output files control.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``EdoutfBuilder`` into ``Edoutf``.

        Returns:
            ``Edoutf`` for ``EdoutfBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Edoutf(
            setting=setting,
        )
