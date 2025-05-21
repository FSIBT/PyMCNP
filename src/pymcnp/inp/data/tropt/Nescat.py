import re
import copy
import typing
import dataclasses


from ._option import TroptOption
from ....utils import types
from ....utils import errors


class Nescat(TroptOption):
    """
    Represents INP nescat elements.

    Attributes:
        setting: Nuclear elastic scattering setting.
    """

    _KEYWORD = 'nescat'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Anescat( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Nescat``.

        Parameters:
            setting: Nuclear elastic scattering setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {'off', 'on'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class NescatBuilder:
    """
    Builds ``Nescat``.

    Attributes:
        setting: Nuclear elastic scattering setting.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``NescatBuilder`` into ``Nescat``.

        Returns:
            ``Nescat`` for ``NescatBuilder``.
        """

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Nescat(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Nescat):
        """
        Unbuilds ``Nescat`` into ``NescatBuilder``

        Returns:
            ``NescatBuilder`` for ``Nescat``.
        """

        return Nescat(
            setting=copy.deepcopy(ast.setting),
        )
