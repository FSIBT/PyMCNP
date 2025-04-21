import re
import typing
import dataclasses


from ._option import Df_1Option
from ....utils import types
from ....utils import errors


class Int(Df_1Option, keyword='int'):
    """
    Represents INP int elements.

    Attributes:
        interpolation: Energy interpolation.
    """

    _ATTRS = {
        'interpolation': types.String,
    }

    _REGEX = re.compile(rf'\Aint( {types.String._REGEX.pattern})\Z')

    def __init__(self, interpolation: types.String):
        """
        Initializes ``Int``.

        Parameters:
            interpolation: Energy interpolation.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if interpolation is None or interpolation not in {'log', 'lin'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, interpolation)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                interpolation,
            ]
        )

        self.interpolation: typing.Final[types.String] = interpolation


@dataclasses.dataclass
class IntBuilder:
    """
    Builds ``Int``.

    Attributes:
        interpolation: Energy interpolation.
    """

    interpolation: str | types.String

    def build(self):
        """
        Builds ``IntBuilder`` into ``Int``.

        Returns:
            ``Int`` for ``IntBuilder``.
        """

        if isinstance(self.interpolation, types.String):
            interpolation = self.interpolation
        elif isinstance(self.interpolation, str):
            interpolation = types.String.from_mcnp(self.interpolation)

        return Int(
            interpolation=interpolation,
        )
