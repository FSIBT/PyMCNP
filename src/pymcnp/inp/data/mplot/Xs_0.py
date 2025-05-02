import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Xs_0(MplotOption):
    """
    Represents INP xs variation #0 elements.

    Attributes:
        m: Material number.
    """

    _ATTRS = {
        'm': types.Integer,
    }

    _REGEX = re.compile(rf'\Axs( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, m: types.Integer):
        """
        Initializes ``Xs_0``.

        Parameters:
            m: Material number.

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

        self.m: typing.Final[types.Integer] = m


@dataclasses.dataclass
class XsBuilder_0:
    """
    Builds ``Xs_0``.

    Attributes:
        m: Material number.
    """

    m: str | int | types.Integer

    def build(self):
        """
        Builds ``XsBuilder_0`` into ``Xs_0``.

        Returns:
            ``Xs_0`` for ``XsBuilder_0``.
        """

        if isinstance(self.m, types.Integer):
            m = self.m
        elif isinstance(self.m, int):
            m = types.Integer(self.m)
        elif isinstance(self.m, str):
            m = types.Integer.from_mcnp(self.m)

        return Xs_0(
            m=m,
        )
