import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Tnorm(_option.FmeshOption):
    """
    Represents INP tnorm elements.

    Attributes:
        setting: Tally results divided by time yes/no.
    """

    _KEYWORD = 'tnorm'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Atnorm( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Tnorm``.

        Parameters:
            setting: Tally results divided by time yes/no.

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
class TnormBuilder(_option.FmeshOptionBuilder):
    """
    Builds ``Tnorm``.

    Attributes:
        setting: Tally results divided by time yes/no.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``TnormBuilder`` into ``Tnorm``.

        Returns:
            ``Tnorm`` for ``TnormBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Tnorm(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Tnorm):
        """
        Unbuilds ``Tnorm`` into ``TnormBuilder``

        Returns:
            ``TnormBuilder`` for ``Tnorm``.
        """

        return TnormBuilder(
            setting=copy.deepcopy(ast.setting),
        )
