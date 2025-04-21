import re
import typing
import dataclasses


from ._option import TroptOption
from ....utils import types
from ....utils import errors


class Nreact(TroptOption, keyword='nreact'):
    """
    Represents INP nreact elements.

    Attributes:
        setting: Nuclear reactions setting.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Anreact( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Nreact``.

        Parameters:
            setting: Nuclear reactions setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'off', 'on', 'atten', 'remove'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class NreactBuilder:
    """
    Builds ``Nreact``.

    Attributes:
        setting: Nuclear reactions setting.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``NreactBuilder`` into ``Nreact``.

        Returns:
            ``Nreact`` for ``NreactBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Nreact(
            setting=setting,
        )
