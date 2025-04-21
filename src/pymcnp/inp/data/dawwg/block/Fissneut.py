import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Fissneut(BlockOption, keyword='fissneut'):
    """
    Represents INP fissneut elements.

    Attributes:
        setting: Fission neutron flag.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Afissneut( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Fissneut``.

        Parameters:
            setting: Fission neutron flag.

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
class FissneutBuilder:
    """
    Builds ``Fissneut``.

    Attributes:
        setting: Fission neutron flag.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``FissneutBuilder`` into ``Fissneut``.

        Returns:
            ``Fissneut`` for ``FissneutBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Fissneut(
            setting=setting,
        )
