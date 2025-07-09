import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Col(_option.SsrOption):
    """
    Represents INP col elements.

    Attributes:
        setting: Collision option setting.
    """

    _KEYWORD = 'col'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Acol( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Col``.

        Parameters:
            setting: Collision option setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {-1, 0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class ColBuilder(_option.SsrOptionBuilder):
    """
    Builds ``Col``.

    Attributes:
        setting: Collision option setting.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``ColBuilder`` into ``Col``.

        Returns:
            ``Col`` for ``ColBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Col(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Col):
        """
        Unbuilds ``Col`` into ``ColBuilder``

        Returns:
            ``ColBuilder`` for ``Col``.
        """

        return ColBuilder(
            setting=copy.deepcopy(ast.setting),
        )
