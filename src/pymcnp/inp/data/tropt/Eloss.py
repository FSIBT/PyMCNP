import re
import typing
import dataclasses


from ._option import TroptOption
from ....utils import types
from ....utils import errors


class Eloss(TroptOption):
    """
    Represents INP eloss elements.

    Attributes:
        setting: Slowing down energy losses setting.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aeloss( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Eloss``.

        Parameters:
            setting: Slowing down energy losses setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'off', 'strag1', 'csda'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class ElossBuilder:
    """
    Builds ``Eloss``.

    Attributes:
        setting: Slowing down energy losses setting.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``ElossBuilder`` into ``Eloss``.

        Returns:
            ``Eloss`` for ``ElossBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Eloss(
            setting=setting,
        )
