import re
import abc
import enum
import pathlib

from .. import errors


class classproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        return self.func(owner)


class McnpTerminalMeta(enum.EnumMeta, abc.ABCMeta):
    pass


class McnpTerminal(enum.Enum, metaclass=McnpTerminalMeta):
    """
    Represents generic MCNP terminal symbols.
    """

    @classmethod
    @abc.abstractmethod
    def from_mcnp(cls, source: str):
        raise NotImplementedError

    @abc.abstractmethod
    def to_mcnp(self):
        raise NotImplementedError

    def __str__(self):
        return self.to_mcnp()

    def __eq__(a, b):
        return (a.__dict__ if a else None) == (b.__dict__ if b else None)


class McnpNonterminalMeta(abc.ABCMeta):
    pass


class McnpNonterminal(metaclass=McnpNonterminalMeta):
    """
    Represents generic MCNP nonterminal symbols.
    """

    @classproperty
    def _REGEX(cls):
        return re.compile(rf"\A{r'|'.join(map(lambda subclass: subclass._REGEX.pattern[2:-2], sorted(cls.__subclasses__(), reverse=True, key=lambda subclass: len(subclass.__name__),),))}\Z")

    @classmethod
    @abc.abstractmethod
    def from_mcnp(cls, source: str):
        raise NotImplementedError

    @abc.abstractmethod
    def to_mcnp(self):
        raise NotImplementedError

    def __str__(self):
        return self.to_mcnp()

    def __eq__(a, b):
        return (a.__dict__ if a else None) == (b.__dict__ if b else None)


class McnpFile(McnpNonterminal, metaclass=abc.ABCMeta):
    """
    Represents generic MCNP files.
    """

    @classmethod
    def from_file(cls, filename: pathlib.Path | str):
        """
        Generates ``McnpFile`` from MCNP files.

        Parameters:
            filename: MCNP file path.

        Raises:
            CliError: RUNTIME_PATH.
        """

        filename = pathlib.Path(filename)

        if not filename.is_file():
            raise errors.CliError(errors.CliCode.RUNTIME_PATH, filename)

        source = filename.read_text()

        return cls.from_mcnp(source)

    def to_file(self, filename: str | pathlib.Path):
        """
        Generates MCNP files from ``McnpFile``.

        Parameters:
            filename: new MCNP file path.
        """

        filename = pathlib.Path(filename)
        filename.write_text(self.to_mcnp())

    def __str__(self):
        return self.to_mcnp()

    def __eq__(a, b):
        return (a.__dict__ if a else None) == (b.__dict__ if b else None)
