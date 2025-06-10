import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Nreact(_option.TroptOption):
    """
    Represents INP nreact elements.

    Attributes:
        setting: Nuclear reactions setting.
    """

    _KEYWORD = 'nreact'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Anreact( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Nreact``.

        Parameters:
            setting: Nuclear reactions setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {'off', 'on', 'atten', 'remove'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class NreactBuilder(_option.TroptOptionBuilder):
    """
    Builds ``Nreact``.

    Attributes:
        setting: Nuclear reactions setting.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``NreactBuilder`` into ``Nreact``.

        Returns:
            ``Nreact`` for ``NreactBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Nreact(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Nreact):
        """
        Unbuilds ``Nreact`` into ``NreactBuilder``

        Returns:
            ``NreactBuilder`` for ``Nreact``.
        """

        return NreactBuilder(
            setting=copy.deepcopy(ast.setting),
        )
