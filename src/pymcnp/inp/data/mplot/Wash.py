import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Wash(MplotOption):
    """
    Represents INP wash elements.

    Attributes:
        aa: Color-wash on/offs.
    """

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Awash( {types.String._REGEX.pattern})\Z')

    def __init__(self, aa: types.String):
        """
        Initializes ``Wash``.

        Parameters:
            aa: Color-wash on/offs.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if aa is None or aa not in {'on', 'off'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                aa,
            ]
        )

        self.aa: typing.Final[types.String] = aa


@dataclasses.dataclass
class WashBuilder:
    """
    Builds ``Wash``.

    Attributes:
        aa: Color-wash on/offs.
    """

    aa: str | types.String

    def build(self):
        """
        Builds ``WashBuilder`` into ``Wash``.

        Returns:
            ``Wash`` for ``WashBuilder``.
        """

        aa = self.aa
        if isinstance(self.aa, types.String):
            aa = self.aa
        elif isinstance(self.aa, str):
            aa = types.String.from_mcnp(self.aa)

        return Wash(
            aa=aa,
        )
