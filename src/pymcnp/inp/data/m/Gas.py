import re
import typing
import dataclasses


from .option_ import MOption_
from ....utils import types
from ....utils import errors


class Gas(MOption_, keyword='gas'):
    """
    Represents INP gas elements.

    Attributes:
        setting: Flag for density-effect correction to electron stopping power.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Agas( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Gas``.

        Parameters:
            setting: Flag for density-effect correction to electron stopping power.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class GasBuilder:
    """
    Builds ``Gas``.

    Attributes:
        setting: Flag for density-effect correction to electron stopping power.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``GasBuilder`` into ``Gas``.

        Returns:
            ``Gas`` for ``GasBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Gas(
            setting=setting,
        )
