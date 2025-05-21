import re
import copy
import typing
import dataclasses


from ._option import FmultOption
from ....utils import types
from ....utils import errors


class Method(FmultOption):
    """
    Represents INP method elements.

    Attributes:
        setting: Gaussian sampling algorithm setting.
    """

    _KEYWORD = 'method'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Amethod( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Method``.

        Parameters:
            setting: Gaussian sampling algorithm setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {0, 1, 3, 5, 6, 7}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class MethodBuilder:
    """
    Builds ``Method``.

    Attributes:
        setting: Gaussian sampling algorithm setting.
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

        return Method(
            setting=copy.deepcopy(ast.setting),
        )
