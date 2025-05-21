import re
import copy
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Ytitle(MplotOption):
    """
    Represents INP ytitle elements.

    Attributes:
        aa: Line to substitute.
    """

    _KEYWORD = 'ytitle'

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Aytitle( \"{types.String._REGEX.pattern}\")\Z')

    def __init__(self, aa: types.String):
        """
        Initializes ``Ytitle``.

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
class YtitleBuilder:
    """
    Builds ``Ytitle``.

    Attributes:
        aa: Line to substitute.
    """

    aa: str | types.String

    def build(self):
        """
        Builds ``YtitleBuilder`` into ``Ytitle``.

        Returns:
            ``Ytitle`` for ``YtitleBuilder``.
        """

        aa = self.aa
        if isinstance(self.aa, types.String):
            aa = self.aa
        elif isinstance(self.aa, str):
            aa = types.String.from_mcnp(self.aa)

        return Ytitle(
            aa=aa,
        )

    @staticmethod
    def unbuild(ast: Ytitle):
        """
        Unbuilds ``Ytitle`` into ``YtitleBuilder``

        Returns:
            ``YtitleBuilder`` for ``Ytitle``.
        """

        return Ytitle(
            aa=copy.deepcopy(ast.aa),
        )
