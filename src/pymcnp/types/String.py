import re
import typing

from . import _type
from .Integer import Integer
from .. import errors


class String(_type.Type):
    """
    Represents MCNP strings.

    Attributes:
        value: String value.
    """

    _REGEX = re.compile(r'\A\S+\Z', re.IGNORECASE)

    def __init__(self, value: str):
        """
        Initializes `String`.

        Parameters:
            value: String value.

        Returns:
            `String`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[str] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `String` from MCNP.

        Praameters:
            source: MCNP string.

        Returns:
            `String`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        return String(source)

    def to_mcnp(self):
        """
        Generates MCNP from `String`.

        Returns:
            MCNP string.
        """

        return self.value

    def __hash__(self):
        return hash(self.value)

    def __iter__(self):
        return self.value.__iter__()

    def __len__(self):
        return self.value.__len__()

    def __getitem__(self, index: int | Integer):
        if isinstance(index, Integer):
            return self.value.__getitem__(index.value)
        else:
            return self.value.__getitem__(index)

    def __contains__(self, item):
        if isinstance(item, String):
            return self.value.__contains__(item.value)
        else:
            return self.value.__contains__(item)

    def __format__(self, spec):
        return self.value.__format__(spec)

    def __lt__(a, b):
        if isinstance(b, String):
            return a.value.__lt__(b.value)
        else:
            return a.value.__lt__(b)

    def __le__(a, b):
        if isinstance(b, String):
            return a.value.__le__(b.value)
        else:
            return a.value.__le__(b)

    def __eq__(a, b):
        if isinstance(b, String):
            return a.value.__eq__(b.value)
        else:
            return a.value.__eq__(b)

    def __ne__(a, b):
        if isinstance(b, String):
            return a.value.__ne__(b.value)
        else:
            return a.value.__ne__(b)

    def __gt__(a, b):
        if isinstance(b, String):
            return a.value.__gt__(b.value)
        else:
            return a.value.__gt__(b)

    def __ge__(a, b):
        if isinstance(b, String):
            return a.value.__ge__(b.value)
        else:
            return a.value.__ge__(b)

    # def __mod__(a, b):
    # if isinstance(b, String):
    # return a.value.__mod__(b.value)
    # else:
    # return a.value.__mod__(b)

    # def __rmod__(a, b):
    # if isinstance(b, String):
    # return a.value.__mod__(b.value)
    # else:
    # return a.value.__mod__(b)

    def __add__(a, b):
        if isinstance(b, String):
            return String(a.value.__add__(b.value))
        else:
            return String(a.value.__add__(b))

    def __mul__(a, b):
        if isinstance(b, Integer):
            return String(a.value.__mul__(b.value))
        else:
            return String(a.value.__mul__(b))

    def __rmul__(a, b):
        if isinstance(b, Integer):
            return String(a.value.__rmul__(b.value))
        else:
            return String(a.value.__rmul__(b))
