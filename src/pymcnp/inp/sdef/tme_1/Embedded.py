import re

from . import _entry
from .... import types
from .... import errors


class Embedded(_entry.TmeEntry_1):
    """
    Represents INP embedded distribution entries.

    Attributes:
        distributions: Distribution distributions.
    """

    _REGEX = re.compile(rf'\A({types.Distribution._REGEX.pattern[2:-2]}(?: ?< ?{types.Distribution._REGEX.pattern[2:-2]})*)\Z', re.IGNORECASE)

    def __init__(self, distributions: types.Tuple(types.Distribution)):
        """
        Initializes `Embedded`.

        Parameters:
            distributions: Time distributions.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if distributions is None or None in distributions:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, distributions)

        self.distributions: types.Tuple(types.Distribution) = distributions

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Embedded` from MCNP.

        Parameters:
            source: MCNP for `Embedded`.

        Returns:
            `Embedded` object.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Embedded._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        distributions = types.Tuple(types.Distribution).from_mcnp(' '.join(source.split('<')))

        return Embedded(distributions)

    def to_mcnp(self):
        """
        Generates MCNP from `Embedded`.

        Returns:
            MCNP for `Embedded`.
        """

        return '<'.join(number.to_mcnp() for number in self.distributions)
