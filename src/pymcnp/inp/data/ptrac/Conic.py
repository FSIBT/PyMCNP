import re
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Conic(PtracOption, keyword='conic'):
    """
    Represents INP conic elements.

    Attributes:
        setting: Activates a PTRAC file format specifically for coincidence tally scoring.
    """

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(rf'\Aconic( {types.String._REGEX.pattern})\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Conic``.

        Parameters:
            setting: Activates a PTRAC file format specifically for coincidence tally scoring.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting not in {'col', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class ConicBuilder:
    """
    Builds ``Conic``.

    Attributes:
        setting: Activates a PTRAC file format specifically for coincidence tally scoring.
    """

    setting: str | types.String

    def build(self):
        """
        Builds ``ConicBuilder`` into ``Conic``.

        Returns:
            ``Conic`` for ``ConicBuilder``.
        """

        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Conic(
            setting=setting,
        )
