import re
import typing
import dataclasses


from ._option import MplotOption
from ....utils import types
from ....utils import errors


class Xtitle(MplotOption, keyword='xtitle'):
    """
    Represents INP xtitle elements.

    Attributes:
        aa: Line to substitute.
    """

    _ATTRS = {
        'aa': types.String,
    }

    _REGEX = re.compile(rf'\Axtitle( \"{types.String._REGEX.pattern}\")\Z')

    def __init__(self, aa: types.String):
        """
        Initializes ``Xtitle``.

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
class XtitleBuilder:
    """
    Builds ``Xtitle``.

    Attributes:
        aa: Line to substitute.
    """

    aa: str | types.String

    def build(self):
        """
        Builds ``XtitleBuilder`` into ``Xtitle``.

        Returns:
            ``Xtitle`` for ``XtitleBuilder``.
        """

        if isinstance(self.aa, types.String):
            aa = self.aa
        elif isinstance(self.aa, str):
            aa = types.String.from_mcnp(self.aa)

        return Xtitle(
            aa=aa,
        )
