import re
import typing
import dataclasses


from .option_ import KpertOption_
from ....utils import types
from ....utils import errors


class Linear(KpertOption_, keyword='linear'):
    """
    Represents INP linear elements.

    Attributes:
        setting: Pertubated fission source on/off.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Alinear( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Linear``.

        Parameters:
            setting: Pertubated fission source on/off.

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
class LinearBuilder:
    """
    Builds ``Linear``.

    Attributes:
        setting: Pertubated fission source on/off.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``LinearBuilder`` into ``Linear``.

        Returns:
            ``Linear`` for ``LinearBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Linear(
            setting=setting,
        )
