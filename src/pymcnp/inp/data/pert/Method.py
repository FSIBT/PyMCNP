import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Method(_option.PertOption):
    """
    Represents INP method elements.

    Attributes:
        setting: Printing and specifies setting.
    """

    _KEYWORD = 'method'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Amethod( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Method``.

        Parameters:
            setting: Printing and specifies setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {1, -1, 2, -2, 3, -3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class MethodBuilder(_option.PertOptionBuilder):
    """
    Builds ``Method``.

    Attributes:
        setting: Printing and specifies setting.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``MethodBuilder`` into ``Method``.

        Returns:
            ``Method`` for ``MethodBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Method(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Method):
        """
        Unbuilds ``Method`` into ``MethodBuilder``

        Returns:
            ``MethodBuilder`` for ``Method``.
        """

        return MethodBuilder(
            setting=copy.deepcopy(ast.setting),
        )
