import re
import typing
import dataclasses


from .option_ import BlockOption_
from .....utils import types
from .....utils import errors


class Trcor(BlockOption_, keyword='trcor'):
    """
    Represents INP trcor elements.

    Attributes:
        setting: Trcor.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Atrcor( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Trcor``.

        Parameters:
            setting: Trcor.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'diag'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class TrcorBuilder:
    """
    Builds ``Trcor``.

    Attributes:
        setting: Trcor.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``TrcorBuilder`` into ``Trcor``.

        Returns:
            ``Trcor`` for ``TrcorBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Trcor(
            setting=setting,
        )
