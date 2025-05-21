import re
import copy
import typing
import dataclasses


from ._option import KoptsOption
from ....utils import types
from ....utils import errors


class Precursor(KoptsOption):
    """
    Represents INP precursor elements.

    Attributes:
        setting: Yes/No detailed precursor information.
    """

    _KEYWORD = 'precursor'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aprecursor( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Precursor``.

        Parameters:
            setting: Yes/No detailed precursor information.

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
class PrecursorBuilder:
    """
    Builds ``Precursor``.

    Attributes:
        setting: Yes/No detailed precursor information.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``PrecursorBuilder`` into ``Precursor``.

        Returns:
            ``Precursor`` for ``PrecursorBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Precursor(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Precursor):
        """
        Unbuilds ``Precursor`` into ``PrecursorBuilder``

        Returns:
            ``PrecursorBuilder`` for ``Precursor``.
        """

        return Precursor(
            setting=copy.deepcopy(ast.setting),
        )
