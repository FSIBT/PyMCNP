import re

from . import _option
from ... import types
from ... import errors


class Dxc(_option.LikeOption):
    """
    Represents INP `dxc` elements.
    """

    _KEYWORD = 'dxc'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'probability': types.Real,
    }

    _REGEX = re.compile(rf'\Adxc(\d+):(\S+)( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, suffix: str | int | types.Integer, designator: str | types.Designator, probability: str | int | float | types.Real):
        """
        Initializes `Dxc`.

        Parameters:
            suffix: Cell option suffix.
            designator: Cell particle designator.
            probability: Cell probability of DXTRAN contribution.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.designator: types.Designator = designator
        self.probability: types.Real = probability

    @property
    def suffix(self) -> types.Integer:
        """
        Gets `suffix`.

        Returns:
            `suffix`.
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Cell option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def designator(self) -> types.Designator:
        """
        Gets `designator`.

        Returns:
            `designator`.
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets `designator`.

        Parameters:
            designator: Cell particle designator.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)

        self._designator: types.Designator = designator

    @property
    def probability(self) -> types.Real:
        """
        Gets `probability`.

        Returns:
            `probability`.
        """

        return self._probability

    @probability.setter
    def probability(self, probability: str | int | float | types.Real) -> None:
        """
        Sets `probability`.

        Parameters:
            probability: Cell probability of DXTRAN contribution.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if probability is not None:
            if isinstance(probability, types.Real):
                probability = probability
            elif isinstance(probability, int) or isinstance(probability, float):
                probability = types.Real(probability)
            elif isinstance(probability, str):
                probability = types.Real.from_mcnp(probability)

        if probability is None or not (probability >= 0 and probability <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, probability)

        self._probability: types.Real = probability
