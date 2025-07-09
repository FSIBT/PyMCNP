import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Fissrp(_option.BlockOption):
    """
    Represents INP fissrp elements.

    Attributes:
        setting: Print fission source rate on/off.
    """

    _KEYWORD = 'fissrp'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Afissrp( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Fissrp``.

        Parameters:
            setting: Print fission source rate on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class FissrpBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Fissrp``.

    Attributes:
        setting: Print fission source rate on/off.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``FissrpBuilder`` into ``Fissrp``.

        Returns:
            ``Fissrp`` for ``FissrpBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Fissrp(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Fissrp):
        """
        Unbuilds ``Fissrp`` into ``FissrpBuilder``

        Returns:
            ``FissrpBuilder`` for ``Fissrp``.
        """

        return FissrpBuilder(
            setting=copy.deepcopy(ast.setting),
        )
