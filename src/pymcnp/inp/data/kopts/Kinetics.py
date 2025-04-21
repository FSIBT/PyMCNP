import re
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Kinetics(KoptsOption, keyword='kinetics'):
    """
    Represents INP kinetics elements.

    Attributes:
        setting: Yes/No calculate point-kinetics parameters.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Akinetics( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Kinetics``.

        Parameters:
            setting: Yes/No calculate point-kinetics parameters.

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
class KineticsBuilder:
    """
    Builds ``Kinetics``.

    Attributes:
        setting: Yes/No calculate point-kinetics parameters.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``KineticsBuilder`` into ``Kinetics``.

        Returns:
            ``Kinetics`` for ``KineticsBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Kinetics(
            setting=setting,
        )
