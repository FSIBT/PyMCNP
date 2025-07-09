import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Linear(_option.KpertOption):
    """
    Represents INP linear elements.

    Attributes:
        setting: Pertubated fission source on/off.
    """

    _KEYWORD = 'linear'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Alinear( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Linear``.

        Parameters:
            setting: Pertubated fission source on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class LinearBuilder(_option.KpertOptionBuilder):
    """
    Builds ``Linear``.

    Attributes:
        setting: Pertubated fission source on/off.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``LinearBuilder`` into ``Linear``.

        Returns:
            ``Linear`` for ``LinearBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Linear(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Linear):
        """
        Unbuilds ``Linear`` into ``LinearBuilder``

        Returns:
            ``LinearBuilder`` for ``Linear``.
        """

        return LinearBuilder(
            setting=copy.deepcopy(ast.setting),
        )
