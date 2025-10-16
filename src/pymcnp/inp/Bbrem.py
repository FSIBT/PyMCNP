import re

from . import _card
from .. import types
from .. import errors


class Bbrem(_card.Card):
    """
    Represents INP bbrem cards.
    """

    _KEYWORD = 'bbrem'

    _ATTRS = {
        'bias_1': types.Real,
        'bias_2': types.Real,
        'bias_3': types.Real,
        'bias_4': types.Real,
        'bias_5': types.Real,
        'bias_6': types.Real,
        'bias_7': types.Real,
        'bias_8': types.Real,
        'bias_9': types.Real,
        'bias_10': types.Real,
        'bias_11': types.Real,
        'bias_12': types.Real,
        'bias_13': types.Real,
        'bias_14': types.Real,
        'bias_15': types.Real,
        'bias_16': types.Real,
        'bias_17': types.Real,
        'bias_18': types.Real,
        'bias_19': types.Real,
        'bias_20': types.Real,
        'bias_21': types.Real,
        'bias_22': types.Real,
        'bias_23': types.Real,
        'bias_24': types.Real,
        'bias_25': types.Real,
        'bias_26': types.Real,
        'bias_27': types.Real,
        'bias_28': types.Real,
        'bias_29': types.Real,
        'bias_30': types.Real,
        'bias_31': types.Real,
        'bias_32': types.Real,
        'bias_33': types.Real,
        'bias_34': types.Real,
        'bias_35': types.Real,
        'bias_36': types.Real,
        'bias_37': types.Real,
        'bias_38': types.Real,
        'bias_39': types.Real,
        'bias_40': types.Real,
        'bias_41': types.Real,
        'bias_42': types.Real,
        'bias_43': types.Real,
        'bias_44': types.Real,
        'bias_45': types.Real,
        'bias_46': types.Real,
        'bias_47': types.Real,
        'bias_48': types.Real,
        'bias_49': types.Real,
        'materials': types.Tuple(types.Integer),
    }

    _REGEX = re.compile(
        rf'\Abbrem( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})((?: {types.Integer._REGEX.pattern[2:-2]})+?)\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        bias_1: str | int | float | types.Real,
        bias_2: str | int | float | types.Real,
        bias_3: str | int | float | types.Real,
        bias_4: str | int | float | types.Real,
        bias_5: str | int | float | types.Real,
        bias_6: str | int | float | types.Real,
        bias_7: str | int | float | types.Real,
        bias_8: str | int | float | types.Real,
        bias_9: str | int | float | types.Real,
        bias_10: str | int | float | types.Real,
        bias_11: str | int | float | types.Real,
        bias_12: str | int | float | types.Real,
        bias_13: str | int | float | types.Real,
        bias_14: str | int | float | types.Real,
        bias_15: str | int | float | types.Real,
        bias_16: str | int | float | types.Real,
        bias_17: str | int | float | types.Real,
        bias_18: str | int | float | types.Real,
        bias_19: str | int | float | types.Real,
        bias_20: str | int | float | types.Real,
        bias_21: str | int | float | types.Real,
        bias_22: str | int | float | types.Real,
        bias_23: str | int | float | types.Real,
        bias_24: str | int | float | types.Real,
        bias_25: str | int | float | types.Real,
        bias_26: str | int | float | types.Real,
        bias_27: str | int | float | types.Real,
        bias_28: str | int | float | types.Real,
        bias_29: str | int | float | types.Real,
        bias_30: str | int | float | types.Real,
        bias_31: str | int | float | types.Real,
        bias_32: str | int | float | types.Real,
        bias_33: str | int | float | types.Real,
        bias_34: str | int | float | types.Real,
        bias_35: str | int | float | types.Real,
        bias_36: str | int | float | types.Real,
        bias_37: str | int | float | types.Real,
        bias_38: str | int | float | types.Real,
        bias_39: str | int | float | types.Real,
        bias_40: str | int | float | types.Real,
        bias_41: str | int | float | types.Real,
        bias_42: str | int | float | types.Real,
        bias_43: str | int | float | types.Real,
        bias_44: str | int | float | types.Real,
        bias_45: str | int | float | types.Real,
        bias_46: str | int | float | types.Real,
        bias_47: str | int | float | types.Real,
        bias_48: str | int | float | types.Real,
        bias_49: str | int | float | types.Real,
        materials: list[str] | list[int] | list[types.Integer],
    ):
        """
        Initializes `Bbrem`.

        Parameters:
            bias_1: Bias factor #1 for bremsstrahlung specturm.
            bias_2: Bias factor #2 for bremsstrahlung specturm.
            bias_3: Bias factor #3 for bremsstrahlung specturm.
            bias_4: Bias factor #4 for bremsstrahlung specturm.
            bias_5: Bias factor #5 for bremsstrahlung specturm.
            bias_6: Bias factor #6 for bremsstrahlung specturm.
            bias_7: Bias factor #7 for bremsstrahlung specturm.
            bias_8: Bias factor #8 for bremsstrahlung specturm.
            bias_9: Bias factor #9 for bremsstrahlung specturm.
            bias_10: Bias factor #10 for bremsstrahlung specturm.
            bias_11: Bias factor #11 for bremsstrahlung specturm.
            bias_12: Bias factor #12 for bremsstrahlung specturm.
            bias_13: Bias factor #13 for bremsstrahlung specturm.
            bias_14: Bias factor #14 for bremsstrahlung specturm.
            bias_15: Bias factor #15 for bremsstrahlung specturm.
            bias_16: Bias factor #16 for bremsstrahlung specturm.
            bias_17: Bias factor #17 for bremsstrahlung specturm.
            bias_18: Bias factor #18 for bremsstrahlung specturm.
            bias_19: Bias factor #19 for bremsstrahlung specturm.
            bias_20: Bias factor #20 for bremsstrahlung specturm.
            bias_21: Bias factor #21 for bremsstrahlung specturm.
            bias_22: Bias factor #22 for bremsstrahlung specturm.
            bias_23: Bias factor #23 for bremsstrahlung specturm.
            bias_24: Bias factor #24 for bremsstrahlung specturm.
            bias_25: Bias factor #25 for bremsstrahlung specturm.
            bias_26: Bias factor #26 for bremsstrahlung specturm.
            bias_27: Bias factor #27 for bremsstrahlung specturm.
            bias_28: Bias factor #28 for bremsstrahlung specturm.
            bias_29: Bias factor #29 for bremsstrahlung specturm.
            bias_30: Bias factor #30 for bremsstrahlung specturm.
            bias_31: Bias factor #31 for bremsstrahlung specturm.
            bias_32: Bias factor #32 for bremsstrahlung specturm.
            bias_33: Bias factor #33 for bremsstrahlung specturm.
            bias_34: Bias factor #34 for bremsstrahlung specturm.
            bias_35: Bias factor #35 for bremsstrahlung specturm.
            bias_36: Bias factor #36 for bremsstrahlung specturm.
            bias_37: Bias factor #37 for bremsstrahlung specturm.
            bias_38: Bias factor #38 for bremsstrahlung specturm.
            bias_39: Bias factor #39 for bremsstrahlung specturm.
            bias_40: Bias factor #40 for bremsstrahlung specturm.
            bias_41: Bias factor #41 for bremsstrahlung specturm.
            bias_42: Bias factor #42 for bremsstrahlung specturm.
            bias_43: Bias factor #43 for bremsstrahlung specturm.
            bias_44: Bias factor #44 for bremsstrahlung specturm.
            bias_45: Bias factor #45 for bremsstrahlung specturm.
            bias_46: Bias factor #46 for bremsstrahlung specturm.
            bias_47: Bias factor #47 for bremsstrahlung specturm.
            bias_48: Bias factor #48 for bremsstrahlung specturm.
            bias_49: Bias factor #49 for bremsstrahlung specturm.
            materials: Material to bias.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.bias_1: types.Real = bias_1
        self.bias_2: types.Real = bias_2
        self.bias_3: types.Real = bias_3
        self.bias_4: types.Real = bias_4
        self.bias_5: types.Real = bias_5
        self.bias_6: types.Real = bias_6
        self.bias_7: types.Real = bias_7
        self.bias_8: types.Real = bias_8
        self.bias_9: types.Real = bias_9
        self.bias_10: types.Real = bias_10
        self.bias_11: types.Real = bias_11
        self.bias_12: types.Real = bias_12
        self.bias_13: types.Real = bias_13
        self.bias_14: types.Real = bias_14
        self.bias_15: types.Real = bias_15
        self.bias_16: types.Real = bias_16
        self.bias_17: types.Real = bias_17
        self.bias_18: types.Real = bias_18
        self.bias_19: types.Real = bias_19
        self.bias_20: types.Real = bias_20
        self.bias_21: types.Real = bias_21
        self.bias_22: types.Real = bias_22
        self.bias_23: types.Real = bias_23
        self.bias_24: types.Real = bias_24
        self.bias_25: types.Real = bias_25
        self.bias_26: types.Real = bias_26
        self.bias_27: types.Real = bias_27
        self.bias_28: types.Real = bias_28
        self.bias_29: types.Real = bias_29
        self.bias_30: types.Real = bias_30
        self.bias_31: types.Real = bias_31
        self.bias_32: types.Real = bias_32
        self.bias_33: types.Real = bias_33
        self.bias_34: types.Real = bias_34
        self.bias_35: types.Real = bias_35
        self.bias_36: types.Real = bias_36
        self.bias_37: types.Real = bias_37
        self.bias_38: types.Real = bias_38
        self.bias_39: types.Real = bias_39
        self.bias_40: types.Real = bias_40
        self.bias_41: types.Real = bias_41
        self.bias_42: types.Real = bias_42
        self.bias_43: types.Real = bias_43
        self.bias_44: types.Real = bias_44
        self.bias_45: types.Real = bias_45
        self.bias_46: types.Real = bias_46
        self.bias_47: types.Real = bias_47
        self.bias_48: types.Real = bias_48
        self.bias_49: types.Real = bias_49
        self.materials: types.Tuple(types.Integer) = materials

    @property
    def bias_1(self) -> types.Real:
        """
        Bias factor #1 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_1

    @bias_1.setter
    def bias_1(self, bias_1: str | int | float | types.Real) -> None:
        """
        Sets `bias_1`.

        Parameters:
            bias_1: Bias factor #1 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_1 is not None:
            if isinstance(bias_1, types.Real):
                bias_1 = bias_1
            elif isinstance(bias_1, int) or isinstance(bias_1, float):
                bias_1 = types.Real(bias_1)
            elif isinstance(bias_1, str):
                bias_1 = types.Real.from_mcnp(bias_1)

        if bias_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_1)

        self._bias_1: types.Real = bias_1

    @property
    def bias_2(self) -> types.Real:
        """
        Bias factor #2 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_2

    @bias_2.setter
    def bias_2(self, bias_2: str | int | float | types.Real) -> None:
        """
        Sets `bias_2`.

        Parameters:
            bias_2: Bias factor #2 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_2 is not None:
            if isinstance(bias_2, types.Real):
                bias_2 = bias_2
            elif isinstance(bias_2, int) or isinstance(bias_2, float):
                bias_2 = types.Real(bias_2)
            elif isinstance(bias_2, str):
                bias_2 = types.Real.from_mcnp(bias_2)

        if bias_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_2)

        self._bias_2: types.Real = bias_2

    @property
    def bias_3(self) -> types.Real:
        """
        Bias factor #3 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_3

    @bias_3.setter
    def bias_3(self, bias_3: str | int | float | types.Real) -> None:
        """
        Sets `bias_3`.

        Parameters:
            bias_3: Bias factor #3 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_3 is not None:
            if isinstance(bias_3, types.Real):
                bias_3 = bias_3
            elif isinstance(bias_3, int) or isinstance(bias_3, float):
                bias_3 = types.Real(bias_3)
            elif isinstance(bias_3, str):
                bias_3 = types.Real.from_mcnp(bias_3)

        if bias_3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_3)

        self._bias_3: types.Real = bias_3

    @property
    def bias_4(self) -> types.Real:
        """
        Bias factor #4 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_4

    @bias_4.setter
    def bias_4(self, bias_4: str | int | float | types.Real) -> None:
        """
        Sets `bias_4`.

        Parameters:
            bias_4: Bias factor #4 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_4 is not None:
            if isinstance(bias_4, types.Real):
                bias_4 = bias_4
            elif isinstance(bias_4, int) or isinstance(bias_4, float):
                bias_4 = types.Real(bias_4)
            elif isinstance(bias_4, str):
                bias_4 = types.Real.from_mcnp(bias_4)

        if bias_4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_4)

        self._bias_4: types.Real = bias_4

    @property
    def bias_5(self) -> types.Real:
        """
        Bias factor #5 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_5

    @bias_5.setter
    def bias_5(self, bias_5: str | int | float | types.Real) -> None:
        """
        Sets `bias_5`.

        Parameters:
            bias_5: Bias factor #5 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_5 is not None:
            if isinstance(bias_5, types.Real):
                bias_5 = bias_5
            elif isinstance(bias_5, int) or isinstance(bias_5, float):
                bias_5 = types.Real(bias_5)
            elif isinstance(bias_5, str):
                bias_5 = types.Real.from_mcnp(bias_5)

        if bias_5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_5)

        self._bias_5: types.Real = bias_5

    @property
    def bias_6(self) -> types.Real:
        """
        Bias factor #6 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_6

    @bias_6.setter
    def bias_6(self, bias_6: str | int | float | types.Real) -> None:
        """
        Sets `bias_6`.

        Parameters:
            bias_6: Bias factor #6 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_6 is not None:
            if isinstance(bias_6, types.Real):
                bias_6 = bias_6
            elif isinstance(bias_6, int) or isinstance(bias_6, float):
                bias_6 = types.Real(bias_6)
            elif isinstance(bias_6, str):
                bias_6 = types.Real.from_mcnp(bias_6)

        if bias_6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_6)

        self._bias_6: types.Real = bias_6

    @property
    def bias_7(self) -> types.Real:
        """
        Bias factor #7 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_7

    @bias_7.setter
    def bias_7(self, bias_7: str | int | float | types.Real) -> None:
        """
        Sets `bias_7`.

        Parameters:
            bias_7: Bias factor #7 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_7 is not None:
            if isinstance(bias_7, types.Real):
                bias_7 = bias_7
            elif isinstance(bias_7, int) or isinstance(bias_7, float):
                bias_7 = types.Real(bias_7)
            elif isinstance(bias_7, str):
                bias_7 = types.Real.from_mcnp(bias_7)

        if bias_7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_7)

        self._bias_7: types.Real = bias_7

    @property
    def bias_8(self) -> types.Real:
        """
        Bias factor #8 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_8

    @bias_8.setter
    def bias_8(self, bias_8: str | int | float | types.Real) -> None:
        """
        Sets `bias_8`.

        Parameters:
            bias_8: Bias factor #8 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_8 is not None:
            if isinstance(bias_8, types.Real):
                bias_8 = bias_8
            elif isinstance(bias_8, int) or isinstance(bias_8, float):
                bias_8 = types.Real(bias_8)
            elif isinstance(bias_8, str):
                bias_8 = types.Real.from_mcnp(bias_8)

        if bias_8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_8)

        self._bias_8: types.Real = bias_8

    @property
    def bias_9(self) -> types.Real:
        """
        Bias factor #9 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_9

    @bias_9.setter
    def bias_9(self, bias_9: str | int | float | types.Real) -> None:
        """
        Sets `bias_9`.

        Parameters:
            bias_9: Bias factor #9 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_9 is not None:
            if isinstance(bias_9, types.Real):
                bias_9 = bias_9
            elif isinstance(bias_9, int) or isinstance(bias_9, float):
                bias_9 = types.Real(bias_9)
            elif isinstance(bias_9, str):
                bias_9 = types.Real.from_mcnp(bias_9)

        if bias_9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_9)

        self._bias_9: types.Real = bias_9

    @property
    def bias_10(self) -> types.Real:
        """
        Bias factor #10 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_10

    @bias_10.setter
    def bias_10(self, bias_10: str | int | float | types.Real) -> None:
        """
        Sets `bias_10`.

        Parameters:
            bias_10: Bias factor #10 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_10 is not None:
            if isinstance(bias_10, types.Real):
                bias_10 = bias_10
            elif isinstance(bias_10, int) or isinstance(bias_10, float):
                bias_10 = types.Real(bias_10)
            elif isinstance(bias_10, str):
                bias_10 = types.Real.from_mcnp(bias_10)

        if bias_10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_10)

        self._bias_10: types.Real = bias_10

    @property
    def bias_11(self) -> types.Real:
        """
        Bias factor #11 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_11

    @bias_11.setter
    def bias_11(self, bias_11: str | int | float | types.Real) -> None:
        """
        Sets `bias_11`.

        Parameters:
            bias_11: Bias factor #11 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_11 is not None:
            if isinstance(bias_11, types.Real):
                bias_11 = bias_11
            elif isinstance(bias_11, int) or isinstance(bias_11, float):
                bias_11 = types.Real(bias_11)
            elif isinstance(bias_11, str):
                bias_11 = types.Real.from_mcnp(bias_11)

        if bias_11 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_11)

        self._bias_11: types.Real = bias_11

    @property
    def bias_12(self) -> types.Real:
        """
        Bias factor #12 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_12

    @bias_12.setter
    def bias_12(self, bias_12: str | int | float | types.Real) -> None:
        """
        Sets `bias_12`.

        Parameters:
            bias_12: Bias factor #12 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_12 is not None:
            if isinstance(bias_12, types.Real):
                bias_12 = bias_12
            elif isinstance(bias_12, int) or isinstance(bias_12, float):
                bias_12 = types.Real(bias_12)
            elif isinstance(bias_12, str):
                bias_12 = types.Real.from_mcnp(bias_12)

        if bias_12 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_12)

        self._bias_12: types.Real = bias_12

    @property
    def bias_13(self) -> types.Real:
        """
        Bias factor #13 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_13

    @bias_13.setter
    def bias_13(self, bias_13: str | int | float | types.Real) -> None:
        """
        Sets `bias_13`.

        Parameters:
            bias_13: Bias factor #13 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_13 is not None:
            if isinstance(bias_13, types.Real):
                bias_13 = bias_13
            elif isinstance(bias_13, int) or isinstance(bias_13, float):
                bias_13 = types.Real(bias_13)
            elif isinstance(bias_13, str):
                bias_13 = types.Real.from_mcnp(bias_13)

        if bias_13 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_13)

        self._bias_13: types.Real = bias_13

    @property
    def bias_14(self) -> types.Real:
        """
        Bias factor #14 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_14

    @bias_14.setter
    def bias_14(self, bias_14: str | int | float | types.Real) -> None:
        """
        Sets `bias_14`.

        Parameters:
            bias_14: Bias factor #14 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_14 is not None:
            if isinstance(bias_14, types.Real):
                bias_14 = bias_14
            elif isinstance(bias_14, int) or isinstance(bias_14, float):
                bias_14 = types.Real(bias_14)
            elif isinstance(bias_14, str):
                bias_14 = types.Real.from_mcnp(bias_14)

        if bias_14 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_14)

        self._bias_14: types.Real = bias_14

    @property
    def bias_15(self) -> types.Real:
        """
        Bias factor #15 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_15

    @bias_15.setter
    def bias_15(self, bias_15: str | int | float | types.Real) -> None:
        """
        Sets `bias_15`.

        Parameters:
            bias_15: Bias factor #15 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_15 is not None:
            if isinstance(bias_15, types.Real):
                bias_15 = bias_15
            elif isinstance(bias_15, int) or isinstance(bias_15, float):
                bias_15 = types.Real(bias_15)
            elif isinstance(bias_15, str):
                bias_15 = types.Real.from_mcnp(bias_15)

        if bias_15 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_15)

        self._bias_15: types.Real = bias_15

    @property
    def bias_16(self) -> types.Real:
        """
        Bias factor #16 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_16

    @bias_16.setter
    def bias_16(self, bias_16: str | int | float | types.Real) -> None:
        """
        Sets `bias_16`.

        Parameters:
            bias_16: Bias factor #16 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_16 is not None:
            if isinstance(bias_16, types.Real):
                bias_16 = bias_16
            elif isinstance(bias_16, int) or isinstance(bias_16, float):
                bias_16 = types.Real(bias_16)
            elif isinstance(bias_16, str):
                bias_16 = types.Real.from_mcnp(bias_16)

        if bias_16 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_16)

        self._bias_16: types.Real = bias_16

    @property
    def bias_17(self) -> types.Real:
        """
        Bias factor #17 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_17

    @bias_17.setter
    def bias_17(self, bias_17: str | int | float | types.Real) -> None:
        """
        Sets `bias_17`.

        Parameters:
            bias_17: Bias factor #17 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_17 is not None:
            if isinstance(bias_17, types.Real):
                bias_17 = bias_17
            elif isinstance(bias_17, int) or isinstance(bias_17, float):
                bias_17 = types.Real(bias_17)
            elif isinstance(bias_17, str):
                bias_17 = types.Real.from_mcnp(bias_17)

        if bias_17 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_17)

        self._bias_17: types.Real = bias_17

    @property
    def bias_18(self) -> types.Real:
        """
        Bias factor #18 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_18

    @bias_18.setter
    def bias_18(self, bias_18: str | int | float | types.Real) -> None:
        """
        Sets `bias_18`.

        Parameters:
            bias_18: Bias factor #18 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_18 is not None:
            if isinstance(bias_18, types.Real):
                bias_18 = bias_18
            elif isinstance(bias_18, int) or isinstance(bias_18, float):
                bias_18 = types.Real(bias_18)
            elif isinstance(bias_18, str):
                bias_18 = types.Real.from_mcnp(bias_18)

        if bias_18 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_18)

        self._bias_18: types.Real = bias_18

    @property
    def bias_19(self) -> types.Real:
        """
        Bias factor #19 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_19

    @bias_19.setter
    def bias_19(self, bias_19: str | int | float | types.Real) -> None:
        """
        Sets `bias_19`.

        Parameters:
            bias_19: Bias factor #19 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_19 is not None:
            if isinstance(bias_19, types.Real):
                bias_19 = bias_19
            elif isinstance(bias_19, int) or isinstance(bias_19, float):
                bias_19 = types.Real(bias_19)
            elif isinstance(bias_19, str):
                bias_19 = types.Real.from_mcnp(bias_19)

        if bias_19 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_19)

        self._bias_19: types.Real = bias_19

    @property
    def bias_20(self) -> types.Real:
        """
        Bias factor #20 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_20

    @bias_20.setter
    def bias_20(self, bias_20: str | int | float | types.Real) -> None:
        """
        Sets `bias_20`.

        Parameters:
            bias_20: Bias factor #20 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_20 is not None:
            if isinstance(bias_20, types.Real):
                bias_20 = bias_20
            elif isinstance(bias_20, int) or isinstance(bias_20, float):
                bias_20 = types.Real(bias_20)
            elif isinstance(bias_20, str):
                bias_20 = types.Real.from_mcnp(bias_20)

        if bias_20 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_20)

        self._bias_20: types.Real = bias_20

    @property
    def bias_21(self) -> types.Real:
        """
        Bias factor #21 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_21

    @bias_21.setter
    def bias_21(self, bias_21: str | int | float | types.Real) -> None:
        """
        Sets `bias_21`.

        Parameters:
            bias_21: Bias factor #21 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_21 is not None:
            if isinstance(bias_21, types.Real):
                bias_21 = bias_21
            elif isinstance(bias_21, int) or isinstance(bias_21, float):
                bias_21 = types.Real(bias_21)
            elif isinstance(bias_21, str):
                bias_21 = types.Real.from_mcnp(bias_21)

        if bias_21 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_21)

        self._bias_21: types.Real = bias_21

    @property
    def bias_22(self) -> types.Real:
        """
        Bias factor #22 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_22

    @bias_22.setter
    def bias_22(self, bias_22: str | int | float | types.Real) -> None:
        """
        Sets `bias_22`.

        Parameters:
            bias_22: Bias factor #22 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_22 is not None:
            if isinstance(bias_22, types.Real):
                bias_22 = bias_22
            elif isinstance(bias_22, int) or isinstance(bias_22, float):
                bias_22 = types.Real(bias_22)
            elif isinstance(bias_22, str):
                bias_22 = types.Real.from_mcnp(bias_22)

        if bias_22 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_22)

        self._bias_22: types.Real = bias_22

    @property
    def bias_23(self) -> types.Real:
        """
        Bias factor #23 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_23

    @bias_23.setter
    def bias_23(self, bias_23: str | int | float | types.Real) -> None:
        """
        Sets `bias_23`.

        Parameters:
            bias_23: Bias factor #23 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_23 is not None:
            if isinstance(bias_23, types.Real):
                bias_23 = bias_23
            elif isinstance(bias_23, int) or isinstance(bias_23, float):
                bias_23 = types.Real(bias_23)
            elif isinstance(bias_23, str):
                bias_23 = types.Real.from_mcnp(bias_23)

        if bias_23 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_23)

        self._bias_23: types.Real = bias_23

    @property
    def bias_24(self) -> types.Real:
        """
        Bias factor #24 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_24

    @bias_24.setter
    def bias_24(self, bias_24: str | int | float | types.Real) -> None:
        """
        Sets `bias_24`.

        Parameters:
            bias_24: Bias factor #24 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_24 is not None:
            if isinstance(bias_24, types.Real):
                bias_24 = bias_24
            elif isinstance(bias_24, int) or isinstance(bias_24, float):
                bias_24 = types.Real(bias_24)
            elif isinstance(bias_24, str):
                bias_24 = types.Real.from_mcnp(bias_24)

        if bias_24 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_24)

        self._bias_24: types.Real = bias_24

    @property
    def bias_25(self) -> types.Real:
        """
        Bias factor #25 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_25

    @bias_25.setter
    def bias_25(self, bias_25: str | int | float | types.Real) -> None:
        """
        Sets `bias_25`.

        Parameters:
            bias_25: Bias factor #25 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_25 is not None:
            if isinstance(bias_25, types.Real):
                bias_25 = bias_25
            elif isinstance(bias_25, int) or isinstance(bias_25, float):
                bias_25 = types.Real(bias_25)
            elif isinstance(bias_25, str):
                bias_25 = types.Real.from_mcnp(bias_25)

        if bias_25 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_25)

        self._bias_25: types.Real = bias_25

    @property
    def bias_26(self) -> types.Real:
        """
        Bias factor #26 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_26

    @bias_26.setter
    def bias_26(self, bias_26: str | int | float | types.Real) -> None:
        """
        Sets `bias_26`.

        Parameters:
            bias_26: Bias factor #26 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_26 is not None:
            if isinstance(bias_26, types.Real):
                bias_26 = bias_26
            elif isinstance(bias_26, int) or isinstance(bias_26, float):
                bias_26 = types.Real(bias_26)
            elif isinstance(bias_26, str):
                bias_26 = types.Real.from_mcnp(bias_26)

        if bias_26 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_26)

        self._bias_26: types.Real = bias_26

    @property
    def bias_27(self) -> types.Real:
        """
        Bias factor #27 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_27

    @bias_27.setter
    def bias_27(self, bias_27: str | int | float | types.Real) -> None:
        """
        Sets `bias_27`.

        Parameters:
            bias_27: Bias factor #27 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_27 is not None:
            if isinstance(bias_27, types.Real):
                bias_27 = bias_27
            elif isinstance(bias_27, int) or isinstance(bias_27, float):
                bias_27 = types.Real(bias_27)
            elif isinstance(bias_27, str):
                bias_27 = types.Real.from_mcnp(bias_27)

        if bias_27 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_27)

        self._bias_27: types.Real = bias_27

    @property
    def bias_28(self) -> types.Real:
        """
        Bias factor #28 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_28

    @bias_28.setter
    def bias_28(self, bias_28: str | int | float | types.Real) -> None:
        """
        Sets `bias_28`.

        Parameters:
            bias_28: Bias factor #28 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_28 is not None:
            if isinstance(bias_28, types.Real):
                bias_28 = bias_28
            elif isinstance(bias_28, int) or isinstance(bias_28, float):
                bias_28 = types.Real(bias_28)
            elif isinstance(bias_28, str):
                bias_28 = types.Real.from_mcnp(bias_28)

        if bias_28 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_28)

        self._bias_28: types.Real = bias_28

    @property
    def bias_29(self) -> types.Real:
        """
        Bias factor #29 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_29

    @bias_29.setter
    def bias_29(self, bias_29: str | int | float | types.Real) -> None:
        """
        Sets `bias_29`.

        Parameters:
            bias_29: Bias factor #29 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_29 is not None:
            if isinstance(bias_29, types.Real):
                bias_29 = bias_29
            elif isinstance(bias_29, int) or isinstance(bias_29, float):
                bias_29 = types.Real(bias_29)
            elif isinstance(bias_29, str):
                bias_29 = types.Real.from_mcnp(bias_29)

        if bias_29 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_29)

        self._bias_29: types.Real = bias_29

    @property
    def bias_30(self) -> types.Real:
        """
        Bias factor #30 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_30

    @bias_30.setter
    def bias_30(self, bias_30: str | int | float | types.Real) -> None:
        """
        Sets `bias_30`.

        Parameters:
            bias_30: Bias factor #30 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_30 is not None:
            if isinstance(bias_30, types.Real):
                bias_30 = bias_30
            elif isinstance(bias_30, int) or isinstance(bias_30, float):
                bias_30 = types.Real(bias_30)
            elif isinstance(bias_30, str):
                bias_30 = types.Real.from_mcnp(bias_30)

        if bias_30 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_30)

        self._bias_30: types.Real = bias_30

    @property
    def bias_31(self) -> types.Real:
        """
        Bias factor #31 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_31

    @bias_31.setter
    def bias_31(self, bias_31: str | int | float | types.Real) -> None:
        """
        Sets `bias_31`.

        Parameters:
            bias_31: Bias factor #31 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_31 is not None:
            if isinstance(bias_31, types.Real):
                bias_31 = bias_31
            elif isinstance(bias_31, int) or isinstance(bias_31, float):
                bias_31 = types.Real(bias_31)
            elif isinstance(bias_31, str):
                bias_31 = types.Real.from_mcnp(bias_31)

        if bias_31 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_31)

        self._bias_31: types.Real = bias_31

    @property
    def bias_32(self) -> types.Real:
        """
        Bias factor #32 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_32

    @bias_32.setter
    def bias_32(self, bias_32: str | int | float | types.Real) -> None:
        """
        Sets `bias_32`.

        Parameters:
            bias_32: Bias factor #32 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_32 is not None:
            if isinstance(bias_32, types.Real):
                bias_32 = bias_32
            elif isinstance(bias_32, int) or isinstance(bias_32, float):
                bias_32 = types.Real(bias_32)
            elif isinstance(bias_32, str):
                bias_32 = types.Real.from_mcnp(bias_32)

        if bias_32 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_32)

        self._bias_32: types.Real = bias_32

    @property
    def bias_33(self) -> types.Real:
        """
        Bias factor #33 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_33

    @bias_33.setter
    def bias_33(self, bias_33: str | int | float | types.Real) -> None:
        """
        Sets `bias_33`.

        Parameters:
            bias_33: Bias factor #33 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_33 is not None:
            if isinstance(bias_33, types.Real):
                bias_33 = bias_33
            elif isinstance(bias_33, int) or isinstance(bias_33, float):
                bias_33 = types.Real(bias_33)
            elif isinstance(bias_33, str):
                bias_33 = types.Real.from_mcnp(bias_33)

        if bias_33 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_33)

        self._bias_33: types.Real = bias_33

    @property
    def bias_34(self) -> types.Real:
        """
        Bias factor #34 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_34

    @bias_34.setter
    def bias_34(self, bias_34: str | int | float | types.Real) -> None:
        """
        Sets `bias_34`.

        Parameters:
            bias_34: Bias factor #34 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_34 is not None:
            if isinstance(bias_34, types.Real):
                bias_34 = bias_34
            elif isinstance(bias_34, int) or isinstance(bias_34, float):
                bias_34 = types.Real(bias_34)
            elif isinstance(bias_34, str):
                bias_34 = types.Real.from_mcnp(bias_34)

        if bias_34 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_34)

        self._bias_34: types.Real = bias_34

    @property
    def bias_35(self) -> types.Real:
        """
        Bias factor #35 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_35

    @bias_35.setter
    def bias_35(self, bias_35: str | int | float | types.Real) -> None:
        """
        Sets `bias_35`.

        Parameters:
            bias_35: Bias factor #35 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_35 is not None:
            if isinstance(bias_35, types.Real):
                bias_35 = bias_35
            elif isinstance(bias_35, int) or isinstance(bias_35, float):
                bias_35 = types.Real(bias_35)
            elif isinstance(bias_35, str):
                bias_35 = types.Real.from_mcnp(bias_35)

        if bias_35 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_35)

        self._bias_35: types.Real = bias_35

    @property
    def bias_36(self) -> types.Real:
        """
        Bias factor #36 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_36

    @bias_36.setter
    def bias_36(self, bias_36: str | int | float | types.Real) -> None:
        """
        Sets `bias_36`.

        Parameters:
            bias_36: Bias factor #36 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_36 is not None:
            if isinstance(bias_36, types.Real):
                bias_36 = bias_36
            elif isinstance(bias_36, int) or isinstance(bias_36, float):
                bias_36 = types.Real(bias_36)
            elif isinstance(bias_36, str):
                bias_36 = types.Real.from_mcnp(bias_36)

        if bias_36 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_36)

        self._bias_36: types.Real = bias_36

    @property
    def bias_37(self) -> types.Real:
        """
        Bias factor #37 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_37

    @bias_37.setter
    def bias_37(self, bias_37: str | int | float | types.Real) -> None:
        """
        Sets `bias_37`.

        Parameters:
            bias_37: Bias factor #37 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_37 is not None:
            if isinstance(bias_37, types.Real):
                bias_37 = bias_37
            elif isinstance(bias_37, int) or isinstance(bias_37, float):
                bias_37 = types.Real(bias_37)
            elif isinstance(bias_37, str):
                bias_37 = types.Real.from_mcnp(bias_37)

        if bias_37 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_37)

        self._bias_37: types.Real = bias_37

    @property
    def bias_38(self) -> types.Real:
        """
        Bias factor #38 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_38

    @bias_38.setter
    def bias_38(self, bias_38: str | int | float | types.Real) -> None:
        """
        Sets `bias_38`.

        Parameters:
            bias_38: Bias factor #38 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_38 is not None:
            if isinstance(bias_38, types.Real):
                bias_38 = bias_38
            elif isinstance(bias_38, int) or isinstance(bias_38, float):
                bias_38 = types.Real(bias_38)
            elif isinstance(bias_38, str):
                bias_38 = types.Real.from_mcnp(bias_38)

        if bias_38 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_38)

        self._bias_38: types.Real = bias_38

    @property
    def bias_39(self) -> types.Real:
        """
        Bias factor #39 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_39

    @bias_39.setter
    def bias_39(self, bias_39: str | int | float | types.Real) -> None:
        """
        Sets `bias_39`.

        Parameters:
            bias_39: Bias factor #39 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_39 is not None:
            if isinstance(bias_39, types.Real):
                bias_39 = bias_39
            elif isinstance(bias_39, int) or isinstance(bias_39, float):
                bias_39 = types.Real(bias_39)
            elif isinstance(bias_39, str):
                bias_39 = types.Real.from_mcnp(bias_39)

        if bias_39 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_39)

        self._bias_39: types.Real = bias_39

    @property
    def bias_40(self) -> types.Real:
        """
        Bias factor #40 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_40

    @bias_40.setter
    def bias_40(self, bias_40: str | int | float | types.Real) -> None:
        """
        Sets `bias_40`.

        Parameters:
            bias_40: Bias factor #40 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_40 is not None:
            if isinstance(bias_40, types.Real):
                bias_40 = bias_40
            elif isinstance(bias_40, int) or isinstance(bias_40, float):
                bias_40 = types.Real(bias_40)
            elif isinstance(bias_40, str):
                bias_40 = types.Real.from_mcnp(bias_40)

        if bias_40 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_40)

        self._bias_40: types.Real = bias_40

    @property
    def bias_41(self) -> types.Real:
        """
        Bias factor #41 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_41

    @bias_41.setter
    def bias_41(self, bias_41: str | int | float | types.Real) -> None:
        """
        Sets `bias_41`.

        Parameters:
            bias_41: Bias factor #41 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_41 is not None:
            if isinstance(bias_41, types.Real):
                bias_41 = bias_41
            elif isinstance(bias_41, int) or isinstance(bias_41, float):
                bias_41 = types.Real(bias_41)
            elif isinstance(bias_41, str):
                bias_41 = types.Real.from_mcnp(bias_41)

        if bias_41 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_41)

        self._bias_41: types.Real = bias_41

    @property
    def bias_42(self) -> types.Real:
        """
        Bias factor #42 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_42

    @bias_42.setter
    def bias_42(self, bias_42: str | int | float | types.Real) -> None:
        """
        Sets `bias_42`.

        Parameters:
            bias_42: Bias factor #42 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_42 is not None:
            if isinstance(bias_42, types.Real):
                bias_42 = bias_42
            elif isinstance(bias_42, int) or isinstance(bias_42, float):
                bias_42 = types.Real(bias_42)
            elif isinstance(bias_42, str):
                bias_42 = types.Real.from_mcnp(bias_42)

        if bias_42 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_42)

        self._bias_42: types.Real = bias_42

    @property
    def bias_43(self) -> types.Real:
        """
        Bias factor #43 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_43

    @bias_43.setter
    def bias_43(self, bias_43: str | int | float | types.Real) -> None:
        """
        Sets `bias_43`.

        Parameters:
            bias_43: Bias factor #43 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_43 is not None:
            if isinstance(bias_43, types.Real):
                bias_43 = bias_43
            elif isinstance(bias_43, int) or isinstance(bias_43, float):
                bias_43 = types.Real(bias_43)
            elif isinstance(bias_43, str):
                bias_43 = types.Real.from_mcnp(bias_43)

        if bias_43 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_43)

        self._bias_43: types.Real = bias_43

    @property
    def bias_44(self) -> types.Real:
        """
        Bias factor #44 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_44

    @bias_44.setter
    def bias_44(self, bias_44: str | int | float | types.Real) -> None:
        """
        Sets `bias_44`.

        Parameters:
            bias_44: Bias factor #44 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_44 is not None:
            if isinstance(bias_44, types.Real):
                bias_44 = bias_44
            elif isinstance(bias_44, int) or isinstance(bias_44, float):
                bias_44 = types.Real(bias_44)
            elif isinstance(bias_44, str):
                bias_44 = types.Real.from_mcnp(bias_44)

        if bias_44 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_44)

        self._bias_44: types.Real = bias_44

    @property
    def bias_45(self) -> types.Real:
        """
        Bias factor #45 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_45

    @bias_45.setter
    def bias_45(self, bias_45: str | int | float | types.Real) -> None:
        """
        Sets `bias_45`.

        Parameters:
            bias_45: Bias factor #45 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_45 is not None:
            if isinstance(bias_45, types.Real):
                bias_45 = bias_45
            elif isinstance(bias_45, int) or isinstance(bias_45, float):
                bias_45 = types.Real(bias_45)
            elif isinstance(bias_45, str):
                bias_45 = types.Real.from_mcnp(bias_45)

        if bias_45 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_45)

        self._bias_45: types.Real = bias_45

    @property
    def bias_46(self) -> types.Real:
        """
        Bias factor #46 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_46

    @bias_46.setter
    def bias_46(self, bias_46: str | int | float | types.Real) -> None:
        """
        Sets `bias_46`.

        Parameters:
            bias_46: Bias factor #46 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_46 is not None:
            if isinstance(bias_46, types.Real):
                bias_46 = bias_46
            elif isinstance(bias_46, int) or isinstance(bias_46, float):
                bias_46 = types.Real(bias_46)
            elif isinstance(bias_46, str):
                bias_46 = types.Real.from_mcnp(bias_46)

        if bias_46 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_46)

        self._bias_46: types.Real = bias_46

    @property
    def bias_47(self) -> types.Real:
        """
        Bias factor #47 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_47

    @bias_47.setter
    def bias_47(self, bias_47: str | int | float | types.Real) -> None:
        """
        Sets `bias_47`.

        Parameters:
            bias_47: Bias factor #47 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_47 is not None:
            if isinstance(bias_47, types.Real):
                bias_47 = bias_47
            elif isinstance(bias_47, int) or isinstance(bias_47, float):
                bias_47 = types.Real(bias_47)
            elif isinstance(bias_47, str):
                bias_47 = types.Real.from_mcnp(bias_47)

        if bias_47 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_47)

        self._bias_47: types.Real = bias_47

    @property
    def bias_48(self) -> types.Real:
        """
        Bias factor #48 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_48

    @bias_48.setter
    def bias_48(self, bias_48: str | int | float | types.Real) -> None:
        """
        Sets `bias_48`.

        Parameters:
            bias_48: Bias factor #48 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_48 is not None:
            if isinstance(bias_48, types.Real):
                bias_48 = bias_48
            elif isinstance(bias_48, int) or isinstance(bias_48, float):
                bias_48 = types.Real(bias_48)
            elif isinstance(bias_48, str):
                bias_48 = types.Real.from_mcnp(bias_48)

        if bias_48 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_48)

        self._bias_48: types.Real = bias_48

    @property
    def bias_49(self) -> types.Real:
        """
        Bias factor #49 for bremsstrahlung specturm

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._bias_49

    @bias_49.setter
    def bias_49(self, bias_49: str | int | float | types.Real) -> None:
        """
        Sets `bias_49`.

        Parameters:
            bias_49: Bias factor #49 for bremsstrahlung specturm.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if bias_49 is not None:
            if isinstance(bias_49, types.Real):
                bias_49 = bias_49
            elif isinstance(bias_49, int) or isinstance(bias_49, float):
                bias_49 = types.Real(bias_49)
            elif isinstance(bias_49, str):
                bias_49 = types.Real.from_mcnp(bias_49)

        if bias_49 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, bias_49)

        self._bias_49: types.Real = bias_49

    @property
    def materials(self) -> types.Tuple(types.Integer):
        """
        Material to bias

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._materials

    @materials.setter
    def materials(self, materials: list[str] | list[int] | list[types.Integer]) -> None:
        """
        Sets `materials`.

        Parameters:
            materials: Material to bias.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if materials is not None:
            array = []
            for item in materials:
                if isinstance(item, types.Integer):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Integer(item))
                elif isinstance(item, str):
                    array.append(types.Integer.from_mcnp(item))
            materials = types.Tuple(types.Integer)(array)

        if materials is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, materials)

        self._materials: types.Tuple(types.Integer) = materials
