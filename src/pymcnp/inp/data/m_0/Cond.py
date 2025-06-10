import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Cond(_option.MOption_0):
    """
    Represents INP cond elements.

    Attributes:
        setting: Conduction state for EL03 electron-transport evaluation.
    """

    _KEYWORD = 'cond'

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(rf'\Acond( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Real):
        """
        Initializes ``Cond``.

        Parameters:
            setting: Conduction state for EL03 electron-transport evaluation.

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

        self.setting: typing.Final[types.Real] = setting


@dataclasses.dataclass
class CondBuilder(_option.MOptionBuilder_0):
    """
    Builds ``Cond``.

    Attributes:
        setting: Conduction state for EL03 electron-transport evaluation.
    """

    setting: str | float | types.Real

    def build(self):
        """
        Builds ``CondBuilder`` into ``Cond``.

        Returns:
            ``Cond`` for ``CondBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Real):
            setting = self.setting
        elif isinstance(self.setting, float) or isinstance(self.setting, int):
            setting = types.Real(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Real.from_mcnp(self.setting)

        return Cond(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Cond):
        """
        Unbuilds ``Cond`` into ``CondBuilder``

        Returns:
            ``CondBuilder`` for ``Cond``.
        """

        return CondBuilder(
            setting=copy.deepcopy(ast.setting),
        )
