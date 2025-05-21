import re
import copy
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

    _KEYWORD = 'xs'

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

        m = self.m
        if isinstance(self.m, types.Integer):
            m = self.m
        elif isinstance(self.m, int):
            m = types.Integer(self.m)
        elif isinstance(self.m, str):
            m = types.Integer.from_mcnp(self.m)

        return Xs_0(
            m=m,
        )

    @staticmethod
    def unbuild(ast: Xs_0):
        """
        Unbuilds ``Xs_0`` into ``XsBuilder_0``

        Returns:
            ``XsBuilder_0`` for ``Xs_0``.
        """

        return Xs_0(
            m=copy.deepcopy(ast.m),
        )
