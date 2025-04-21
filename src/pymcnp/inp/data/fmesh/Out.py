import re
import typing
import dataclasses


from ._option import FmeshOption
from ....utils import types
from ....utils import errors


class Out(FmeshOption, keyword='out'):
    """
    Represents INP out elements.

    Attributes:
        setting: Output format.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aout( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Out``.

        Parameters:
            setting: Output format.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'col', 'cf', 'ij', 'ik', 'jk', 'none'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class OutBuilder:
    """
    Builds ``Out``.

    Attributes:
        setting: Output format.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``OutBuilder`` into ``Out``.

        Returns:
            ``Out`` for ``OutBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Out(
            setting=setting,
        )
