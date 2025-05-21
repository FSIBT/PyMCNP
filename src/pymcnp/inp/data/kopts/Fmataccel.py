import re
import copy
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Fmataccel(KoptsOption):
    """
    Represents INP fmataccel elements.

    Attributes:
        setting: fmataccel.
    """

    _KEYWORD = 'fmataccel'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Afmataccel( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Fmataccel``.

        Parameters:
            setting: fmataccel.

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
class FmataccelBuilder:
    """
    Builds ``Fmataccel``.

    Attributes:
        setting: fmataccel.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``FmataccelBuilder`` into ``Fmataccel``.

        Returns:
            ``Fmataccel`` for ``FmataccelBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Fmataccel(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Fmataccel):
        """
        Unbuilds ``Fmataccel`` into ``FmataccelBuilder``

        Returns:
            ``FmataccelBuilder`` for ``Fmataccel``.
        """

        return Fmataccel(
            setting=copy.deepcopy(ast.setting),
        )
