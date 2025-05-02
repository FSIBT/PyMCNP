import re
import typing
import dataclasses


from ._option import TroptOption
from ....utils import types
from ....utils import errors


class Mcscat(TroptOption):
    """
    Represents INP mcscat elements.

    Attributes:
        setting: Multiple coulomb scattering setting.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Amcscat( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Mcscat``.

        Parameters:
            setting: Multiple coulomb scattering setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'off', 'fnal1', 'gaussian', 'fnal2'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class McscatBuilder:
    """
    Builds ``Mcscat``.

    Attributes:
        setting: Multiple coulomb scattering setting.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``McscatBuilder`` into ``Mcscat``.

        Returns:
            ``Mcscat`` for ``McscatBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Mcscat(
            setting=setting,
        )
