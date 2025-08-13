import re

from . import _card
from .. import types


class Lcb(_card.Card):
    """
    Represents INP `lcb` cards.
    """

    _KEYWORD = 'lcb'

    _ATTRS = {
        'flenb1': types.Real,
        'flenb2': types.Real,
        'flenb3': types.Real,
        'flenb4': types.Real,
        'flenb5': types.Real,
        'flenb6': types.Real,
        'cotfe': types.Real,
        'film0': types.Real,
    }

    _REGEX = re.compile(
        rf'\Alcb( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        flenb1: str | int | float | types.Real = None,
        flenb2: str | int | float | types.Real = None,
        flenb3: str | int | float | types.Real = None,
        flenb4: str | int | float | types.Real = None,
        flenb5: str | int | float | types.Real = None,
        flenb6: str | int | float | types.Real = None,
        cotfe: str | int | float | types.Real = None,
        film0: str | int | float | types.Real = None,
    ):
        """
        Initializes `Lcb`.

        Parameters:
            flenb1: Kinetic energy for nucleons CEM/Bertini/INCL.
            flenb2: Kinetic energy for nucleons LAQGSM03.03.
            flenb3: Kinetic energy for pions CEM/Bertini/INCL.
            flenb4: Kinetic energy for pions LAQGSM03.03.
            flenb5: Kinetic energy for nucleons ISABEL.
            flenb6: Kinetic energy for appropriate model.
            cotfe: Cutoff kinetic energy for particle escape.
            film0: Maximum correction allowed for masss-energy balancing.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.flenb1: types.Real = flenb1
        self.flenb2: types.Real = flenb2
        self.flenb3: types.Real = flenb3
        self.flenb4: types.Real = flenb4
        self.flenb5: types.Real = flenb5
        self.flenb6: types.Real = flenb6
        self.cotfe: types.Real = cotfe
        self.film0: types.Real = film0

    @property
    def flenb1(self) -> types.Real:
        """
        Kinetic energy for nucleons CEM/Bertini/INCL

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._flenb1

    @flenb1.setter
    def flenb1(self, flenb1: str | int | float | types.Real) -> None:
        """
        Sets `flenb1`.

        Parameters:
            flenb1: Kinetic energy for nucleons CEM/Bertini/INCL.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if flenb1 is not None:
            if isinstance(flenb1, types.Real):
                flenb1 = flenb1
            elif isinstance(flenb1, int) or isinstance(flenb1, float):
                flenb1 = types.Real(flenb1)
            elif isinstance(flenb1, str):
                flenb1 = types.Real.from_mcnp(flenb1)

        self._flenb1: types.Real = flenb1

    @property
    def flenb2(self) -> types.Real:
        """
        Kinetic energy for nucleons LAQGSM03.03

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._flenb2

    @flenb2.setter
    def flenb2(self, flenb2: str | int | float | types.Real) -> None:
        """
        Sets `flenb2`.

        Parameters:
            flenb2: Kinetic energy for nucleons LAQGSM03.03.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if flenb2 is not None:
            if isinstance(flenb2, types.Real):
                flenb2 = flenb2
            elif isinstance(flenb2, int) or isinstance(flenb2, float):
                flenb2 = types.Real(flenb2)
            elif isinstance(flenb2, str):
                flenb2 = types.Real.from_mcnp(flenb2)

        self._flenb2: types.Real = flenb2

    @property
    def flenb3(self) -> types.Real:
        """
        Kinetic energy for pions CEM/Bertini/INCL

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._flenb3

    @flenb3.setter
    def flenb3(self, flenb3: str | int | float | types.Real) -> None:
        """
        Sets `flenb3`.

        Parameters:
            flenb3: Kinetic energy for pions CEM/Bertini/INCL.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if flenb3 is not None:
            if isinstance(flenb3, types.Real):
                flenb3 = flenb3
            elif isinstance(flenb3, int) or isinstance(flenb3, float):
                flenb3 = types.Real(flenb3)
            elif isinstance(flenb3, str):
                flenb3 = types.Real.from_mcnp(flenb3)

        self._flenb3: types.Real = flenb3

    @property
    def flenb4(self) -> types.Real:
        """
        Kinetic energy for pions LAQGSM03.03

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._flenb4

    @flenb4.setter
    def flenb4(self, flenb4: str | int | float | types.Real) -> None:
        """
        Sets `flenb4`.

        Parameters:
            flenb4: Kinetic energy for pions LAQGSM03.03.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if flenb4 is not None:
            if isinstance(flenb4, types.Real):
                flenb4 = flenb4
            elif isinstance(flenb4, int) or isinstance(flenb4, float):
                flenb4 = types.Real(flenb4)
            elif isinstance(flenb4, str):
                flenb4 = types.Real.from_mcnp(flenb4)

        self._flenb4: types.Real = flenb4

    @property
    def flenb5(self) -> types.Real:
        """
        Kinetic energy for nucleons ISABEL

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._flenb5

    @flenb5.setter
    def flenb5(self, flenb5: str | int | float | types.Real) -> None:
        """
        Sets `flenb5`.

        Parameters:
            flenb5: Kinetic energy for nucleons ISABEL.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if flenb5 is not None:
            if isinstance(flenb5, types.Real):
                flenb5 = flenb5
            elif isinstance(flenb5, int) or isinstance(flenb5, float):
                flenb5 = types.Real(flenb5)
            elif isinstance(flenb5, str):
                flenb5 = types.Real.from_mcnp(flenb5)

        self._flenb5: types.Real = flenb5

    @property
    def flenb6(self) -> types.Real:
        """
        Kinetic energy for appropriate model

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._flenb6

    @flenb6.setter
    def flenb6(self, flenb6: str | int | float | types.Real) -> None:
        """
        Sets `flenb6`.

        Parameters:
            flenb6: Kinetic energy for appropriate model.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if flenb6 is not None:
            if isinstance(flenb6, types.Real):
                flenb6 = flenb6
            elif isinstance(flenb6, int) or isinstance(flenb6, float):
                flenb6 = types.Real(flenb6)
            elif isinstance(flenb6, str):
                flenb6 = types.Real.from_mcnp(flenb6)

        self._flenb6: types.Real = flenb6

    @property
    def cotfe(self) -> types.Real:
        """
        Cutoff kinetic energy for particle escape

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._cotfe

    @cotfe.setter
    def cotfe(self, cotfe: str | int | float | types.Real) -> None:
        """
        Sets `cotfe`.

        Parameters:
            cotfe: Cutoff kinetic energy for particle escape.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if cotfe is not None:
            if isinstance(cotfe, types.Real):
                cotfe = cotfe
            elif isinstance(cotfe, int) or isinstance(cotfe, float):
                cotfe = types.Real(cotfe)
            elif isinstance(cotfe, str):
                cotfe = types.Real.from_mcnp(cotfe)

        self._cotfe: types.Real = cotfe

    @property
    def film0(self) -> types.Real:
        """
        Maximum correction allowed for masss-energy balancing

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._film0

    @film0.setter
    def film0(self, film0: str | int | float | types.Real) -> None:
        """
        Sets `film0`.

        Parameters:
            film0: Maximum correction allowed for masss-energy balancing.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if film0 is not None:
            if isinstance(film0, types.Real):
                film0 = film0
            elif isinstance(film0, int) or isinstance(film0, float):
                film0 = types.Real(film0)
            elif isinstance(film0, str):
                film0 = types.Real.from_mcnp(film0)

        self._film0: types.Real = film0
