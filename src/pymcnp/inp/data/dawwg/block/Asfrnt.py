import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Asfrnt(BlockOption):
    """
    Represents INP asfrnt elements.

    Attributes:
        setting: Back-going flux at plane k.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aasfrnt( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Asfrnt``.

        Parameters:
            setting: Back-going flux at plane k.

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
class AsfrntBuilder:
    """
    Builds ``Asfrnt``.

    Attributes:
        setting: Back-going flux at plane k.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``AsfrntBuilder`` into ``Asfrnt``.

        Returns:
            ``Asfrnt`` for ``AsfrntBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Asfrnt(
            setting=setting,
        )
