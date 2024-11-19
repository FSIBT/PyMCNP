"""
Contains abstract classes for ``inp``.
"""

import enum

from ..utils import _object


class CardEntry(_object.PyMcnpObject):
    """
    Represents INP card entries.

    ``CardEntry`` specifies common methods and attributes for PyMCNP card
    entry objects as an abstract class.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        raise NotImplementedError


class CardKeyword(_object.PyMcnpObject, enum.StrEnum):
    """
    Represents INP card option keywords.

    ``CardKeyword`` specifies common methods and attributes for PyMCNP card
    option keyword objects as an abstract class.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``CardKeyword``.

        ``from_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``CardKeyword``.
        """

        return self.value


class CardOption(_object.PyMcnpObject):
    """
    Represents INP card options.

    ``CardOption`` specifies common methods and attributes for PyMCNP card
    option objects as an abstract class.

    Attributes:
        keyword: Card option keyword.
        value: Card option value.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        """
        Generates INP from ``CardOption``.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``CardOption``.
        """

        if isinstance(self.value, tuple):
            if isinstance(self.value[0], str):
                return f'{self.keyword.to_mcnp()}={" ".join(entry for entry in self.value)}'
            else:
                return (
                    f'{self.keyword.to_mcnp()}={" ".join(entry.to_mcnp() for entry in self.value)}'
                )
        else:
            if isinstance(self.value, str):
                return f'{self.keyword.to_mcnp()}={self.value}'
            else:
                return f'{self.keyword.to_mcnp()}={self.value.to_mcnp()}'


class CardMnemonic(_object.PyMcnpObject, enum.StrEnum):
    """
    Represents INP card mnemonics.

    ``CardMnemonic`` specifies common methods and attributes for PyMCNP card
    mnemonic objects as an abstract class.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        """
        Generates INP from ``CardMnemonic``.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``CardMnemonic``.
        """

        return self.value


class Card(_object.PyMcnpObject):
    """
    Represents INP cards.

    ``Card`` specifies common methods and attributes for PyMCNP cards objects
    as an abstract class.

    Attributes:
        ident: Card identifier.
        line_number: Card line number.
        comment: Card inline comment.
    """

    @staticmethod
    def from_mcnp(source: str):
        raise NotImplementedError

    def to_mcnp(self) -> str:
        raise NotImplementedError
