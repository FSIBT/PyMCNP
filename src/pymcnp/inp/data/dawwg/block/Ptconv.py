import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ptconv(BlockOption):
    """
    Represents INP ptconv elements.

    Attributes:
        setting: Special criticality convergence scheme on/off.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aptconv( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ptconv``.

        Parameters:
            setting: Special criticality convergence scheme on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class PtconvBuilder:
    """
    Builds ``Ptconv``.

    Attributes:
        setting: Special criticality convergence scheme on/off.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``PtconvBuilder`` into ``Ptconv``.

        Returns:
            ``Ptconv`` for ``PtconvBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ptconv(
            setting=setting,
        )
