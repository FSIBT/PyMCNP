import re

from . import _card
from .. import types
from .. import errors


class Tsplt(_card.Card):
    """
    Represents INP `tsplt` cards.
    """

    _KEYWORD = 'tsplt'

    _ATTRS = {
        'designator': types.Designator,
        'ratio_1': types.Real,
        'time_1': types.Real,
        'ratio_2': types.Real,
        'time_2': types.Real,
        'ratio_3': types.Real,
        'time_3': types.Real,
        'ratio_4': types.Real,
        'time_4': types.Real,
        'ratio_5': types.Real,
        'time_5': types.Real,
        'ratio_6': types.Real,
        'time_6': types.Real,
        'ratio_7': types.Real,
        'time_7': types.Real,
        'ratio_8': types.Real,
        'time_8': types.Real,
        'ratio_9': types.Real,
        'time_9': types.Real,
        'ratio_10': types.Real,
        'time_10': types.Real,
        'ratio_11': types.Real,
        'time_11': types.Real,
        'ratio_12': types.Real,
        'time_12': types.Real,
        'ratio_13': types.Real,
        'time_13': types.Real,
        'ratio_14': types.Real,
        'time_14': types.Real,
        'ratio_15': types.Real,
        'time_15': types.Real,
        'ratio_16': types.Real,
        'time_16': types.Real,
        'ratio_17': types.Real,
        'time_17': types.Real,
        'ratio_18': types.Real,
        'time_18': types.Real,
        'ratio_19': types.Real,
        'time_19': types.Real,
        'ratio_20': types.Real,
        'time_20': types.Real,
    }

    _REGEX = re.compile(
        rf'\Atsplt:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        designator: str | types.Designator,
        ratio_1: str | int | float | types.Real = None,
        time_1: str | int | float | types.Real = None,
        ratio_2: str | int | float | types.Real = None,
        time_2: str | int | float | types.Real = None,
        ratio_3: str | int | float | types.Real = None,
        time_3: str | int | float | types.Real = None,
        ratio_4: str | int | float | types.Real = None,
        time_4: str | int | float | types.Real = None,
        ratio_5: str | int | float | types.Real = None,
        time_5: str | int | float | types.Real = None,
        ratio_6: str | int | float | types.Real = None,
        time_6: str | int | float | types.Real = None,
        ratio_7: str | int | float | types.Real = None,
        time_7: str | int | float | types.Real = None,
        ratio_8: str | int | float | types.Real = None,
        time_8: str | int | float | types.Real = None,
        ratio_9: str | int | float | types.Real = None,
        time_9: str | int | float | types.Real = None,
        ratio_10: str | int | float | types.Real = None,
        time_10: str | int | float | types.Real = None,
        ratio_11: str | int | float | types.Real = None,
        time_11: str | int | float | types.Real = None,
        ratio_12: str | int | float | types.Real = None,
        time_12: str | int | float | types.Real = None,
        ratio_13: str | int | float | types.Real = None,
        time_13: str | int | float | types.Real = None,
        ratio_14: str | int | float | types.Real = None,
        time_14: str | int | float | types.Real = None,
        ratio_15: str | int | float | types.Real = None,
        time_15: str | int | float | types.Real = None,
        ratio_16: str | int | float | types.Real = None,
        time_16: str | int | float | types.Real = None,
        ratio_17: str | int | float | types.Real = None,
        time_17: str | int | float | types.Real = None,
        ratio_18: str | int | float | types.Real = None,
        time_18: str | int | float | types.Real = None,
        ratio_19: str | int | float | types.Real = None,
        time_19: str | int | float | types.Real = None,
        ratio_20: str | int | float | types.Real = None,
        time_20: str | int | float | types.Real = None,
    ):
        """
        Initializes `Tsplt`.

        Parameters:
            designator: Data card particle designator.
            ratio_1: Splitting/roulette ratio #1.
            time_1: Splitting/roulette time #1.
            ratio_2: Splitting/roulette ratio #2.
            time_2: Splitting/roulette time #2.
            ratio_3: Splitting/roulette ratio #3.
            time_3: Splitting/roulette time #3.
            ratio_4: Splitting/roulette ratio #4.
            time_4: Splitting/roulette time #4.
            ratio_5: Splitting/roulette ratio #5.
            time_5: Splitting/roulette time #5.
            ratio_6: Splitting/roulette ratio #6.
            time_6: Splitting/roulette time #6.
            ratio_7: Splitting/roulette ratio #7.
            time_7: Splitting/roulette time #7.
            ratio_8: Splitting/roulette ratio #8.
            time_8: Splitting/roulette time #8.
            ratio_9: Splitting/roulette ratio #9.
            time_9: Splitting/roulette time #9.
            ratio_10: Splitting/roulette ratio #10.
            time_10: Splitting/roulette time #10.
            ratio_11: Splitting/roulette ratio #11.
            time_11: Splitting/roulette time #11.
            ratio_12: Splitting/roulette ratio #12.
            time_12: Splitting/roulette time #12.
            ratio_13: Splitting/roulette ratio #13.
            time_13: Splitting/roulette time #13.
            ratio_14: Splitting/roulette ratio #14.
            time_14: Splitting/roulette time #14.
            ratio_15: Splitting/roulette ratio #15.
            time_15: Splitting/roulette time #15.
            ratio_16: Splitting/roulette ratio #16.
            time_16: Splitting/roulette time #16.
            ratio_17: Splitting/roulette ratio #17.
            time_17: Splitting/roulette time #17.
            ratio_18: Splitting/roulette ratio #18.
            time_18: Splitting/roulette time #18.
            ratio_19: Splitting/roulette ratio #19.
            time_19: Splitting/roulette time #19.
            ratio_20: Splitting/roulette ratio #20.
            time_20: Splitting/roulette time #20.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.designator: types.Designator = designator
        self.ratio_1: types.Real = ratio_1
        self.time_1: types.Real = time_1
        self.ratio_2: types.Real = ratio_2
        self.time_2: types.Real = time_2
        self.ratio_3: types.Real = ratio_3
        self.time_3: types.Real = time_3
        self.ratio_4: types.Real = ratio_4
        self.time_4: types.Real = time_4
        self.ratio_5: types.Real = ratio_5
        self.time_5: types.Real = time_5
        self.ratio_6: types.Real = ratio_6
        self.time_6: types.Real = time_6
        self.ratio_7: types.Real = ratio_7
        self.time_7: types.Real = time_7
        self.ratio_8: types.Real = ratio_8
        self.time_8: types.Real = time_8
        self.ratio_9: types.Real = ratio_9
        self.time_9: types.Real = time_9
        self.ratio_10: types.Real = ratio_10
        self.time_10: types.Real = time_10
        self.ratio_11: types.Real = ratio_11
        self.time_11: types.Real = time_11
        self.ratio_12: types.Real = ratio_12
        self.time_12: types.Real = time_12
        self.ratio_13: types.Real = ratio_13
        self.time_13: types.Real = time_13
        self.ratio_14: types.Real = ratio_14
        self.time_14: types.Real = time_14
        self.ratio_15: types.Real = ratio_15
        self.time_15: types.Real = time_15
        self.ratio_16: types.Real = ratio_16
        self.time_16: types.Real = time_16
        self.ratio_17: types.Real = ratio_17
        self.time_17: types.Real = time_17
        self.ratio_18: types.Real = ratio_18
        self.time_18: types.Real = time_18
        self.ratio_19: types.Real = ratio_19
        self.time_19: types.Real = time_19
        self.ratio_20: types.Real = ratio_20
        self.time_20: types.Real = time_20

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
    def time_1(self) -> types.Real:
        """
        Splitting/roulette time #1

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_1

    @time_1.setter
    def time_1(self, time_1: str | int | float | types.Real) -> None:
        """
        Sets `time_1`.

        Parameters:
            time_1: Splitting/roulette time #1.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_1 is not None:
            if isinstance(time_1, types.Real):
                time_1 = time_1
            elif isinstance(time_1, int) or isinstance(time_1, float):
                time_1 = types.Real(time_1)
            elif isinstance(time_1, str):
                time_1 = types.Real.from_mcnp(time_1)

        self._time_1: types.Real = time_1

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
    def time_2(self) -> types.Real:
        """
        Splitting/roulette time #2

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_2

    @time_2.setter
    def time_2(self, time_2: str | int | float | types.Real) -> None:
        """
        Sets `time_2`.

        Parameters:
            time_2: Splitting/roulette time #2.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_2 is not None:
            if isinstance(time_2, types.Real):
                time_2 = time_2
            elif isinstance(time_2, int) or isinstance(time_2, float):
                time_2 = types.Real(time_2)
            elif isinstance(time_2, str):
                time_2 = types.Real.from_mcnp(time_2)

        self._time_2: types.Real = time_2

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
    def time_3(self) -> types.Real:
        """
        Splitting/roulette time #3

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_3

    @time_3.setter
    def time_3(self, time_3: str | int | float | types.Real) -> None:
        """
        Sets `time_3`.

        Parameters:
            time_3: Splitting/roulette time #3.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_3 is not None:
            if isinstance(time_3, types.Real):
                time_3 = time_3
            elif isinstance(time_3, int) or isinstance(time_3, float):
                time_3 = types.Real(time_3)
            elif isinstance(time_3, str):
                time_3 = types.Real.from_mcnp(time_3)

        self._time_3: types.Real = time_3

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
    def time_4(self) -> types.Real:
        """
        Splitting/roulette time #4

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_4

    @time_4.setter
    def time_4(self, time_4: str | int | float | types.Real) -> None:
        """
        Sets `time_4`.

        Parameters:
            time_4: Splitting/roulette time #4.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_4 is not None:
            if isinstance(time_4, types.Real):
                time_4 = time_4
            elif isinstance(time_4, int) or isinstance(time_4, float):
                time_4 = types.Real(time_4)
            elif isinstance(time_4, str):
                time_4 = types.Real.from_mcnp(time_4)

        self._time_4: types.Real = time_4

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
    def time_5(self) -> types.Real:
        """
        Splitting/roulette time #5

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_5

    @time_5.setter
    def time_5(self, time_5: str | int | float | types.Real) -> None:
        """
        Sets `time_5`.

        Parameters:
            time_5: Splitting/roulette time #5.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_5 is not None:
            if isinstance(time_5, types.Real):
                time_5 = time_5
            elif isinstance(time_5, int) or isinstance(time_5, float):
                time_5 = types.Real(time_5)
            elif isinstance(time_5, str):
                time_5 = types.Real.from_mcnp(time_5)

        self._time_5: types.Real = time_5

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
    def time_6(self) -> types.Real:
        """
        Splitting/roulette time #6

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_6

    @time_6.setter
    def time_6(self, time_6: str | int | float | types.Real) -> None:
        """
        Sets `time_6`.

        Parameters:
            time_6: Splitting/roulette time #6.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_6 is not None:
            if isinstance(time_6, types.Real):
                time_6 = time_6
            elif isinstance(time_6, int) or isinstance(time_6, float):
                time_6 = types.Real(time_6)
            elif isinstance(time_6, str):
                time_6 = types.Real.from_mcnp(time_6)

        self._time_6: types.Real = time_6

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
    def time_7(self) -> types.Real:
        """
        Splitting/roulette time #7

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_7

    @time_7.setter
    def time_7(self, time_7: str | int | float | types.Real) -> None:
        """
        Sets `time_7`.

        Parameters:
            time_7: Splitting/roulette time #7.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_7 is not None:
            if isinstance(time_7, types.Real):
                time_7 = time_7
            elif isinstance(time_7, int) or isinstance(time_7, float):
                time_7 = types.Real(time_7)
            elif isinstance(time_7, str):
                time_7 = types.Real.from_mcnp(time_7)

        self._time_7: types.Real = time_7

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
    def time_8(self) -> types.Real:
        """
        Splitting/roulette time #8

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_8

    @time_8.setter
    def time_8(self, time_8: str | int | float | types.Real) -> None:
        """
        Sets `time_8`.

        Parameters:
            time_8: Splitting/roulette time #8.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_8 is not None:
            if isinstance(time_8, types.Real):
                time_8 = time_8
            elif isinstance(time_8, int) or isinstance(time_8, float):
                time_8 = types.Real(time_8)
            elif isinstance(time_8, str):
                time_8 = types.Real.from_mcnp(time_8)

        self._time_8: types.Real = time_8

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
    def time_9(self) -> types.Real:
        """
        Splitting/roulette time #9

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_9

    @time_9.setter
    def time_9(self, time_9: str | int | float | types.Real) -> None:
        """
        Sets `time_9`.

        Parameters:
            time_9: Splitting/roulette time #9.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_9 is not None:
            if isinstance(time_9, types.Real):
                time_9 = time_9
            elif isinstance(time_9, int) or isinstance(time_9, float):
                time_9 = types.Real(time_9)
            elif isinstance(time_9, str):
                time_9 = types.Real.from_mcnp(time_9)

        self._time_9: types.Real = time_9

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
    def time_10(self) -> types.Real:
        """
        Splitting/roulette time #10

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_10

    @time_10.setter
    def time_10(self, time_10: str | int | float | types.Real) -> None:
        """
        Sets `time_10`.

        Parameters:
            time_10: Splitting/roulette time #10.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_10 is not None:
            if isinstance(time_10, types.Real):
                time_10 = time_10
            elif isinstance(time_10, int) or isinstance(time_10, float):
                time_10 = types.Real(time_10)
            elif isinstance(time_10, str):
                time_10 = types.Real.from_mcnp(time_10)

        self._time_10: types.Real = time_10

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
    def time_11(self) -> types.Real:
        """
        Splitting/roulette time #11

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_11

    @time_11.setter
    def time_11(self, time_11: str | int | float | types.Real) -> None:
        """
        Sets `time_11`.

        Parameters:
            time_11: Splitting/roulette time #11.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_11 is not None:
            if isinstance(time_11, types.Real):
                time_11 = time_11
            elif isinstance(time_11, int) or isinstance(time_11, float):
                time_11 = types.Real(time_11)
            elif isinstance(time_11, str):
                time_11 = types.Real.from_mcnp(time_11)

        self._time_11: types.Real = time_11

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
    def time_12(self) -> types.Real:
        """
        Splitting/roulette time #12

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_12

    @time_12.setter
    def time_12(self, time_12: str | int | float | types.Real) -> None:
        """
        Sets `time_12`.

        Parameters:
            time_12: Splitting/roulette time #12.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_12 is not None:
            if isinstance(time_12, types.Real):
                time_12 = time_12
            elif isinstance(time_12, int) or isinstance(time_12, float):
                time_12 = types.Real(time_12)
            elif isinstance(time_12, str):
                time_12 = types.Real.from_mcnp(time_12)

        self._time_12: types.Real = time_12

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
    def time_13(self) -> types.Real:
        """
        Splitting/roulette time #13

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_13

    @time_13.setter
    def time_13(self, time_13: str | int | float | types.Real) -> None:
        """
        Sets `time_13`.

        Parameters:
            time_13: Splitting/roulette time #13.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_13 is not None:
            if isinstance(time_13, types.Real):
                time_13 = time_13
            elif isinstance(time_13, int) or isinstance(time_13, float):
                time_13 = types.Real(time_13)
            elif isinstance(time_13, str):
                time_13 = types.Real.from_mcnp(time_13)

        self._time_13: types.Real = time_13

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
    def time_14(self) -> types.Real:
        """
        Splitting/roulette time #14

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_14

    @time_14.setter
    def time_14(self, time_14: str | int | float | types.Real) -> None:
        """
        Sets `time_14`.

        Parameters:
            time_14: Splitting/roulette time #14.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_14 is not None:
            if isinstance(time_14, types.Real):
                time_14 = time_14
            elif isinstance(time_14, int) or isinstance(time_14, float):
                time_14 = types.Real(time_14)
            elif isinstance(time_14, str):
                time_14 = types.Real.from_mcnp(time_14)

        self._time_14: types.Real = time_14

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
    def time_15(self) -> types.Real:
        """
        Splitting/roulette time #15

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_15

    @time_15.setter
    def time_15(self, time_15: str | int | float | types.Real) -> None:
        """
        Sets `time_15`.

        Parameters:
            time_15: Splitting/roulette time #15.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_15 is not None:
            if isinstance(time_15, types.Real):
                time_15 = time_15
            elif isinstance(time_15, int) or isinstance(time_15, float):
                time_15 = types.Real(time_15)
            elif isinstance(time_15, str):
                time_15 = types.Real.from_mcnp(time_15)

        self._time_15: types.Real = time_15

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
    def time_16(self) -> types.Real:
        """
        Splitting/roulette time #16

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_16

    @time_16.setter
    def time_16(self, time_16: str | int | float | types.Real) -> None:
        """
        Sets `time_16`.

        Parameters:
            time_16: Splitting/roulette time #16.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_16 is not None:
            if isinstance(time_16, types.Real):
                time_16 = time_16
            elif isinstance(time_16, int) or isinstance(time_16, float):
                time_16 = types.Real(time_16)
            elif isinstance(time_16, str):
                time_16 = types.Real.from_mcnp(time_16)

        self._time_16: types.Real = time_16

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
    def time_17(self) -> types.Real:
        """
        Splitting/roulette time #17

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_17

    @time_17.setter
    def time_17(self, time_17: str | int | float | types.Real) -> None:
        """
        Sets `time_17`.

        Parameters:
            time_17: Splitting/roulette time #17.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_17 is not None:
            if isinstance(time_17, types.Real):
                time_17 = time_17
            elif isinstance(time_17, int) or isinstance(time_17, float):
                time_17 = types.Real(time_17)
            elif isinstance(time_17, str):
                time_17 = types.Real.from_mcnp(time_17)

        self._time_17: types.Real = time_17

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
    def time_18(self) -> types.Real:
        """
        Splitting/roulette time #18

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_18

    @time_18.setter
    def time_18(self, time_18: str | int | float | types.Real) -> None:
        """
        Sets `time_18`.

        Parameters:
            time_18: Splitting/roulette time #18.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_18 is not None:
            if isinstance(time_18, types.Real):
                time_18 = time_18
            elif isinstance(time_18, int) or isinstance(time_18, float):
                time_18 = types.Real(time_18)
            elif isinstance(time_18, str):
                time_18 = types.Real.from_mcnp(time_18)

        self._time_18: types.Real = time_18

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
    def time_19(self) -> types.Real:
        """
        Splitting/roulette time #19

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_19

    @time_19.setter
    def time_19(self, time_19: str | int | float | types.Real) -> None:
        """
        Sets `time_19`.

        Parameters:
            time_19: Splitting/roulette time #19.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_19 is not None:
            if isinstance(time_19, types.Real):
                time_19 = time_19
            elif isinstance(time_19, int) or isinstance(time_19, float):
                time_19 = types.Real(time_19)
            elif isinstance(time_19, str):
                time_19 = types.Real.from_mcnp(time_19)

        self._time_19: types.Real = time_19

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
    def time_20(self) -> types.Real:
        """
        Splitting/roulette time #20

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._time_20

    @time_20.setter
    def time_20(self, time_20: str | int | float | types.Real) -> None:
        """
        Sets `time_20`.

        Parameters:
            time_20: Splitting/roulette time #20.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if time_20 is not None:
            if isinstance(time_20, types.Real):
                time_20 = time_20
            elif isinstance(time_20, int) or isinstance(time_20, float):
                time_20 = types.Real(time_20)
            elif isinstance(time_20, str):
                time_20 = types.Real.from_mcnp(time_20)

        self._time_20: types.Real = time_20
