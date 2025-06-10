import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Type(_option.FmeshOption):
    """
    Represents INP type elements.

    Attributes:
        setting: Tally quantity.
    """

    _KEYWORD = 'type'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Atype( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Type``.

        Parameters:
            setting: Tally quantity.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {'flux', 'source'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class TypeBuilder(_option.FmeshOptionBuilder):
    """
    Builds ``Type``.

    Attributes:
        setting: Tally quantity.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``TypeBuilder`` into ``Type``.

        Returns:
            ``Type`` for ``TypeBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Type(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Type):
        """
        Unbuilds ``Type`` into ``TypeBuilder``

        Returns:
            ``TypeBuilder`` for ``Type``.
        """

        return TypeBuilder(
            setting=copy.deepcopy(ast.setting),
        )
