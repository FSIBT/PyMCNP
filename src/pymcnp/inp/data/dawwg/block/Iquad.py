import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Iquad(_option.BlockOption):
    """
    Represents INP iquad elements.

    Attributes:
        setting: Quadrature.
    """

    _KEYWORD = 'iquad'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aiquad( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Iquad``.

        Parameters:
            setting: Quadrature.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class IquadBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Iquad``.

    Attributes:
        setting: Quadrature.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``IquadBuilder`` into ``Iquad``.

        Returns:
            ``Iquad`` for ``IquadBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Iquad(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Iquad):
        """
        Unbuilds ``Iquad`` into ``IquadBuilder``

        Returns:
            ``IquadBuilder`` for ``Iquad``.
        """

        return IquadBuilder(
            setting=copy.deepcopy(ast.setting),
        )
