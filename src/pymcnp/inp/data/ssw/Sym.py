import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Sym(_option.SswOption):
    """
    Represents INP sym elements.

    Attributes:
        setting: Symmetric option flag.
    """

    _KEYWORD = 'sym'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Asym( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Sym``.

        Parameters:
            setting: Symmetric option flag.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class SymBuilder(_option.SswOptionBuilder):
    """
    Builds ``Sym``.

    Attributes:
        setting: Symmetric option flag.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``SymBuilder`` into ``Sym``.

        Returns:
            ``Sym`` for ``SymBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Sym(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Sym):
        """
        Unbuilds ``Sym`` into ``SymBuilder``

        Returns:
            ``SymBuilder`` for ``Sym``.
        """

        return SymBuilder(
            setting=copy.deepcopy(ast.setting),
        )
