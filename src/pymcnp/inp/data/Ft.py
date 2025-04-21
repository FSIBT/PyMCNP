import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Ft(DataOption, keyword='ft'):
    """
    Represents INP ft elements.

    Attributes:
        suffix: Data card option suffix.
        treatments: Tally special treatments.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'treatments': types.String,
    }

    _REGEX = re.compile(r'\Aft(\d+)( [\S\s]+)\Z')

    def __init__(self, suffix: types.Integer, treatments: types.String):
        """
        Initializes ``Ft``.

        Parameters:
            suffix: Data card option suffix.
            treatments: Tally special treatments.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if treatments is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, treatments)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                treatments,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.treatments: typing.Final[types.String] = treatments


@dataclasses.dataclass
class FtBuilder:
    """
    Builds ``Ft``.

    Attributes:
        suffix: Data card option suffix.
        treatments: Tally special treatments.
    """

    suffix: str | int | types.Integer
    treatments: str | types.String

    def build(self):
        """
        Builds ``FtBuilder`` into ``Ft``.

        Returns:
            ``Ft`` for ``FtBuilder``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.treatments, types.String):
            treatments = self.treatments
        elif isinstance(self.treatments, str):
            treatments = types.String.from_mcnp(self.treatments)

        return Ft(
            suffix=suffix,
            treatments=treatments,
        )
