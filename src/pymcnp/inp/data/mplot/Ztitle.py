import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Ztitle(MplotOption):
    """
    Represents INP ztitle elements.

    Attributes:
        aa: Line to substitute.
    """

    _KEYWORD = 'ztitle'

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Aztitle( \"{types.String._REGEX.pattern}\")\Z')

    def __init__(self, aa: types.String):
        """
        Initializes ``Ztitle``.

        Parameters:
            aa: Line to substitute.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if aa is None or not (len(aa) <= 40):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, aa)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                aa,
            ]
        )

        self.aa: typing.Final[types.String] = aa


@dataclasses.dataclass
class ZtitleBuilder:
    """
    Builds ``Ztitle``.

    Attributes:
        aa: Line to substitute.
    """

    aa: str | types.String

    def build(self):
        """
        Builds ``ZtitleBuilder`` into ``Ztitle``.

        Returns:
            ``Ztitle`` for ``ZtitleBuilder``.
        """

        aa = self.aa
        if isinstance(self.aa, types.String):
            aa = self.aa
        elif isinstance(self.aa, str):
            aa = types.String.from_mcnp(self.aa)

        return Ztitle(
            aa=aa,
        )

    @staticmethod
    def unbuild(ast: Ztitle):
        """
        Unbuilds ``Ztitle`` into ``ZtitleBuilder``

        Returns:
            ``ZtitleBuilder`` for ``Ztitle``.
        """

        return Ztitle(
            aa=copy.deepcopy(ast.aa),
        )
