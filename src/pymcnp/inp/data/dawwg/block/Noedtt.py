import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Noedtt(_option.BlockOption):
    """
    Represents INP noedtt elements.

    Attributes:
        setting: Suppress writing EDITIT on/off.
    """

    _KEYWORD = 'noedtt'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Anoedtt( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Noedtt``.

        Parameters:
            setting: Suppress writing EDITIT on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class NoedttBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Noedtt``.

    Attributes:
        setting: Suppress writing EDITIT on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NoedttBuilder`` into ``Noedtt``.

        Returns:
            ``Noedtt`` for ``NoedttBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Noedtt(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Noedtt):
        """
        Unbuilds ``Noedtt`` into ``NoedttBuilder``

        Returns:
            ``NoedttBuilder`` for ``Noedtt``.
        """

        return NoedttBuilder(
            setting=copy.deepcopy(ast.setting),
        )
