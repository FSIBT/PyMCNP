import re
import typing

from . import outp
from . import _file
from . import types
from . import errors


class Outp(_file.File):
    """
    Represents OUTP files.

    Attributes:
        header: OUPT header.
        blocks: OUTP tables.
        footer: OUTP footer.
    """

    _REGEX = re.compile(rf'\A({outp.Header._REGEX.pattern[2:-2]})([\s\S]*)\Z', re.IGNORECASE)

    def __init__(
        self,
        header: outp.Header,
        blocks: types.Tuple(outp.Block),
    ):
        """
        Initializes `Outp`.

        Parameters:
            header: OUPT header.
            blocks: OUTP tables.
            footer: OUTP footer.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if header is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_FILE, header)

        if blocks is None or None in blocks:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_FILE, blocks)

        self.header: typing.Final[outp.Header] = header
        self.blocks: typing.Final[types.Tuple(outp.Block)] = blocks

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Outp` from OUTP.

        Parameters:
            source: OUTP for `Outp`.

        Returns:
            `Outp`.
        """

        tokens = re.split(r'(\n\d)', source)

        if len(tokens) > 2:
            header = outp.Header.from_mcnp(tokens[0] + '\n')
            tokens[1] = ''.join(filter(bool, tokens[1:]))
        else:
            header = outp.Header.from_mcnp(tokens[0])
            tokens.append('')

        blocks = []

        for subsource in re.split(r'\n1', tokens[1]):
            if not subsource:
                continue
            else:
                subsource = '1' + subsource

            for subclass in outp.Block.__subclasses__():
                try:
                    if block := subclass.from_mcnp(subsource):
                        break
                except Exception:
                    continue
            else:
                continue

            blocks.append(block)

        blocks = types.Tuple(outp.Block)(blocks)

        return Outp(
            header,
            blocks,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `Outp`.

        Returns:
            OUTP for `Outp`.
        """

        return self.header.to_mcnp() + '\n'.join(map(str, self.blocks))

    def to_dataframe(self):
        """
        Generates `pandas.DataFrame` from `Outp`.

        Returns:
            Tuple of `pandas.DataFrame`.
        """

        tallies = {}

        for block in self.blocks:
            if hasattr(block, 'to_dataframe'):
                tallies[block.number.value.strip()] = block.to_dataframe()

        return tallies
