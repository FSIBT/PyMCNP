import re
import typing
import dataclasses


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Col(SsrOption_, keyword='col'):
    """
    Represents INP col elements.

    Attributes:
        setting: Collision option setting.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Acol( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Col``.

        Parameters:
            setting: Collision option setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {-1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class ColBuilder:
    """
    Builds ``Col``.

    Attributes:
        setting: Collision option setting.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``ColBuilder`` into ``Col``.

        Returns:
            ``Col`` for ``ColBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Col(
            setting=setting,
        )
