import re
import typing
import dataclasses


from ._option import RandOption
from ....utils import types
from ....utils import errors


class Hist(RandOption, keyword='hist'):
    """
    Represents INP hist elements.

    Attributes:
        hist: Starting pseudorandom number.
    """

    _ATTRS = {
        'hist': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Ahist( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, hist: types.IntegerOrJump):
        """
        Initializes ``Hist``.

        Parameters:
            hist: Starting pseudorandom number.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if hist is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, hist)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                hist,
            ]
        )

        self.hist: typing.Final[types.IntegerOrJump] = hist


@dataclasses.dataclass
class HistBuilder:
    """
    Builds ``Hist``.

    Attributes:
        hist: Starting pseudorandom number.
    """

    hist: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``HistBuilder`` into ``Hist``.

        Returns:
            ``Hist`` for ``HistBuilder``.
        """

        if isinstance(self.hist, types.Integer):
            hist = self.hist
        elif isinstance(self.hist, int):
            hist = types.IntegerOrJump(self.hist)
        elif isinstance(self.hist, str):
            hist = types.IntegerOrJump.from_mcnp(self.hist)

        return Hist(
            hist=hist,
        )
