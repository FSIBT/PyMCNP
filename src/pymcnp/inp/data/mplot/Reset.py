import re
import copy
import typing
import dataclasses


from . import _option
from ....utils import types
from ....utils import errors


class Reset(_option.MplotOption):
    """
    Represents INP reset elements.

    Attributes:
        aa: Command parameter reset.
    """

    _KEYWORD = 'reset'

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(r'\Areset(?: (all|coplot))?\Z')

    def __init__(self, aa: types.String = None):
        """
        Initializes ``Reset``.

        Parameters:
            aa: Command parameter reset.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if aa is not None and aa not in {'all', 'coplot'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                aa,
            ]
        )

        self.aa: typing.Final[types.String] = aa


@dataclasses.dataclass
class ResetBuilder(_option.MplotOptionBuilder):
    """
    Builds ``Reset``.

    Attributes:
        aa: Command parameter reset.
    """

    aa: str | types.String = None

    def build(self):
        """
        Builds ``ResetBuilder`` into ``Reset``.

        Returns:
            ``Reset`` for ``ResetBuilder``.
        """

        aa = self.aa
        if isinstance(self.aa, types.String):
            aa = self.aa
        elif isinstance(self.aa, str):
            aa = types.String.from_mcnp(self.aa)

        return Reset(
            aa=aa,
        )

    @staticmethod
    def unbuild(ast: Reset):
        """
        Unbuilds ``Reset`` into ``ResetBuilder``

        Returns:
            ``ResetBuilder`` for ``Reset``.
        """

        return ResetBuilder(
            aa=copy.deepcopy(ast.aa),
        )
