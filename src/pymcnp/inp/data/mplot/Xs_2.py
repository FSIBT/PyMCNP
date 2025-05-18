import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Xs_2(MplotOption):
    """
    Represents INP xs variation #2 elements.

    Attributes:
        m: Material question mark.
    """

    _ATTRS = {
        'm': types.String,
    }

    _REGEX = re.compile(rf'\Axs( {types.String._REGEX.pattern})\Z')

    def __init__(self, m: types.String):
        """
        Initializes ``Xs_2``.

        Parameters:
            m: Material question mark.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if m is None or not (m == '?'):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, m)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                m,
            ]
        )

        self.m: typing.Final[types.String] = m


@dataclasses.dataclass
class XsBuilder_2:
    """
    Builds ``Xs_2``.

    Attributes:
        m: Material question mark.
    """

    m: str | types.String

    def build(self):
        """
        Builds ``XsBuilder_2`` into ``Xs_2``.

        Returns:
            ``Xs_2`` for ``XsBuilder_2``.
        """

        m = self.m
        if isinstance(self.m, types.String):
            m = self.m
        elif isinstance(self.m, str):
            m = types.String.from_mcnp(self.m)

        return Xs_2(
            m=m,
        )
