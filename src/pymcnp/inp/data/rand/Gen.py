import re
import copy
import typing
import dataclasses


from ._option import RandOption
from ....utils import types
from ....utils import errors


class Gen(RandOption):
    """
    Represents INP gen elements.

    Attributes:
        setting: Type of pseudorandom number generator.
    """

    _KEYWORD = 'gen'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Agen( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Gen``.

        Parameters:
            setting: Type of pseudorandom number generator.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {1, 2, 3, 4}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class GenBuilder:
    """
    Builds ``Gen``.

    Attributes:
        setting: Type of pseudorandom number generator.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``GenBuilder`` into ``Gen``.

        Returns:
            ``Gen`` for ``GenBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Gen(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Gen):
        """
        Unbuilds ``Gen`` into ``GenBuilder``

        Returns:
            ``GenBuilder`` for ``Gen``.
        """

        return Gen(
            setting=copy.deepcopy(ast.setting),
        )
