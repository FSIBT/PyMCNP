import re
import typing
import dataclasses


from .option_ import TroptOption_
from ....utils import types
from ....utils import errors


class Nescat(TroptOption_, keyword='nescat'):
    """
    Represents INP nescat elements.

    Attributes:
        setting: Nuclear elastic scattering setting.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Anescat( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Nescat``.

        Parameters:
            setting: Nuclear elastic scattering setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'off', 'on'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class NescatBuilder:
    """
    Builds ``Nescat``.

    Attributes:
        setting: Nuclear elastic scattering setting.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``NescatBuilder`` into ``Nescat``.

        Returns:
            ``Nescat`` for ``NescatBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Nescat(
            setting=setting,
        )
