import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Fm(DataOption):
    """
    Represents INP fm elements.

    Attributes:
        suffix: Data card option suffix.
        bins: Tally multiplier bins.
    """

    _KEYWORD = 'fm'

    _ATTRS = {
        'suffix': types.Integer,
        'bins': types.String,
    }

    _REGEX = re.compile(r'\Afm(\d+)( [\S\s]+)\Z')

    def __init__(self, suffix: types.Integer, bins: types.String):
        """
        Initializes ``Fm``.

        Parameters:
            suffix: Data card option suffix.
            bins: Tally multiplier bins.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if suffix is None or not (suffix.value <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if bins is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, bins)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bins,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.bins: typing.Final[types.String] = bins


@dataclasses.dataclass
class FmBuilder:
    """
    Builds ``Fm``.

    Attributes:
        suffix: Data card option suffix.
        bins: Tally multiplier bins.
    """

    suffix: str | int | types.Integer
    bins: str | types.String

    def build(self):
        """
        Builds ``FmBuilder`` into ``Fm``.

        Returns:
            ``Fm`` for ``FmBuilder``.
        """

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        bins = self.bins
        if isinstance(self.bins, types.String):
            bins = self.bins
        elif isinstance(self.bins, str):
            bins = types.String.from_mcnp(self.bins)

        return Fm(
            suffix=suffix,
            bins=bins,
        )

    @staticmethod
    def unbuild(ast: Fm):
        """
        Unbuilds ``Fm`` into ``FmBuilder``

        Returns:
            ``FmBuilder`` for ``Fm``.
        """

        return Fm(
            suffix=copy.deepcopy(ast.suffix),
            bins=copy.deepcopy(ast.bins),
        )
