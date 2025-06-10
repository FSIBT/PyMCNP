import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Ntichi(_option.BlockOption):
    """
    Represents INP ntichi elements.

    Attributes:
        setting: MENDF fission fraction.
    """

    _KEYWORD = 'ntichi'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Antichi( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Ntichi``.

        Parameters:
            setting: MENDF fission fraction.

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

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class NtichiBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Ntichi``.

    Attributes:
        setting: MENDF fission fraction.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``NtichiBuilder`` into ``Ntichi``.

        Returns:
            ``Ntichi`` for ``NtichiBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Ntichi(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Ntichi):
        """
        Unbuilds ``Ntichi`` into ``NtichiBuilder``

        Returns:
            ``NtichiBuilder`` for ``Ntichi``.
        """

        return NtichiBuilder(
            setting=copy.deepcopy(ast.setting),
        )
