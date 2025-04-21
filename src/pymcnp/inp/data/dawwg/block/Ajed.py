import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Ajed(BlockOption, keyword='ajed'):
    """
    Represents INP ajed elements.

    Attributes:
        setting: Regular/adjoint edits control.
    """

    _ATTRS = {
        'setting': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aajed( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, setting: types.IntegerOrJump):
        """
        Initializes ``Ajed``.

        Parameters:
            setting: Regular/adjoint edits control.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.IntegerOrJump] = setting


@dataclasses.dataclass
class AjedBuilder:
    """
    Builds ``Ajed``.

    Attributes:
        setting: Regular/adjoint edits control.
    """

    setting: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``AjedBuilder`` into ``Ajed``.

        Returns:
            ``Ajed`` for ``AjedBuilder``.
        """

        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.IntegerOrJump(self.setting)
        elif isinstance(self.setting, str):
            setting = types.IntegerOrJump.from_mcnp(self.setting)

        return Ajed(
            setting=setting,
        )
