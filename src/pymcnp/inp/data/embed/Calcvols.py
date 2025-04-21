import re
import typing
import dataclasses


from ._option import EmbedOption
from ....utils import types
from ....utils import errors


class Calcvols(EmbedOption, keyword='calcvols'):
    """
    Represents INP calcvols elements.

    Attributes:
        setting: Yes/no calculate the inferred geometry cell information.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Acalcvols( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Calcvols``.

        Parameters:
            setting: Yes/no calculate the inferred geometry cell information.

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
class CalcvolsBuilder:
    """
    Builds ``Calcvols``.

    Attributes:
        setting: Yes/no calculate the inferred geometry cell information.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``CalcvolsBuilder`` into ``Calcvols``.

        Returns:
            ``Calcvols`` for ``CalcvolsBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Calcvols(
            setting=setting,
        )
