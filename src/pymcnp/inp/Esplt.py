import re

from . import _card
from .. import types
from .. import errors


class Esplt(_card.Card):
    """
    Represents INP `esplt` cards.
    """

    _KEYWORD = 'esplt'

    _ATTRS = {
        'designator': types.Designator,
        'ratio_1': types.Real,
        'energy_1': types.Real,
        'ratio_2': types.Real,
        'energy_2': types.Real,
        'ratio_3': types.Real,
        'energy_3': types.Real,
        'ratio_4': types.Real,
        'energy_4': types.Real,
        'ratio_5': types.Real,
        'energy_5': types.Real,
        'ratio_6': types.Real,
        'energy_6': types.Real,
        'ratio_7': types.Real,
        'energy_7': types.Real,
        'ratio_8': types.Real,
        'energy_8': types.Real,
        'ratio_9': types.Real,
        'energy_9': types.Real,
        'ratio_10': types.Real,
        'energy_10': types.Real,
        'ratio_11': types.Real,
        'energy_11': types.Real,
        'ratio_12': types.Real,
        'energy_12': types.Real,
        'ratio_13': types.Real,
        'energy_13': types.Real,
        'ratio_14': types.Real,
        'energy_14': types.Real,
        'ratio_15': types.Real,
        'energy_15': types.Real,
        'ratio_16': types.Real,
        'energy_16': types.Real,
        'ratio_17': types.Real,
        'energy_17': types.Real,
        'ratio_18': types.Real,
        'energy_18': types.Real,
        'ratio_19': types.Real,
        'energy_19': types.Real,
        'ratio_20': types.Real,
        'energy_20': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aesplt:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        designator: str | types.Designator,
        ratio_1: str | int | float | types.Real = None,
        energy_1: str | int | float | types.Real = None,
        ratio_2: str | int | float | types.Real = None,
        energy_2: str | int | float | types.Real = None,
        ratio_3: str | int | float | types.Real = None,
        energy_3: str | int | float | types.Real = None,
        ratio_4: str | int | float | types.Real = None,
        energy_4: str | int | float | types.Real = None,
        ratio_5: str | int | float | types.Real = None,
        energy_5: str | int | float | types.Real = None,
        ratio_6: str | int | float | types.Real = None,
        energy_6: str | int | float | types.Real = None,
        ratio_7: str | int | float | types.Real = None,
        energy_7: str | int | float | types.Real = None,
        ratio_8: str | int | float | types.Real = None,
        energy_8: str | int | float | types.Real = None,
        ratio_9: str | int | float | types.Real = None,
        energy_9: str | int | float | types.Real = None,
        ratio_10: str | int | float | types.Real = None,
        energy_10: str | int | float | types.Real = None,
        ratio_11: str | int | float | types.Real = None,
        energy_11: str | int | float | types.Real = None,
        ratio_12: str | int | float | types.Real = None,
        energy_12: str | int | float | types.Real = None,
        ratio_13: str | int | float | types.Real = None,
        energy_13: str | int | float | types.Real = None,
        ratio_14: str | int | float | types.Real = None,
        energy_14: str | int | float | types.Real = None,
        ratio_15: str | int | float | types.Real = None,
        energy_15: str | int | float | types.Real = None,
        ratio_16: str | int | float | types.Real = None,
        energy_16: str | int | float | types.Real = None,
        ratio_17: str | int | float | types.Real = None,
        energy_17: str | int | float | types.Real = None,
        ratio_18: str | int | float | types.Real = None,
        energy_18: str | int | float | types.Real = None,
        ratio_19: str | int | float | types.Real = None,
        energy_19: str | int | float | types.Real = None,
        ratio_20: str | int | float | types.Real = None,
        energy_20: str | int | float | types.Real = None,
    ):
        """
        Initializes `Esplt`.

        Parameters:
            designator: Data card particle designator.
            ratio_1: Splitting/roulette ratio #1.
            energy_1: Splitting/roulette energy #1.
            ratio_2: Splitting/roulette ratio #2.
            energy_2: Splitting/roulette energy #2.
            ratio_3: Splitting/roulette ratio #3.
            energy_3: Splitting/roulette energy #3.
            ratio_4: Splitting/roulette ratio #4.
            energy_4: Splitting/roulette energy #4.
            ratio_5: Splitting/roulette ratio #5.
            energy_5: Splitting/roulette energy #5.
            ratio_6: Splitting/roulette ratio #6.
            energy_6: Splitting/roulette energy #6.
            ratio_7: Splitting/roulette ratio #7.
            energy_7: Splitting/roulette energy #7.
            ratio_8: Splitting/roulette ratio #8.
            energy_8: Splitting/roulette energy #8.
            ratio_9: Splitting/roulette ratio #9.
            energy_9: Splitting/roulette energy #9.
            ratio_10: Splitting/roulette ratio #10.
            energy_10: Splitting/roulette energy #10.
            ratio_11: Splitting/roulette ratio #11.
            energy_11: Splitting/roulette energy #11.
            ratio_12: Splitting/roulette ratio #12.
            energy_12: Splitting/roulette energy #12.
            ratio_13: Splitting/roulette ratio #13.
            energy_13: Splitting/roulette energy #13.
            ratio_14: Splitting/roulette ratio #14.
            energy_14: Splitting/roulette energy #14.
            ratio_15: Splitting/roulette ratio #15.
            energy_15: Splitting/roulette energy #15.
            ratio_16: Splitting/roulette ratio #16.
            energy_16: Splitting/roulette energy #16.
            ratio_17: Splitting/roulette ratio #17.
            energy_17: Splitting/roulette energy #17.
            ratio_18: Splitting/roulette ratio #18.
            energy_18: Splitting/roulette energy #18.
            ratio_19: Splitting/roulette ratio #19.
            energy_19: Splitting/roulette energy #19.
            ratio_20: Splitting/roulette ratio #20.
            energy_20: Splitting/roulette energy #20.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.designator: types.Designator = designator
        self.ratio_1: types.Real = ratio_1
        self.energy_1: types.Real = energy_1
        self.ratio_2: types.Real = ratio_2
        self.energy_2: types.Real = energy_2
        self.ratio_3: types.Real = ratio_3
        self.energy_3: types.Real = energy_3
        self.ratio_4: types.Real = ratio_4
        self.energy_4: types.Real = energy_4
        self.ratio_5: types.Real = ratio_5
        self.energy_5: types.Real = energy_5
        self.ratio_6: types.Real = ratio_6
        self.energy_6: types.Real = energy_6
        self.ratio_7: types.Real = ratio_7
        self.energy_7: types.Real = energy_7
        self.ratio_8: types.Real = ratio_8
        self.energy_8: types.Real = energy_8
        self.ratio_9: types.Real = ratio_9
        self.energy_9: types.Real = energy_9
        self.ratio_10: types.Real = ratio_10
        self.energy_10: types.Real = energy_10
        self.ratio_11: types.Real = ratio_11
        self.energy_11: types.Real = energy_11
        self.ratio_12: types.Real = ratio_12
        self.energy_12: types.Real = energy_12
        self.ratio_13: types.Real = ratio_13
        self.energy_13: types.Real = energy_13
        self.ratio_14: types.Real = ratio_14
        self.energy_14: types.Real = energy_14
        self.ratio_15: types.Real = ratio_15
        self.energy_15: types.Real = energy_15
        self.ratio_16: types.Real = ratio_16
        self.energy_16: types.Real = energy_16
        self.ratio_17: types.Real = ratio_17
        self.energy_17: types.Real = energy_17
        self.ratio_18: types.Real = ratio_18
        self.energy_18: types.Real = energy_18
        self.ratio_19: types.Real = ratio_19
        self.energy_19: types.Real = energy_19
        self.ratio_20: types.Real = ratio_20
        self.energy_20: types.Real = energy_20

    @property
    def designator(self) -> types.Designator:
        """
        Data card particle designator

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
            designator: Data card particle designator.

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
    def ratio_1(self) -> types.Real:
        """
        Splitting/roulette ratio #1

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_1

    @ratio_1.setter
    def ratio_1(self, ratio_1: str | int | float | types.Real) -> None:
        """
        Sets `ratio_1`.

        Parameters:
            ratio_1: Splitting/roulette ratio #1.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_1 is not None:
            if isinstance(ratio_1, types.Real):
                ratio_1 = ratio_1
            elif isinstance(ratio_1, int) or isinstance(ratio_1, float):
                ratio_1 = types.Real(ratio_1)
            elif isinstance(ratio_1, str):
                ratio_1 = types.Real.from_mcnp(ratio_1)

        self._ratio_1: types.Real = ratio_1

    @property
    def energy_1(self) -> types.Real:
        """
        Splitting/roulette energy #1

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_1

    @energy_1.setter
    def energy_1(self, energy_1: str | int | float | types.Real) -> None:
        """
        Sets `energy_1`.

        Parameters:
            energy_1: Splitting/roulette energy #1.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_1 is not None:
            if isinstance(energy_1, types.Real):
                energy_1 = energy_1
            elif isinstance(energy_1, int) or isinstance(energy_1, float):
                energy_1 = types.Real(energy_1)
            elif isinstance(energy_1, str):
                energy_1 = types.Real.from_mcnp(energy_1)

        self._energy_1: types.Real = energy_1

    @property
    def ratio_2(self) -> types.Real:
        """
        Splitting/roulette ratio #2

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_2

    @ratio_2.setter
    def ratio_2(self, ratio_2: str | int | float | types.Real) -> None:
        """
        Sets `ratio_2`.

        Parameters:
            ratio_2: Splitting/roulette ratio #2.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_2 is not None:
            if isinstance(ratio_2, types.Real):
                ratio_2 = ratio_2
            elif isinstance(ratio_2, int) or isinstance(ratio_2, float):
                ratio_2 = types.Real(ratio_2)
            elif isinstance(ratio_2, str):
                ratio_2 = types.Real.from_mcnp(ratio_2)

        self._ratio_2: types.Real = ratio_2

    @property
    def energy_2(self) -> types.Real:
        """
        Splitting/roulette energy #2

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_2

    @energy_2.setter
    def energy_2(self, energy_2: str | int | float | types.Real) -> None:
        """
        Sets `energy_2`.

        Parameters:
            energy_2: Splitting/roulette energy #2.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_2 is not None:
            if isinstance(energy_2, types.Real):
                energy_2 = energy_2
            elif isinstance(energy_2, int) or isinstance(energy_2, float):
                energy_2 = types.Real(energy_2)
            elif isinstance(energy_2, str):
                energy_2 = types.Real.from_mcnp(energy_2)

        self._energy_2: types.Real = energy_2

    @property
    def ratio_3(self) -> types.Real:
        """
        Splitting/roulette ratio #3

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_3

    @ratio_3.setter
    def ratio_3(self, ratio_3: str | int | float | types.Real) -> None:
        """
        Sets `ratio_3`.

        Parameters:
            ratio_3: Splitting/roulette ratio #3.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_3 is not None:
            if isinstance(ratio_3, types.Real):
                ratio_3 = ratio_3
            elif isinstance(ratio_3, int) or isinstance(ratio_3, float):
                ratio_3 = types.Real(ratio_3)
            elif isinstance(ratio_3, str):
                ratio_3 = types.Real.from_mcnp(ratio_3)

        self._ratio_3: types.Real = ratio_3

    @property
    def energy_3(self) -> types.Real:
        """
        Splitting/roulette energy #3

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_3

    @energy_3.setter
    def energy_3(self, energy_3: str | int | float | types.Real) -> None:
        """
        Sets `energy_3`.

        Parameters:
            energy_3: Splitting/roulette energy #3.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_3 is not None:
            if isinstance(energy_3, types.Real):
                energy_3 = energy_3
            elif isinstance(energy_3, int) or isinstance(energy_3, float):
                energy_3 = types.Real(energy_3)
            elif isinstance(energy_3, str):
                energy_3 = types.Real.from_mcnp(energy_3)

        self._energy_3: types.Real = energy_3

    @property
    def ratio_4(self) -> types.Real:
        """
        Splitting/roulette ratio #4

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_4

    @ratio_4.setter
    def ratio_4(self, ratio_4: str | int | float | types.Real) -> None:
        """
        Sets `ratio_4`.

        Parameters:
            ratio_4: Splitting/roulette ratio #4.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_4 is not None:
            if isinstance(ratio_4, types.Real):
                ratio_4 = ratio_4
            elif isinstance(ratio_4, int) or isinstance(ratio_4, float):
                ratio_4 = types.Real(ratio_4)
            elif isinstance(ratio_4, str):
                ratio_4 = types.Real.from_mcnp(ratio_4)

        self._ratio_4: types.Real = ratio_4

    @property
    def energy_4(self) -> types.Real:
        """
        Splitting/roulette energy #4

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_4

    @energy_4.setter
    def energy_4(self, energy_4: str | int | float | types.Real) -> None:
        """
        Sets `energy_4`.

        Parameters:
            energy_4: Splitting/roulette energy #4.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_4 is not None:
            if isinstance(energy_4, types.Real):
                energy_4 = energy_4
            elif isinstance(energy_4, int) or isinstance(energy_4, float):
                energy_4 = types.Real(energy_4)
            elif isinstance(energy_4, str):
                energy_4 = types.Real.from_mcnp(energy_4)

        self._energy_4: types.Real = energy_4

    @property
    def ratio_5(self) -> types.Real:
        """
        Splitting/roulette ratio #5

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_5

    @ratio_5.setter
    def ratio_5(self, ratio_5: str | int | float | types.Real) -> None:
        """
        Sets `ratio_5`.

        Parameters:
            ratio_5: Splitting/roulette ratio #5.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_5 is not None:
            if isinstance(ratio_5, types.Real):
                ratio_5 = ratio_5
            elif isinstance(ratio_5, int) or isinstance(ratio_5, float):
                ratio_5 = types.Real(ratio_5)
            elif isinstance(ratio_5, str):
                ratio_5 = types.Real.from_mcnp(ratio_5)

        self._ratio_5: types.Real = ratio_5

    @property
    def energy_5(self) -> types.Real:
        """
        Splitting/roulette energy #5

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_5

    @energy_5.setter
    def energy_5(self, energy_5: str | int | float | types.Real) -> None:
        """
        Sets `energy_5`.

        Parameters:
            energy_5: Splitting/roulette energy #5.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_5 is not None:
            if isinstance(energy_5, types.Real):
                energy_5 = energy_5
            elif isinstance(energy_5, int) or isinstance(energy_5, float):
                energy_5 = types.Real(energy_5)
            elif isinstance(energy_5, str):
                energy_5 = types.Real.from_mcnp(energy_5)

        self._energy_5: types.Real = energy_5

    @property
    def ratio_6(self) -> types.Real:
        """
        Splitting/roulette ratio #6

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_6

    @ratio_6.setter
    def ratio_6(self, ratio_6: str | int | float | types.Real) -> None:
        """
        Sets `ratio_6`.

        Parameters:
            ratio_6: Splitting/roulette ratio #6.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_6 is not None:
            if isinstance(ratio_6, types.Real):
                ratio_6 = ratio_6
            elif isinstance(ratio_6, int) or isinstance(ratio_6, float):
                ratio_6 = types.Real(ratio_6)
            elif isinstance(ratio_6, str):
                ratio_6 = types.Real.from_mcnp(ratio_6)

        self._ratio_6: types.Real = ratio_6

    @property
    def energy_6(self) -> types.Real:
        """
        Splitting/roulette energy #6

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_6

    @energy_6.setter
    def energy_6(self, energy_6: str | int | float | types.Real) -> None:
        """
        Sets `energy_6`.

        Parameters:
            energy_6: Splitting/roulette energy #6.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_6 is not None:
            if isinstance(energy_6, types.Real):
                energy_6 = energy_6
            elif isinstance(energy_6, int) or isinstance(energy_6, float):
                energy_6 = types.Real(energy_6)
            elif isinstance(energy_6, str):
                energy_6 = types.Real.from_mcnp(energy_6)

        self._energy_6: types.Real = energy_6

    @property
    def ratio_7(self) -> types.Real:
        """
        Splitting/roulette ratio #7

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_7

    @ratio_7.setter
    def ratio_7(self, ratio_7: str | int | float | types.Real) -> None:
        """
        Sets `ratio_7`.

        Parameters:
            ratio_7: Splitting/roulette ratio #7.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_7 is not None:
            if isinstance(ratio_7, types.Real):
                ratio_7 = ratio_7
            elif isinstance(ratio_7, int) or isinstance(ratio_7, float):
                ratio_7 = types.Real(ratio_7)
            elif isinstance(ratio_7, str):
                ratio_7 = types.Real.from_mcnp(ratio_7)

        self._ratio_7: types.Real = ratio_7

    @property
    def energy_7(self) -> types.Real:
        """
        Splitting/roulette energy #7

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_7

    @energy_7.setter
    def energy_7(self, energy_7: str | int | float | types.Real) -> None:
        """
        Sets `energy_7`.

        Parameters:
            energy_7: Splitting/roulette energy #7.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_7 is not None:
            if isinstance(energy_7, types.Real):
                energy_7 = energy_7
            elif isinstance(energy_7, int) or isinstance(energy_7, float):
                energy_7 = types.Real(energy_7)
            elif isinstance(energy_7, str):
                energy_7 = types.Real.from_mcnp(energy_7)

        self._energy_7: types.Real = energy_7

    @property
    def ratio_8(self) -> types.Real:
        """
        Splitting/roulette ratio #8

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_8

    @ratio_8.setter
    def ratio_8(self, ratio_8: str | int | float | types.Real) -> None:
        """
        Sets `ratio_8`.

        Parameters:
            ratio_8: Splitting/roulette ratio #8.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_8 is not None:
            if isinstance(ratio_8, types.Real):
                ratio_8 = ratio_8
            elif isinstance(ratio_8, int) or isinstance(ratio_8, float):
                ratio_8 = types.Real(ratio_8)
            elif isinstance(ratio_8, str):
                ratio_8 = types.Real.from_mcnp(ratio_8)

        self._ratio_8: types.Real = ratio_8

    @property
    def energy_8(self) -> types.Real:
        """
        Splitting/roulette energy #8

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_8

    @energy_8.setter
    def energy_8(self, energy_8: str | int | float | types.Real) -> None:
        """
        Sets `energy_8`.

        Parameters:
            energy_8: Splitting/roulette energy #8.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_8 is not None:
            if isinstance(energy_8, types.Real):
                energy_8 = energy_8
            elif isinstance(energy_8, int) or isinstance(energy_8, float):
                energy_8 = types.Real(energy_8)
            elif isinstance(energy_8, str):
                energy_8 = types.Real.from_mcnp(energy_8)

        self._energy_8: types.Real = energy_8

    @property
    def ratio_9(self) -> types.Real:
        """
        Splitting/roulette ratio #9

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_9

    @ratio_9.setter
    def ratio_9(self, ratio_9: str | int | float | types.Real) -> None:
        """
        Sets `ratio_9`.

        Parameters:
            ratio_9: Splitting/roulette ratio #9.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_9 is not None:
            if isinstance(ratio_9, types.Real):
                ratio_9 = ratio_9
            elif isinstance(ratio_9, int) or isinstance(ratio_9, float):
                ratio_9 = types.Real(ratio_9)
            elif isinstance(ratio_9, str):
                ratio_9 = types.Real.from_mcnp(ratio_9)

        self._ratio_9: types.Real = ratio_9

    @property
    def energy_9(self) -> types.Real:
        """
        Splitting/roulette energy #9

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_9

    @energy_9.setter
    def energy_9(self, energy_9: str | int | float | types.Real) -> None:
        """
        Sets `energy_9`.

        Parameters:
            energy_9: Splitting/roulette energy #9.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_9 is not None:
            if isinstance(energy_9, types.Real):
                energy_9 = energy_9
            elif isinstance(energy_9, int) or isinstance(energy_9, float):
                energy_9 = types.Real(energy_9)
            elif isinstance(energy_9, str):
                energy_9 = types.Real.from_mcnp(energy_9)

        self._energy_9: types.Real = energy_9

    @property
    def ratio_10(self) -> types.Real:
        """
        Splitting/roulette ratio #10

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_10

    @ratio_10.setter
    def ratio_10(self, ratio_10: str | int | float | types.Real) -> None:
        """
        Sets `ratio_10`.

        Parameters:
            ratio_10: Splitting/roulette ratio #10.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_10 is not None:
            if isinstance(ratio_10, types.Real):
                ratio_10 = ratio_10
            elif isinstance(ratio_10, int) or isinstance(ratio_10, float):
                ratio_10 = types.Real(ratio_10)
            elif isinstance(ratio_10, str):
                ratio_10 = types.Real.from_mcnp(ratio_10)

        self._ratio_10: types.Real = ratio_10

    @property
    def energy_10(self) -> types.Real:
        """
        Splitting/roulette energy #10

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_10

    @energy_10.setter
    def energy_10(self, energy_10: str | int | float | types.Real) -> None:
        """
        Sets `energy_10`.

        Parameters:
            energy_10: Splitting/roulette energy #10.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_10 is not None:
            if isinstance(energy_10, types.Real):
                energy_10 = energy_10
            elif isinstance(energy_10, int) or isinstance(energy_10, float):
                energy_10 = types.Real(energy_10)
            elif isinstance(energy_10, str):
                energy_10 = types.Real.from_mcnp(energy_10)

        self._energy_10: types.Real = energy_10

    @property
    def ratio_11(self) -> types.Real:
        """
        Splitting/roulette ratio #11

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_11

    @ratio_11.setter
    def ratio_11(self, ratio_11: str | int | float | types.Real) -> None:
        """
        Sets `ratio_11`.

        Parameters:
            ratio_11: Splitting/roulette ratio #11.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_11 is not None:
            if isinstance(ratio_11, types.Real):
                ratio_11 = ratio_11
            elif isinstance(ratio_11, int) or isinstance(ratio_11, float):
                ratio_11 = types.Real(ratio_11)
            elif isinstance(ratio_11, str):
                ratio_11 = types.Real.from_mcnp(ratio_11)

        self._ratio_11: types.Real = ratio_11

    @property
    def energy_11(self) -> types.Real:
        """
        Splitting/roulette energy #11

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_11

    @energy_11.setter
    def energy_11(self, energy_11: str | int | float | types.Real) -> None:
        """
        Sets `energy_11`.

        Parameters:
            energy_11: Splitting/roulette energy #11.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_11 is not None:
            if isinstance(energy_11, types.Real):
                energy_11 = energy_11
            elif isinstance(energy_11, int) or isinstance(energy_11, float):
                energy_11 = types.Real(energy_11)
            elif isinstance(energy_11, str):
                energy_11 = types.Real.from_mcnp(energy_11)

        self._energy_11: types.Real = energy_11

    @property
    def ratio_12(self) -> types.Real:
        """
        Splitting/roulette ratio #12

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_12

    @ratio_12.setter
    def ratio_12(self, ratio_12: str | int | float | types.Real) -> None:
        """
        Sets `ratio_12`.

        Parameters:
            ratio_12: Splitting/roulette ratio #12.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_12 is not None:
            if isinstance(ratio_12, types.Real):
                ratio_12 = ratio_12
            elif isinstance(ratio_12, int) or isinstance(ratio_12, float):
                ratio_12 = types.Real(ratio_12)
            elif isinstance(ratio_12, str):
                ratio_12 = types.Real.from_mcnp(ratio_12)

        self._ratio_12: types.Real = ratio_12

    @property
    def energy_12(self) -> types.Real:
        """
        Splitting/roulette energy #12

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_12

    @energy_12.setter
    def energy_12(self, energy_12: str | int | float | types.Real) -> None:
        """
        Sets `energy_12`.

        Parameters:
            energy_12: Splitting/roulette energy #12.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_12 is not None:
            if isinstance(energy_12, types.Real):
                energy_12 = energy_12
            elif isinstance(energy_12, int) or isinstance(energy_12, float):
                energy_12 = types.Real(energy_12)
            elif isinstance(energy_12, str):
                energy_12 = types.Real.from_mcnp(energy_12)

        self._energy_12: types.Real = energy_12

    @property
    def ratio_13(self) -> types.Real:
        """
        Splitting/roulette ratio #13

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_13

    @ratio_13.setter
    def ratio_13(self, ratio_13: str | int | float | types.Real) -> None:
        """
        Sets `ratio_13`.

        Parameters:
            ratio_13: Splitting/roulette ratio #13.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_13 is not None:
            if isinstance(ratio_13, types.Real):
                ratio_13 = ratio_13
            elif isinstance(ratio_13, int) or isinstance(ratio_13, float):
                ratio_13 = types.Real(ratio_13)
            elif isinstance(ratio_13, str):
                ratio_13 = types.Real.from_mcnp(ratio_13)

        self._ratio_13: types.Real = ratio_13

    @property
    def energy_13(self) -> types.Real:
        """
        Splitting/roulette energy #13

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_13

    @energy_13.setter
    def energy_13(self, energy_13: str | int | float | types.Real) -> None:
        """
        Sets `energy_13`.

        Parameters:
            energy_13: Splitting/roulette energy #13.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_13 is not None:
            if isinstance(energy_13, types.Real):
                energy_13 = energy_13
            elif isinstance(energy_13, int) or isinstance(energy_13, float):
                energy_13 = types.Real(energy_13)
            elif isinstance(energy_13, str):
                energy_13 = types.Real.from_mcnp(energy_13)

        self._energy_13: types.Real = energy_13

    @property
    def ratio_14(self) -> types.Real:
        """
        Splitting/roulette ratio #14

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_14

    @ratio_14.setter
    def ratio_14(self, ratio_14: str | int | float | types.Real) -> None:
        """
        Sets `ratio_14`.

        Parameters:
            ratio_14: Splitting/roulette ratio #14.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_14 is not None:
            if isinstance(ratio_14, types.Real):
                ratio_14 = ratio_14
            elif isinstance(ratio_14, int) or isinstance(ratio_14, float):
                ratio_14 = types.Real(ratio_14)
            elif isinstance(ratio_14, str):
                ratio_14 = types.Real.from_mcnp(ratio_14)

        self._ratio_14: types.Real = ratio_14

    @property
    def energy_14(self) -> types.Real:
        """
        Splitting/roulette energy #14

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_14

    @energy_14.setter
    def energy_14(self, energy_14: str | int | float | types.Real) -> None:
        """
        Sets `energy_14`.

        Parameters:
            energy_14: Splitting/roulette energy #14.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_14 is not None:
            if isinstance(energy_14, types.Real):
                energy_14 = energy_14
            elif isinstance(energy_14, int) or isinstance(energy_14, float):
                energy_14 = types.Real(energy_14)
            elif isinstance(energy_14, str):
                energy_14 = types.Real.from_mcnp(energy_14)

        self._energy_14: types.Real = energy_14

    @property
    def ratio_15(self) -> types.Real:
        """
        Splitting/roulette ratio #15

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_15

    @ratio_15.setter
    def ratio_15(self, ratio_15: str | int | float | types.Real) -> None:
        """
        Sets `ratio_15`.

        Parameters:
            ratio_15: Splitting/roulette ratio #15.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_15 is not None:
            if isinstance(ratio_15, types.Real):
                ratio_15 = ratio_15
            elif isinstance(ratio_15, int) or isinstance(ratio_15, float):
                ratio_15 = types.Real(ratio_15)
            elif isinstance(ratio_15, str):
                ratio_15 = types.Real.from_mcnp(ratio_15)

        self._ratio_15: types.Real = ratio_15

    @property
    def energy_15(self) -> types.Real:
        """
        Splitting/roulette energy #15

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_15

    @energy_15.setter
    def energy_15(self, energy_15: str | int | float | types.Real) -> None:
        """
        Sets `energy_15`.

        Parameters:
            energy_15: Splitting/roulette energy #15.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_15 is not None:
            if isinstance(energy_15, types.Real):
                energy_15 = energy_15
            elif isinstance(energy_15, int) or isinstance(energy_15, float):
                energy_15 = types.Real(energy_15)
            elif isinstance(energy_15, str):
                energy_15 = types.Real.from_mcnp(energy_15)

        self._energy_15: types.Real = energy_15

    @property
    def ratio_16(self) -> types.Real:
        """
        Splitting/roulette ratio #16

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_16

    @ratio_16.setter
    def ratio_16(self, ratio_16: str | int | float | types.Real) -> None:
        """
        Sets `ratio_16`.

        Parameters:
            ratio_16: Splitting/roulette ratio #16.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_16 is not None:
            if isinstance(ratio_16, types.Real):
                ratio_16 = ratio_16
            elif isinstance(ratio_16, int) or isinstance(ratio_16, float):
                ratio_16 = types.Real(ratio_16)
            elif isinstance(ratio_16, str):
                ratio_16 = types.Real.from_mcnp(ratio_16)

        self._ratio_16: types.Real = ratio_16

    @property
    def energy_16(self) -> types.Real:
        """
        Splitting/roulette energy #16

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_16

    @energy_16.setter
    def energy_16(self, energy_16: str | int | float | types.Real) -> None:
        """
        Sets `energy_16`.

        Parameters:
            energy_16: Splitting/roulette energy #16.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_16 is not None:
            if isinstance(energy_16, types.Real):
                energy_16 = energy_16
            elif isinstance(energy_16, int) or isinstance(energy_16, float):
                energy_16 = types.Real(energy_16)
            elif isinstance(energy_16, str):
                energy_16 = types.Real.from_mcnp(energy_16)

        self._energy_16: types.Real = energy_16

    @property
    def ratio_17(self) -> types.Real:
        """
        Splitting/roulette ratio #17

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_17

    @ratio_17.setter
    def ratio_17(self, ratio_17: str | int | float | types.Real) -> None:
        """
        Sets `ratio_17`.

        Parameters:
            ratio_17: Splitting/roulette ratio #17.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_17 is not None:
            if isinstance(ratio_17, types.Real):
                ratio_17 = ratio_17
            elif isinstance(ratio_17, int) or isinstance(ratio_17, float):
                ratio_17 = types.Real(ratio_17)
            elif isinstance(ratio_17, str):
                ratio_17 = types.Real.from_mcnp(ratio_17)

        self._ratio_17: types.Real = ratio_17

    @property
    def energy_17(self) -> types.Real:
        """
        Splitting/roulette energy #17

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_17

    @energy_17.setter
    def energy_17(self, energy_17: str | int | float | types.Real) -> None:
        """
        Sets `energy_17`.

        Parameters:
            energy_17: Splitting/roulette energy #17.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_17 is not None:
            if isinstance(energy_17, types.Real):
                energy_17 = energy_17
            elif isinstance(energy_17, int) or isinstance(energy_17, float):
                energy_17 = types.Real(energy_17)
            elif isinstance(energy_17, str):
                energy_17 = types.Real.from_mcnp(energy_17)

        self._energy_17: types.Real = energy_17

    @property
    def ratio_18(self) -> types.Real:
        """
        Splitting/roulette ratio #18

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_18

    @ratio_18.setter
    def ratio_18(self, ratio_18: str | int | float | types.Real) -> None:
        """
        Sets `ratio_18`.

        Parameters:
            ratio_18: Splitting/roulette ratio #18.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_18 is not None:
            if isinstance(ratio_18, types.Real):
                ratio_18 = ratio_18
            elif isinstance(ratio_18, int) or isinstance(ratio_18, float):
                ratio_18 = types.Real(ratio_18)
            elif isinstance(ratio_18, str):
                ratio_18 = types.Real.from_mcnp(ratio_18)

        self._ratio_18: types.Real = ratio_18

    @property
    def energy_18(self) -> types.Real:
        """
        Splitting/roulette energy #18

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_18

    @energy_18.setter
    def energy_18(self, energy_18: str | int | float | types.Real) -> None:
        """
        Sets `energy_18`.

        Parameters:
            energy_18: Splitting/roulette energy #18.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_18 is not None:
            if isinstance(energy_18, types.Real):
                energy_18 = energy_18
            elif isinstance(energy_18, int) or isinstance(energy_18, float):
                energy_18 = types.Real(energy_18)
            elif isinstance(energy_18, str):
                energy_18 = types.Real.from_mcnp(energy_18)

        self._energy_18: types.Real = energy_18

    @property
    def ratio_19(self) -> types.Real:
        """
        Splitting/roulette ratio #19

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_19

    @ratio_19.setter
    def ratio_19(self, ratio_19: str | int | float | types.Real) -> None:
        """
        Sets `ratio_19`.

        Parameters:
            ratio_19: Splitting/roulette ratio #19.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_19 is not None:
            if isinstance(ratio_19, types.Real):
                ratio_19 = ratio_19
            elif isinstance(ratio_19, int) or isinstance(ratio_19, float):
                ratio_19 = types.Real(ratio_19)
            elif isinstance(ratio_19, str):
                ratio_19 = types.Real.from_mcnp(ratio_19)

        self._ratio_19: types.Real = ratio_19

    @property
    def energy_19(self) -> types.Real:
        """
        Splitting/roulette energy #19

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_19

    @energy_19.setter
    def energy_19(self, energy_19: str | int | float | types.Real) -> None:
        """
        Sets `energy_19`.

        Parameters:
            energy_19: Splitting/roulette energy #19.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_19 is not None:
            if isinstance(energy_19, types.Real):
                energy_19 = energy_19
            elif isinstance(energy_19, int) or isinstance(energy_19, float):
                energy_19 = types.Real(energy_19)
            elif isinstance(energy_19, str):
                energy_19 = types.Real.from_mcnp(energy_19)

        self._energy_19: types.Real = energy_19

    @property
    def ratio_20(self) -> types.Real:
        """
        Splitting/roulette ratio #20

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._ratio_20

    @ratio_20.setter
    def ratio_20(self, ratio_20: str | int | float | types.Real) -> None:
        """
        Sets `ratio_20`.

        Parameters:
            ratio_20: Splitting/roulette ratio #20.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if ratio_20 is not None:
            if isinstance(ratio_20, types.Real):
                ratio_20 = ratio_20
            elif isinstance(ratio_20, int) or isinstance(ratio_20, float):
                ratio_20 = types.Real(ratio_20)
            elif isinstance(ratio_20, str):
                ratio_20 = types.Real.from_mcnp(ratio_20)

        self._ratio_20: types.Real = ratio_20

    @property
    def energy_20(self) -> types.Real:
        """
        Splitting/roulette energy #20

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._energy_20

    @energy_20.setter
    def energy_20(self, energy_20: str | int | float | types.Real) -> None:
        """
        Sets `energy_20`.

        Parameters:
            energy_20: Splitting/roulette energy #20.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if energy_20 is not None:
            if isinstance(energy_20, types.Real):
                energy_20 = energy_20
            elif isinstance(energy_20, int) or isinstance(energy_20, float):
                energy_20 = types.Real(energy_20)
            elif isinstance(energy_20, str):
                energy_20 = types.Real.from_mcnp(energy_20)

        self._energy_20: types.Real = energy_20
