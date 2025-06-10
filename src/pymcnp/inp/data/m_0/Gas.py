import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Gas(_option.MOption_0):
    """
    Represents INP gas elements.

    Attributes:
        setting: Flag for density-effect correction to electron stopping power.
    """

    _KEYWORD = 'gas'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Agas( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Gas``.

        Parameters:
            setting: Flag for density-effect correction to electron stopping power.

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
class GasBuilder(_option.MOptionBuilder_0):
    """
    Builds ``Gas``.

    Attributes:
        setting: Flag for density-effect correction to electron stopping power.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``GasBuilder`` into ``Gas``.

        Returns:
            ``Gas`` for ``GasBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Gas(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Gas):
        """
        Unbuilds ``Gas`` into ``GasBuilder``

        Returns:
            ``GasBuilder`` for ``Gas``.
        """

        return GasBuilder(
            setting=copy.deepcopy(ast.setting),
        )
