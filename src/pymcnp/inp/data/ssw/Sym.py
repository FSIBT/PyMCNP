import re
import typing
import dataclasses


from ._option import SswOption
from ....utils import types
from ....utils import errors


class Sym(SswOption, keyword='sym'):
    """
    Represents INP sym elements.

    Attributes:
        setting: Symmetric option flag.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Asym( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Sym``.

        Parameters:
            setting: Symmetric option flag.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class SymBuilder:
    """
    Builds ``Sym``.

    Attributes:
        setting: Symmetric option flag.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``SymBuilder`` into ``Sym``.

        Returns:
            ``Sym`` for ``SymBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Sym(
            setting=setting,
        )
