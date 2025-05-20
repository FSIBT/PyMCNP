import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Enorm(FmeshOption):
    """
    Represents INP enorm elements.

    Attributes:
        setting: Tally results divided by energy yes/no.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aenorm( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Enorm``.

        Parameters:
            setting: Tally results divided by energy yes/no.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class EnormBuilder:
    """
    Builds ``Enorm``.

    Attributes:
        setting: Tally results divided by energy yes/no.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``EnormBuilder`` into ``Enorm``.

        Returns:
            ``Enorm`` for ``EnormBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Enorm(
            setting=setting,
        )
