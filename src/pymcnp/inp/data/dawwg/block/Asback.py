import re
import copy
import typing
import dataclasses


from . import _option
from .....utils import types
from .....utils import errors


class Asback(_option.BlockOption):
    """
    Represents INP asback elements.

    Attributes:
        setting: Front-going flux at plane k.
    """

    _KEYWORD = 'asback'

    _ATTRS = {
        'setting': types.Integer,
    }

    _REGEX = re.compile(rf'\Aasback( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, setting: types.Integer):
        """
        Initializes ``Asback``.

        Parameters:
            setting: Front-going flux at plane k.

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

        self.setting: typing.Final[types.Integer] = setting


@dataclasses.dataclass
class AsbackBuilder(_option.BlockOptionBuilder):
    """
    Builds ``Asback``.

    Attributes:
        setting: Front-going flux at plane k.
    """

    setting: str | int | types.Integer

    def build(self):
        """
        Builds ``AsbackBuilder`` into ``Asback``.

        Returns:
            ``Asback`` for ``AsbackBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.Integer):
            setting = self.setting
        elif isinstance(self.setting, int):
            setting = types.Integer(self.setting)
        elif isinstance(self.setting, str):
            setting = types.Integer.from_mcnp(self.setting)

        return Asback(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Asback):
        """
        Unbuilds ``Asback`` into ``AsbackBuilder``

        Returns:
            ``AsbackBuilder`` for ``Asback``.
        """

        return AsbackBuilder(
            setting=copy.deepcopy(ast.setting),
        )
