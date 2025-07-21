import re

from . import _option
from ... import types
from ... import errors


class Pd(_option.DataOption):
    """
    Represents INP pd elements.
    """

    _KEYWORD = 'pd'

    _ATTRS = {
        'suffix': types.Integer,
        'designator': types.Designator,
        'probabilities': types.Tuple(types.Real),
    }

    _REGEX = re.compile(rf'\Apd(\d+):(\S+)((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, suffix: str | int | types.Integer, designator: str | types.Designator, probabilities: list[str] | list[float] | list[types.Real]):
        """
        Initializes ``Pd``.

        Parameters:
            suffix: Data card option suffix.
            designator: Data card particle designator.
            probabilities: Probability of contribution to DXTRAN.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.suffix: types.Integer = suffix
        self.designator: types.Designator = designator
        self.probabilities: types.Tuple(types.Real) = probabilities

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

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

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def designator(self) -> types.Designator:
        """
        Data card particle designator

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets ``designator``.

        Parameters:
            designator: Data card particle designator.

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
    def probabilities(self) -> types.Tuple(types.Real):
        """
        Probability of contribution to DXTRAN

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._probabilities

    @probabilities.setter
    def probabilities(self, probabilities: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``probabilities``.

        Parameters:
            probabilities: Probability of contribution to DXTRAN.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if probabilities is not None:
            array = []
            for item in probabilities:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int) or isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
            probabilities = types.Tuple(types.Real)(array)

        if probabilities is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, probabilities)

        self._probabilities: types.Tuple(types.Real) = probabilities
