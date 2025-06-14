import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Totnu(_option.DataOption):
    """
    Represents INP totnu elements.

    Attributes:
        no: Delay fission sampling on/off.
    """

    _KEYWORD = 'totnu'

    _ATTRS = {
        'no': types.String,
    }

    _REGEX = re.compile(rf'\Atotnu( {types.String._REGEX.pattern[2:-2]})?\Z')

    def __init__(self, no: types.String = None):
        """
        Initializes ``Totnu``.

        Parameters:
            no: Delay fission sampling on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if no is not None and not (no.value == 'no'):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, no)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                no,
            ]
        )

        self.no: typing.Final[types.String] = no


@dataclasses.dataclass
class TotnuBuilder(_option.DataOptionBuilder):
    """
    Builds ``Totnu``.

    Attributes:
        no: Delay fission sampling on/off.
    """

    no: str | types.String = None

    def build(self):
        """
        Builds ``TotnuBuilder`` into ``Totnu``.

        Returns:
            ``Totnu`` for ``TotnuBuilder``.
        """

        no = self.no
        if isinstance(self.no, types.String):
            no = self.no
        elif isinstance(self.no, str):
            no = types.String.from_mcnp(self.no)

        return Totnu(
            no=no,
        )

    @staticmethod
    def unbuild(ast: Totnu):
        """
        Unbuilds ``Totnu`` into ``TotnuBuilder``

        Returns:
            ``TotnuBuilder`` for ``Totnu``.
        """

        return TotnuBuilder(
            no=copy.deepcopy(ast.no),
        )
