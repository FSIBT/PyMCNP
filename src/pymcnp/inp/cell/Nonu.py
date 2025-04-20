import re
import typing
import dataclasses


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Nonu(CellOption_, keyword='nonu'):
    """
    Represents INP nonu elements.

    Attributes:
        setting: Cell fission setting.
    """

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Anonu( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Nonu``.

        Parameters:
            setting: Cell fission setting.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting.value not in {0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class NonuBuilder:
    """
    Builds ``Nonu``.

    Attributes:
        setting: Cell fission setting.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NonuBuilder`` into ``Nonu``.

        Returns:
            ``Nonu`` for ``NonuBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Nonu(
            setting=setting,
        )
