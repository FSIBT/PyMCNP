import re

from . import _option
from ...utils import types
from ...utils import errors


class Vol(_option.DataOption):
    """
    Represents INP vol elements.

    Attributes:
        no: Volume calculation on/off.
        volumes: Tuple of cell volumes.
    """

    _KEYWORD = 'vol'

    _ATTRS = {
        'no': types.String,
        'volumes': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Avol(?: (no))?((?: {types.Real._REGEX.pattern[2:-2]})+?)\Z')

    def __init__(self, volumes: list[str] | list[float] | list[types.Real], no: str | types.String = None):
        """
        Initializes ``Vol``.

        Parameters:
            no: Volume calculation on/off.
            volumes: Tuple of cell volumes.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.no: types.String = no
        self.volumes: types.Tuple[types.Real] = volumes

    @property
    def no(self) -> types.String:
        """
        Gets ``no``.

        Returns:
            ``no``.
        """

        return self._no

    @no.setter
    def no(self, no: str | types.String) -> None:
        """
        Sets ``no``.

        Parameters:
            no: Volume calculation on/off.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if no is not None:
            if isinstance(no, types.String):
                no = no
            elif isinstance(no, str):
                no = types.String.from_mcnp(no)
            else:
                raise TypeError

        if no is not None and no not in {'no'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, no)

        self._no: types.String = no

    @property
    def volumes(self) -> types.Tuple[types.Real]:
        """
        Gets ``volumes``.

        Returns:
            ``volumes``.
        """

        return self._volumes

    @volumes.setter
    def volumes(self, volumes: list[str] | list[float] | list[types.Real]) -> None:
        """
        Sets ``volumes``.

        Parameters:
            volumes: Tuple of cell volumes.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if volumes is not None:
            array = []
            for item in volumes:
                if isinstance(item, types.Real):
                    array.append(item)
                elif isinstance(item, int):
                    array.append(types.Real(item))
                elif isinstance(item, float):
                    array.append(types.Real(item))
                elif isinstance(item, str):
                    array.append(types.Real.from_mcnp(item))
                else:
                    raise TypeError
            volumes = types.Tuple(array)

        if volumes is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, volumes)

        self._volumes: types.Tuple[types.Real] = volumes
