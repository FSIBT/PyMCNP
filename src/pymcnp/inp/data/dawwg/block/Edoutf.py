import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Edoutf(_option.BlockOption):
    """
    Represents INP edoutf elements.

    Attributes:
        setting: ASCII output files control.
    """

    _KEYWORD = 'edoutf'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aedoutf( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Edoutf``.

        Parameters:
            setting: ASCII output files control.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {-3, -2, -1, 0, 1, 2, 3}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class EdoutfBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Edoutf``.

    Attributes:
        setting: ASCII output files control.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``EdoutfBuilder`` into ``Edoutf``.

        Returns:
            ``Edoutf`` for ``EdoutfBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Edoutf(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Edoutf):
        """
        Unbuilds ``Edoutf`` into ``EdoutfBuilder``

        Returns:
            ``EdoutfBuilder`` for ``Edoutf``.
        """

        return EdoutfBuilder(
            setting=copy.deepcopy(ast.setting),
        )
