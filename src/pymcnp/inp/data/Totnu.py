import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Totnu(DataOption):
    """
    Represents INP totnu elements.

    Attributes:
        no: Delay fission sampling on/off.
    """

    _ATTRS = {
        'no': types.String,
    }

    _REGEX = re.compile(rf'\Atotnu( {types.String._REGEX.pattern})?\Z')

    def __init__(self, no: types.String = None):
        """
        Initializes ``Totnu``.

        Parameters:
            no: Delay fission sampling on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if no is not None and not (no == 'no'):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, no)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                no,
            ]
        )

        self.no: typing.Final[types.String] = no


@dataclasses.dataclass
class TotnuBuilder:
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
