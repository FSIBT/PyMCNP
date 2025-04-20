import re
import typing
import dataclasses


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Xsectp(BlockOption_, keyword='xsectp'):
    """
    Represents INP xsectp elements.

    Attributes:
        setting: Cross-section print flag.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Axsectp( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Xsectp``.

        Parameters:
            setting: Cross-section print flag.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class XsectpBuilder:
    """
    Builds ``Xsectp``.

    Attributes:
        setting: Cross-section print flag.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``XsectpBuilder`` into ``Xsectp``.

        Returns:
            ``Xsectp`` for ``XsectpBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Xsectp(
            setting=setting,
        )
