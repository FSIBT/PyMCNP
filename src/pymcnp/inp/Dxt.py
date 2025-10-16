import re

from . import dxt
from . import _card
from .. import types
from .. import errors


class Dxt(_card.Card):
    """
    Represents INP `dxt` cards.
    """

    _KEYWORD = 'dxt'

    _ATTRS = {
        'designator': types.Designator,
        'spheres_1': dxt.Shell,
        'spheres_2': dxt.Shell,
        'spheres_3': dxt.Shell,
        'spheres_4': dxt.Shell,
        'spheres_5': dxt.Shell,
        'spheres_6': dxt.Shell,
        'spheres_7': dxt.Shell,
        'spheres_8': dxt.Shell,
        'spheres_9': dxt.Shell,
        'spheres_10': dxt.Shell,
        'cutoff_1': types.Real,
        'cutoff_2': types.Real,
        'weight': types.Real,
    }

    _REGEX = re.compile(
        rf'\Adxt:(\S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( \S+ \S+ \S+ \S+ \S+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        designator: str | types.Designator,
        spheres_1: str | dxt.Shell,
        spheres_2: str | dxt.Shell,
        spheres_3: str | dxt.Shell,
        spheres_4: str | dxt.Shell,
        spheres_5: str | dxt.Shell,
        spheres_6: str | dxt.Shell,
        spheres_7: str | dxt.Shell,
        spheres_8: str | dxt.Shell,
        spheres_9: str | dxt.Shell,
        spheres_10: str | dxt.Shell,
        cutoff_1: str | int | float | types.Real,
        cutoff_2: str | int | float | types.Real,
        weight: str | int | float | types.Real,
    ):
        """
        Initializes `Dxt`.

        Parameters:
            designator: Data card particle designator.
            spheres_1: DXTRAN spheres #1.
            spheres_2: DXTRAN spheres #2.
            spheres_3: DXTRAN spheres #3.
            spheres_4: DXTRAN spheres #4.
            spheres_5: DXTRAN spheres #5.
            spheres_6: DXTRAN spheres #6.
            spheres_7: DXTRAN spheres #7.
            spheres_8: DXTRAN spheres #8.
            spheres_9: DXTRAN spheres #9.
            spheres_10: DXTRAN spheres #10.
            cutoff_1: Upper weight cutoff in the spheres.
            cutoff_2: Lower weight cutoff in the spheres.
            weight: Minimum photon weight.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.designator: types.Designator = designator
        self.spheres_1: dxt.Shell = spheres_1
        self.spheres_2: dxt.Shell = spheres_2
        self.spheres_3: dxt.Shell = spheres_3
        self.spheres_4: dxt.Shell = spheres_4
        self.spheres_5: dxt.Shell = spheres_5
        self.spheres_6: dxt.Shell = spheres_6
        self.spheres_7: dxt.Shell = spheres_7
        self.spheres_8: dxt.Shell = spheres_8
        self.spheres_9: dxt.Shell = spheres_9
        self.spheres_10: dxt.Shell = spheres_10
        self.cutoff_1: types.Real = cutoff_1
        self.cutoff_2: types.Real = cutoff_2
        self.weight: types.Real = weight

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
    def spheres_1(self) -> dxt.Shell:
        """
        DXTRAN spheres #1

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres_1

    @spheres_1.setter
    def spheres_1(self, spheres_1: str | dxt.Shell) -> None:
        """
        Sets `spheres_1`.

        Parameters:
            spheres_1: DXTRAN spheres #1.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres_1 is not None:
            if isinstance(spheres_1, dxt.Shell):
                spheres_1 = spheres_1
            elif isinstance(spheres_1, str):
                spheres_1 = dxt.Shell.from_mcnp(spheres_1)

        if spheres_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres_1)

        self._spheres_1: dxt.Shell = spheres_1

    @property
    def spheres_2(self) -> dxt.Shell:
        """
        DXTRAN spheres #2

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres_2

    @spheres_2.setter
    def spheres_2(self, spheres_2: str | dxt.Shell) -> None:
        """
        Sets `spheres_2`.

        Parameters:
            spheres_2: DXTRAN spheres #2.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres_2 is not None:
            if isinstance(spheres_2, dxt.Shell):
                spheres_2 = spheres_2
            elif isinstance(spheres_2, str):
                spheres_2 = dxt.Shell.from_mcnp(spheres_2)

        if spheres_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres_2)

        self._spheres_2: dxt.Shell = spheres_2

    @property
    def spheres_3(self) -> dxt.Shell:
        """
        DXTRAN spheres #3

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres_3

    @spheres_3.setter
    def spheres_3(self, spheres_3: str | dxt.Shell) -> None:
        """
        Sets `spheres_3`.

        Parameters:
            spheres_3: DXTRAN spheres #3.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres_3 is not None:
            if isinstance(spheres_3, dxt.Shell):
                spheres_3 = spheres_3
            elif isinstance(spheres_3, str):
                spheres_3 = dxt.Shell.from_mcnp(spheres_3)

        if spheres_3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres_3)

        self._spheres_3: dxt.Shell = spheres_3

    @property
    def spheres_4(self) -> dxt.Shell:
        """
        DXTRAN spheres #4

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres_4

    @spheres_4.setter
    def spheres_4(self, spheres_4: str | dxt.Shell) -> None:
        """
        Sets `spheres_4`.

        Parameters:
            spheres_4: DXTRAN spheres #4.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres_4 is not None:
            if isinstance(spheres_4, dxt.Shell):
                spheres_4 = spheres_4
            elif isinstance(spheres_4, str):
                spheres_4 = dxt.Shell.from_mcnp(spheres_4)

        if spheres_4 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres_4)

        self._spheres_4: dxt.Shell = spheres_4

    @property
    def spheres_5(self) -> dxt.Shell:
        """
        DXTRAN spheres #5

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres_5

    @spheres_5.setter
    def spheres_5(self, spheres_5: str | dxt.Shell) -> None:
        """
        Sets `spheres_5`.

        Parameters:
            spheres_5: DXTRAN spheres #5.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres_5 is not None:
            if isinstance(spheres_5, dxt.Shell):
                spheres_5 = spheres_5
            elif isinstance(spheres_5, str):
                spheres_5 = dxt.Shell.from_mcnp(spheres_5)

        if spheres_5 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres_5)

        self._spheres_5: dxt.Shell = spheres_5

    @property
    def spheres_6(self) -> dxt.Shell:
        """
        DXTRAN spheres #6

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres_6

    @spheres_6.setter
    def spheres_6(self, spheres_6: str | dxt.Shell) -> None:
        """
        Sets `spheres_6`.

        Parameters:
            spheres_6: DXTRAN spheres #6.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres_6 is not None:
            if isinstance(spheres_6, dxt.Shell):
                spheres_6 = spheres_6
            elif isinstance(spheres_6, str):
                spheres_6 = dxt.Shell.from_mcnp(spheres_6)

        if spheres_6 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres_6)

        self._spheres_6: dxt.Shell = spheres_6

    @property
    def spheres_7(self) -> dxt.Shell:
        """
        DXTRAN spheres #7

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres_7

    @spheres_7.setter
    def spheres_7(self, spheres_7: str | dxt.Shell) -> None:
        """
        Sets `spheres_7`.

        Parameters:
            spheres_7: DXTRAN spheres #7.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres_7 is not None:
            if isinstance(spheres_7, dxt.Shell):
                spheres_7 = spheres_7
            elif isinstance(spheres_7, str):
                spheres_7 = dxt.Shell.from_mcnp(spheres_7)

        if spheres_7 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres_7)

        self._spheres_7: dxt.Shell = spheres_7

    @property
    def spheres_8(self) -> dxt.Shell:
        """
        DXTRAN spheres #8

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres_8

    @spheres_8.setter
    def spheres_8(self, spheres_8: str | dxt.Shell) -> None:
        """
        Sets `spheres_8`.

        Parameters:
            spheres_8: DXTRAN spheres #8.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres_8 is not None:
            if isinstance(spheres_8, dxt.Shell):
                spheres_8 = spheres_8
            elif isinstance(spheres_8, str):
                spheres_8 = dxt.Shell.from_mcnp(spheres_8)

        if spheres_8 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres_8)

        self._spheres_8: dxt.Shell = spheres_8

    @property
    def spheres_9(self) -> dxt.Shell:
        """
        DXTRAN spheres #9

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres_9

    @spheres_9.setter
    def spheres_9(self, spheres_9: str | dxt.Shell) -> None:
        """
        Sets `spheres_9`.

        Parameters:
            spheres_9: DXTRAN spheres #9.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres_9 is not None:
            if isinstance(spheres_9, dxt.Shell):
                spheres_9 = spheres_9
            elif isinstance(spheres_9, str):
                spheres_9 = dxt.Shell.from_mcnp(spheres_9)

        if spheres_9 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres_9)

        self._spheres_9: dxt.Shell = spheres_9

    @property
    def spheres_10(self) -> dxt.Shell:
        """
        DXTRAN spheres #10

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._spheres_10

    @spheres_10.setter
    def spheres_10(self, spheres_10: str | dxt.Shell) -> None:
        """
        Sets `spheres_10`.

        Parameters:
            spheres_10: DXTRAN spheres #10.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if spheres_10 is not None:
            if isinstance(spheres_10, dxt.Shell):
                spheres_10 = spheres_10
            elif isinstance(spheres_10, str):
                spheres_10 = dxt.Shell.from_mcnp(spheres_10)

        if spheres_10 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, spheres_10)

        self._spheres_10: dxt.Shell = spheres_10

    @property
    def cutoff_1(self) -> types.Real:
        """
        Upper weight cutoff in the spheres

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._cutoff_1

    @cutoff_1.setter
    def cutoff_1(self, cutoff_1: str | int | float | types.Real) -> None:
        """
        Sets `cutoff_1`.

        Parameters:
            cutoff_1: Upper weight cutoff in the spheres.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if cutoff_1 is not None:
            if isinstance(cutoff_1, types.Real):
                cutoff_1 = cutoff_1
            elif isinstance(cutoff_1, int) or isinstance(cutoff_1, float):
                cutoff_1 = types.Real(cutoff_1)
            elif isinstance(cutoff_1, str):
                cutoff_1 = types.Real.from_mcnp(cutoff_1)

        if cutoff_1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, cutoff_1)

        self._cutoff_1: types.Real = cutoff_1

    @property
    def cutoff_2(self) -> types.Real:
        """
        Lower weight cutoff in the spheres

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._cutoff_2

    @cutoff_2.setter
    def cutoff_2(self, cutoff_2: str | int | float | types.Real) -> None:
        """
        Sets `cutoff_2`.

        Parameters:
            cutoff_2: Lower weight cutoff in the spheres.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if cutoff_2 is not None:
            if isinstance(cutoff_2, types.Real):
                cutoff_2 = cutoff_2
            elif isinstance(cutoff_2, int) or isinstance(cutoff_2, float):
                cutoff_2 = types.Real(cutoff_2)
            elif isinstance(cutoff_2, str):
                cutoff_2 = types.Real.from_mcnp(cutoff_2)

        if cutoff_2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, cutoff_2)

        self._cutoff_2: types.Real = cutoff_2

    @property
    def weight(self) -> types.Real:
        """
        Minimum photon weight

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._weight

    @weight.setter
    def weight(self, weight: str | int | float | types.Real) -> None:
        """
        Sets `weight`.

        Parameters:
            weight: Minimum photon weight.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if weight is not None:
            if isinstance(weight, types.Real):
                weight = weight
            elif isinstance(weight, int) or isinstance(weight, float):
                weight = types.Real(weight)
            elif isinstance(weight, str):
                weight = types.Real.from_mcnp(weight)

        if weight is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, weight)

        self._weight: types.Real = weight
