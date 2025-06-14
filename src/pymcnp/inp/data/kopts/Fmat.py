import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Fmat(_option.KoptsOption):
    """
    Represents INP fmat elements.

    Attributes:
        setting: Yes/No FMAT.
    """

    _KEYWORD = 'fmat'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Afmat( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Fmat``.

        Parameters:
            setting: Yes/No FMAT.

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
class FmatBuilder(_option.KoptsOptionBuilder):
    """
    Builds ``Fmat``.

    Attributes:
        setting: Yes/No FMAT.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``FmatBuilder`` into ``Fmat``.

        Returns:
            ``Fmat`` for ``FmatBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Fmat(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Fmat):
        """
        Unbuilds ``Fmat`` into ``FmatBuilder``

        Returns:
            ``FmatBuilder`` for ``Fmat``.
        """

        return FmatBuilder(
            setting=copy.deepcopy(ast.setting),
        )
