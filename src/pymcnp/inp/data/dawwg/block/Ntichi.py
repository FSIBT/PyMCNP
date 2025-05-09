import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ntichi(BlockOption):
    """
    Represents INP ntichi elements.

    Attributes:
        setting: MENDF fission fraction.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Antichi( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ntichi``.

        Parameters:
            setting: MENDF fission fraction.

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
class NtichiBuilder:
    """
    Builds ``Ntichi``.

    Attributes:
        setting: MENDF fission fraction.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``NtichiBuilder`` into ``Ntichi``.

        Returns:
            ``Ntichi`` for ``NtichiBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ntichi(
            setting=setting,
        )
