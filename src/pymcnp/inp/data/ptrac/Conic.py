import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Conic(_option.PtracOption):
    """
    Represents INP conic elements.

    Attributes:
        setting: Activates a PTRAC file format specifically for coincidence tally scoring.
    """

    _KEYWORD = 'conic'

    _ATTRS = {
        'setting': types.String,
    }

    _REGEX = re.compile(r'\Aconic(?: (col|lin))\Z')

    def __init__(self, setting: types.String):
        """
        Initializes ``Conic``.

        Parameters:
            setting: Activates a PTRAC file format specifically for coincidence tally scoring.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if setting is None or setting.value not in {'col', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, setting)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                setting,
            ]
        )

        self.setting: typing.Final[types.String] = setting


@dataclasses.dataclass
class ConicBuilder(_option.PtracOptionBuilder):
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

        setting = self.setting
        if isinstance(self.setting, types.String):
            setting = self.setting
        elif isinstance(self.setting, str):
            setting = types.String.from_mcnp(self.setting)

        return Conic(
            setting=setting,
        )

    @staticmethod
    def unbuild(ast: Conic):
        """
        Unbuilds ``Conic`` into ``ConicBuilder``

        Returns:
            ``ConicBuilder`` for ``Conic``.
        """

        return ConicBuilder(
            setting=copy.deepcopy(ast.setting),
        )
