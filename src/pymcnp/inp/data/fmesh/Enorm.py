import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Enorm(_option.FmeshOption):
    """
    Represents INP enorm elements.

    Attributes:
        setting: Tally results divided by energy yes/no.
    """

    _KEYWORD = 'enorm'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aenorm( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Enorm``.

        Parameters:
            setting: Tally results divided by energy yes/no.

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
class EnormBuilder(_option.FmeshOptionBuilder):
    """
    Builds ``Enorm``.

    Attributes:
        setting: Tally results divided by energy yes/no.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``EnormBuilder`` into ``Enorm``.

        Returns:
            ``Enorm`` for ``EnormBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Enorm(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Enorm):
        """
        Unbuilds ``Enorm`` into ``EnormBuilder``

        Returns:
            ``EnormBuilder`` for ``Enorm``.
        """

        return EnormBuilder(
            setting=copy.deepcopy(ast.setting),
        )
