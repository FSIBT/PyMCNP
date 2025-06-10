import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Xs_2(_option.MplotOption):
    """
    Represents INP xs variation #2 elements.

    Attributes:
        m: Material question mark.
    """

    _KEYWORD = 'xs'

    _ATTRS = {
        'm': types.String,
    }

    _REGEX = re.compile(rf'\Axs( {types.String._REGEX.pattern[2:-2]})\Z')

    def __init__(self, m: types.String):
        """
        Initializes ``Xs_2``.

        Parameters:
            m: Material question mark.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if m is None or not (m.value == '?'):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, m)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                m,
            ]
        )

        self.m: typing.Final[types.String] = m


@dataclasses.dataclass
class XsBuilder_2(_option.MplotOptionBuilder):
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

    @staticmethod
    def unbuild(ast: Xs_2):
        """
        Unbuilds ``Xs_2`` into ``XsBuilder_2``

        Returns:
            ``XsBuilder_2`` for ``Xs_2``.
        """

        return XsBuilder_2(
            m=copy.deepcopy(ast.m),
        )
