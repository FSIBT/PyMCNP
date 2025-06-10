import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Atom(_option.EmbeeOption):
    """
    Represents INP atom elements.

    Attributes:
        setting: Flag to multiply by atom density.
    """

    _KEYWORD = 'atom'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aatom( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Atom``.

        Parameters:
            setting: Flag to multiply by atom density.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class AtomBuilder(_option.EmbeeOptionBuilder):
    """
    Builds ``Atom``.

    Attributes:
        setting: Flag to multiply by atom density.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``AtomBuilder`` into ``Atom``.

        Returns:
            ``Atom`` for ``AtomBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Atom(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Atom):
        """
        Unbuilds ``Atom`` into ``AtomBuilder``

        Returns:
            ``AtomBuilder`` for ``Atom``.
        """

        return AtomBuilder(
            setting=copy.deepcopy(ast.setting),
        )
