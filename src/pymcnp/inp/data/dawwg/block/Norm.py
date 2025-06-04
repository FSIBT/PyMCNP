import re
import copy
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Norm(BlockOption):
    """
    Represents INP norm elements.

    Attributes:
        setting: Norm.
    """

    _KEYWORD = 'norm'

    _ATTRS = {
        'setting': types.Real,
    }

    _REGEX = re.compile(rf'\Anorm( {types.Real._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Real):
        """
        Initializes ``Norm``.

        Parameters:
            setting: Norm.

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
class NormBuilder:
    """
    Builds ``Norm``.

    Attributes:
        setting: Norm.
    """

    setting: str | float | types.Real

    def build(self):
        """
        Builds ``NormBuilder`` into ``Norm``.

        Returns:
            ``Norm`` for ``NormBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Real):
            setting = self.setting
        elif isinstance(self.setting, float) or isinstance(self.setting, int):
            setting = types.Real(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Real.from_mcnp(self.setting)

        return Norm(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Norm):
        """
        Unbuilds ``Norm`` into ``NormBuilder``

        Returns:
            ``NormBuilder`` for ``Norm``.
        """

        return Norm(
            setting=copy.deepcopy(ast.setting),
        )
