import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Label(MplotOption):
    """
    Represents INP label elements.

    Attributes:
        aa: Line to substitute.
    """

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Alabel( \"{types.String._REGEX.pattern}\")\Z')

    def __init__(self, aa: types.String):
        """
        Initializes ``Label``.

        Parameters:
            aa: Line to substitute.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if aa is None or not (len(aa) <= 10):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                aa,
            ]
        )

        self.aa: typing.Final[types.String] = aa


@dataclasses.dataclass
class LabelBuilder:
    """
    Builds ``Label``.

    Attributes:
        aa: Line to substitute.
    """

    aa: str | types.String

    def build(self):
        """
        Builds ``LabelBuilder`` into ``Label``.

        Returns:
            ``Label`` for ``LabelBuilder``.
        """

        aa = self.aa
        if isinstance(self.aa, types.String):
            aa = self.aa
        elif isinstance(self.aa, str):
            aa = types.String.from_mcnp(self.aa)

        return Label(
            aa=aa,
        )
