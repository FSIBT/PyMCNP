import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class M_1(DataOption):
    """
    Represents INP m variation #1 elements.

    Attributes:
        suffix: Data card option suffix.
        abx: Material library.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'abx': types.String,
    }

    _REGEX = re.compile(rf'\Am(\d+)( {types.String._REGEX.pattern})\Z')

    def __init__(self, suffix: types.Integer, abx: types.String):
        """
        Initializes ``M_1``.

        Parameters:
            suffix: Data card option suffix.
            abx: Material library.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if abx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, abx)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                abx,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.abx: typing.Final[types.String] = abx


@dataclasses.dataclass
class MBuilder_1:
    """
    Builds ``M_1``.

    Attributes:
        suffix: Data card option suffix.
        abx: Material library.
    """

    suffix: str | int | types.Integer
    abx: str | types.String

    def build(self):
        """
        Builds ``MBuilder_1`` into ``M_1``.

        Returns:
            ``M_1`` for ``MBuilder_1``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        abx = self.abx
        if isinstance(self.abx, types.String):
            abx = self.abx
        elif isinstance(self.abx, str):
            abx = types.String.from_mcnp(self.abx)

        return M_1(
            suffix=suffix,
            abx=abx,
        )
