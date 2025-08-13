import re
import typing

from . import _block
from .. import types
from .. import errors


class Header(_block.Block):
    """
    Represents OUTP header tables.

    Attributes:
        name: name name & version
    """

    _REGEX = re.compile(
        r'\A\s+Code Name & Version = (.+)\n'
        r'  \n'
        r'(\s+_/\s+_/\s+_/_/_/\s+_/\s+_/\s+_/_/_/\s+_/_/_/ ?\n\s+_/_/  _/_/\s+_/\s+_/_/\s+_/\s+_/\s+_/\s+_/\s+?\n\s+_/  _/  _/\s+_/\s+_/  _/  _/\s+_/_/_/\s+_/_/_/\s+?\n  _/\s+_/\s+_/\s+_/\s+_/_/\s+_/\s+_/\s+_/\s+?\n _/\s+_/\s+_/_/_/\s+_/\s+_/\s+_/\s+_/_/\s+?\n)'
        r'  \n'
        r'((?:  [+]---------------------------------------------------------------------(?:--)?[+]\n)(?:.+\n)+(?:  [+]---------------------------------------------------------------------(?:--)?[+]\n))'
        r'  \n\Z'
    )

    def __init__(self, name: types.String, logo: types.String, box: types.String):
        """
        Initializes `Header`.

        Parameters:
            name: Simulation name.
            logo: MCNP logo.
            box: Simulation disclaimer.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if name is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, name)

        if logo is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, logo)

        if box is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, box)

        self.name: typing.Final[types.String] = name
        self.logo: typing.Final[types.String] = logo
        self.box: typing.Final[types.String] = box

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Header` from OUTP.

        Parameters:
            source: OUTP for `Header`.

        Returns:
            `Header`.

        Raises:
            OutpError: SYNTAX_TABLE.
        """

        tokens = Header._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        name = types.String.from_mcnp(tokens[1])
        logo = types.String.from_mcnp(tokens[2])
        box = types.String.from_mcnp(tokens[3])

        return Header(
            name,
            logo,
            box,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `Header`.

        Returns:
            OUTP for `Header`.
        """

        return f"""
          Code Name & Version = {self.name}
  
{self.logo}  
{self.box}  

"""[1:-1]
