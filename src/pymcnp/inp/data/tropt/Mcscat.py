import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Mcscat(_option.TroptOption):
    """
    Represents INP mcscat elements.

    Attributes:
        setting: Multiple coulomb scattering setting.
    """

    _KEYWORD = 'mcscat'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Amcscat( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Mcscat``.

        Parameters:
            setting: Multiple coulomb scattering setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {'off', 'fnal1', 'gaussian', 'fnal2'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class McscatBuilder(_option.TroptOptionBuilder):
    """
    Builds ``Mcscat``.

    Attributes:
        setting: Multiple coulomb scattering setting.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``McscatBuilder`` into ``Mcscat``.

        Returns:
            ``Mcscat`` for ``McscatBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Mcscat(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Mcscat):
        """
        Unbuilds ``Mcscat`` into ``McscatBuilder``

        Returns:
            ``McscatBuilder`` for ``Mcscat``.
        """

        return McscatBuilder(
            setting=copy.deepcopy(ast.setting),
        )
