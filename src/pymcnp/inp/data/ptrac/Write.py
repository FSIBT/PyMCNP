import re
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Write(PtracOption, keyword='write'):
    """
    Represents INP write elements.

    Attributes:
        setting: Controls what particle parameters are written.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Awrite( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Write``.

        Parameters:
            setting: Controls what particle parameters are written.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if setting is None or setting not in {'pos', 'all'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class WriteBuilder:
    """
    Builds ``Write``.

    Attributes:
        setting: Controls what particle parameters are written.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``WriteBuilder`` into ``Write``.

        Returns:
            ``Write`` for ``WriteBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Write(
            setting=setting,
        )
