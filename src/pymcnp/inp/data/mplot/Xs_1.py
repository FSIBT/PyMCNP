import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Xs_1(MplotOption):
    """
    Represents INP xs variation #1 elements.

    Attributes:
        m: Material ZAID.
    """

    _ATTRS = {
        'm': types.Zaid,
    }

    _REGEX = re.compile(rf'\Axs( {types.Zaid._REGEX.pattern})\Z')

    def __init__(self, m: types.Zaid):
        """
        Initializes ``Xs_1``.

        Parameters:
            m: Material ZAID.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if m is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, m)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                m,
            ]
        )

        self.m: typing.Final[types.Zaid] = m


@dataclasses.dataclass
class XsBuilder_1:
    """
    Builds ``Xs_1``.

    Attributes:
        m: Material ZAID.
    """

    m: str | types.Zaid

    def build(self):
        """
        Builds ``XsBuilder_1`` into ``Xs_1``.

        Returns:
            ``Xs_1`` for ``XsBuilder_1``.
        """

        if isinstance(self.m, types.Zaid):
            m = self.m
        elif isinstance(self.m, str):
            m = types.Zaid.from_mcnp(self.m)

        return Xs_1(
            m=m,
        )
