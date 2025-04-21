import re
import typing
import dataclasses


from ._option import BlockOption
from .....utils import types
from .....utils import errors


class Srcacc(BlockOption, keyword='srcacc'):
    """
    Represents INP srcacc elements.

    Attributes:
        setting: Transport accelerations.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Asrcacc( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Srcacc``.

        Parameters:
            setting: Transport accelerations.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'dsa', 'tsa', 'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class SrcaccBuilder:
    """
    Builds ``Srcacc``.

    Attributes:
        setting: Transport accelerations.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``SrcaccBuilder`` into ``Srcacc``.

        Returns:
            ``Srcacc`` for ``SrcaccBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Srcacc(
            setting=setting,
        )
