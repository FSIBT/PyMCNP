import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Eloss(_option.TroptOption):
    """
    Represents INP eloss elements.

    Attributes:
        setting: Slowing down energy losses setting.
    """

    _KEYWORD = 'eloss'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aeloss( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Eloss``.

        Parameters:
            setting: Slowing down energy losses setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'off', 'strag1', 'csda'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class ElossBuilder(_option.TroptOptionBuilder):
    """
    Builds ``Eloss``.

    Attributes:
        setting: Slowing down energy losses setting.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``ElossBuilder`` into ``Eloss``.

        Returns:
            ``Eloss`` for ``ElossBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Eloss(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Eloss):
        """
        Unbuilds ``Eloss`` into ``ElossBuilder``

        Returns:
            ``ElossBuilder`` for ``Eloss``.
        """

        return ElossBuilder(
            setting=copy.deepcopy(ast.setting),
        )
