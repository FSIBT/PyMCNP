import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Trcor(_option.BlockOption):
    """
    Represents INP trcor elements.

    Attributes:
        setting: Trcor.
    """

    _KEYWORD = 'trcor'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Atrcor( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Trcor``.

        Parameters:
            setting: Trcor.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'diag'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class TrcorBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Trcor``.

    Attributes:
        setting: Trcor.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``TrcorBuilder`` into ``Trcor``.

        Returns:
            ``Trcor`` for ``TrcorBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Trcor(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Trcor):
        """
        Unbuilds ``Trcor`` into ``TrcorBuilder``

        Returns:
            ``TrcorBuilder`` for ``Trcor``.
        """

        return TrcorBuilder(
            setting=copy.deepcopy(ast.setting),
        )
