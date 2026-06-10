import re


from .. import abc


# _REGEX_REPEAT = re.compile(r'(\S+) (\d+)R', re.IGNORECASE)
# _REGEX_INSERT = re.compile(r'(\S+) (\d+)I (\S+)', re.IGNORECASE)
# _REGEX_JUMP = re.compile(r'(?<=\s)(\d+)(J)(?=\s)', re.IGNORECASE)
# _REGEX_LOG = re.compile(r'(\S+) (\d+)I?LOG (\S+)', re.IGNORECASE)


class Space(abc.Terminal):
    """
    Represents spaces for parameters.
    """

    _pattern = re.compile(r'( *(?:\$.+)?\n {1,5} *| +&\n +|\n {1,5} *| +)([\s\S]*)', re.IGNORECASE)
    _default = ' '


class Option(abc.Nonterminal):
    """
    Represents options.
    """

    _space = (Space,)


'''
    @classmethod
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into options.

        Parameters:
            source: Source string to compile.

        Returns:
            Nonterminal symbol corresponding to `source`.

        Raises:
            Error: Expected symbol.
            Error: Expected space.
        """

        assert isinstance(source, str)

        # Preprocessing horizontal data format.
        source = _REGEX_REPEAT.sub(lambda match: f"{match[1]} {' '.join([match[1]] * int(match[2]))}", source)
        source = _REGEX_INSERT.sub(lambda match: ' '.join(map(str, numpy.linspace(float(match[1]), float(match[3]), num=int(match[2])))), source)
        source = _REGEX_JUMP.sub(lambda match: ' '.join([match[2]] * int(match[1])), source)
        source = _REGEX_LOG.sub(lambda match: ' '.join(map(str, numpy.logspace(float(match[1]), float(match[3]), num=int(match[2])))), source)

        return super().from_mcnp(source)
'''
