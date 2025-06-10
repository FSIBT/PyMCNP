import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Lib(_option.BlockOption):
    """
    Represents INP lib elements.

    Attributes:
        setting: Name of cross-section file.
    """

    _KEYWORD = 'lib'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Alib( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Lib``.

        Parameters:
            setting: Name of cross-section file.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class LibBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Lib``.

    Attributes:
        setting: Name of cross-section file.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``LibBuilder`` into ``Lib``.

        Returns:
            ``Lib`` for ``LibBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Lib(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Lib):
        """
        Unbuilds ``Lib`` into ``LibBuilder``

        Returns:
            ``LibBuilder`` for ``Lib``.
        """

        return LibBuilder(
            setting=copy.deepcopy(ast.setting),
        )
