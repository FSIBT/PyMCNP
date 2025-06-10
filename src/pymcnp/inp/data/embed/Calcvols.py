import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Calcvols(_option.EmbedOption):
    """
    Represents INP calcvols elements.

    Attributes:
        setting: Yes/no calculate the inferred geometry cell information.
    """

    _KEYWORD = 'calcvols'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Acalcvols( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Calcvols``.

        Parameters:
            setting: Yes/no calculate the inferred geometry cell information.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {'yes', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class CalcvolsBuilder(_option.EmbedOptionBuilder):
    """
    Builds ``Calcvols``.

    Attributes:
        setting: Yes/no calculate the inferred geometry cell information.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``CalcvolsBuilder`` into ``Calcvols``.

        Returns:
            ``Calcvols`` for ``CalcvolsBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Calcvols(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Calcvols):
        """
        Unbuilds ``Calcvols`` into ``CalcvolsBuilder``

        Returns:
            ``CalcvolsBuilder`` for ``Calcvols``.
        """

        return CalcvolsBuilder(
            setting=copy.deepcopy(ast.setting),
        )
