import re

from . import _card
from .. import types
from .. import errors


class Cut(_card.Card):
    """
    Represents INP cut cards.
    """

    _KEYWORD = 'cut'

    _ATTRS = {
        'designator': types.Designator,
        'time_cutoff': types.Real,
        'energy_cutoff': types.Real,
        'weight_cutoff1': types.Real,
        'weight_cutoff2': types.Real,
        'source_weight': types.Real,
    }

    _REGEX = re.compile(
        rf'\Acut:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        designator: str | types.Designator,
        time_cutoff: str | int | float | types.Real = None,
        energy_cutoff: str | int | float | types.Real = None,
        weight_cutoff1: str | int | float | types.Real = None,
        weight_cutoff2: str | int | float | types.Real = None,
        source_weight: str | int | float | types.Real = None,
    ):
        """
        Initializes `Cut`.

        Parameters:
            designator: Data option particle designator.
            time_cutoff: Time cutoff in shakes.
            energy_cutoff: Lower energy cutoff.
            weight_cutoff1: Weight cutoff #1.
            weight_cutoff2: Weight cutoff #2.
            source_weight: Minimum source weight.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.designator: types.Designator = designator
        self.time_cutoff: types.Real = time_cutoff
        self.energy_cutoff: types.Real = energy_cutoff
        self.weight_cutoff1: types.Real = weight_cutoff1
        self.weight_cutoff2: types.Real = weight_cutoff2
        self.source_weight: types.Real = source_weight

    @property
    def designator(self) -> types.Designator:
        """
        Data option particle designator

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._designator

    @designator.setter
    def designator(self, designator: str | types.Designator) -> None:
        """
        Sets `designator`.

        Parameters:
            designator: Data option particle designator.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if designator is not None:
            if isinstance(designator, types.Designator):
                designator = designator
            elif isinstance(designator, str):
                designator = types.Designator.from_mcnp(designator)

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, designator)

        self._designator: types.Designator = designator

    @property
    def time_cutoff(self) -> types.Real:
        """
        Time cutoff in shakes

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_cutoff

    @time_cutoff.setter
    def time_cutoff(self, time_cutoff: str | int | float | types.Real) -> None:
        """
        Sets `time_cutoff`.

        Parameters:
            time_cutoff: Time cutoff in shakes.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_cutoff is not None:
            if isinstance(time_cutoff, types.Real):
                time_cutoff = time_cutoff
            elif isinstance(time_cutoff, int) or isinstance(time_cutoff, float):
                time_cutoff = types.Real(time_cutoff)
            elif isinstance(time_cutoff, str):
                time_cutoff = types.Real.from_mcnp(time_cutoff)

        self._time_cutoff: types.Real = time_cutoff

    @property
    def energy_cutoff(self) -> types.Real:
        """
        Lower energy cutoff

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_cutoff

    @energy_cutoff.setter
    def energy_cutoff(self, energy_cutoff: str | int | float | types.Real) -> None:
        """
        Sets `energy_cutoff`.

        Parameters:
            energy_cutoff: Lower energy cutoff.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_cutoff is not None:
            if isinstance(energy_cutoff, types.Real):
                energy_cutoff = energy_cutoff
            elif isinstance(energy_cutoff, int) or isinstance(energy_cutoff, float):
                energy_cutoff = types.Real(energy_cutoff)
            elif isinstance(energy_cutoff, str):
                energy_cutoff = types.Real.from_mcnp(energy_cutoff)

        self._energy_cutoff: types.Real = energy_cutoff

    @property
    def weight_cutoff1(self) -> types.Real:
        """
        Weight cutoff #1

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._weight_cutoff1

    @weight_cutoff1.setter
    def weight_cutoff1(self, weight_cutoff1: str | int | float | types.Real) -> None:
        """
        Sets `weight_cutoff1`.

        Parameters:
            weight_cutoff1: Weight cutoff #1.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if weight_cutoff1 is not None:
            if isinstance(weight_cutoff1, types.Real):
                weight_cutoff1 = weight_cutoff1
            elif isinstance(weight_cutoff1, int) or isinstance(weight_cutoff1, float):
                weight_cutoff1 = types.Real(weight_cutoff1)
            elif isinstance(weight_cutoff1, str):
                weight_cutoff1 = types.Real.from_mcnp(weight_cutoff1)

        self._weight_cutoff1: types.Real = weight_cutoff1

    @property
    def weight_cutoff2(self) -> types.Real:
        """
        Weight cutoff #2

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._weight_cutoff2

    @weight_cutoff2.setter
    def weight_cutoff2(self, weight_cutoff2: str | int | float | types.Real) -> None:
        """
        Sets `weight_cutoff2`.

        Parameters:
            weight_cutoff2: Weight cutoff #2.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if weight_cutoff2 is not None:
            if isinstance(weight_cutoff2, types.Real):
                weight_cutoff2 = weight_cutoff2
            elif isinstance(weight_cutoff2, int) or isinstance(weight_cutoff2, float):
                weight_cutoff2 = types.Real(weight_cutoff2)
            elif isinstance(weight_cutoff2, str):
                weight_cutoff2 = types.Real.from_mcnp(weight_cutoff2)

        self._weight_cutoff2: types.Real = weight_cutoff2

    @property
    def source_weight(self) -> types.Real:
        """
        Minimum source weight

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._source_weight

    @source_weight.setter
    def source_weight(self, source_weight: str | int | float | types.Real) -> None:
        """
        Sets `source_weight`.

        Parameters:
            source_weight: Minimum source weight.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if source_weight is not None:
            if isinstance(source_weight, types.Real):
                source_weight = source_weight
            elif isinstance(source_weight, int) or isinstance(source_weight, float):
                source_weight = types.Real(source_weight)
            elif isinstance(source_weight, str):
                source_weight = types.Real.from_mcnp(source_weight)

        self._source_weight: types.Real = source_weight
