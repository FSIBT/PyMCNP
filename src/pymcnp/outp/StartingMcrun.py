import re
import typing

from . import _block
from .. import types
from .. import errors


class StartingMcrun(_block.Block):
    """
    Represents OUTP `1starting mcrun` blocks.

    Attributes:
        cp0: Geometry error.
        title: Problem title.
        data: First 50 source particles.
    """

    _REGEX = re.compile(
        r'\A1starting mcrun.      cp0 = (.{5})                                                                       print table 110\n\n'
        r'      (.{80})\n\n\n'
        r'     nps    x          y          z          cell       surf     u          v          w        energy     weight      time\n \n'
        r'((?:.+\n)+)\Z'
    )

    def __init__(
        self,
        cp0: types.String,
        title: types.String,
        data: types.String,
    ):
        """
        Initializes `StartingMcrun`.

        Parameters:
            cp0: Geometry error.
            title: Problem title.
            data: First 50 source particles.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if cp0 is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, cp0)
        if title is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, title)
        if data is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, data)

        self.cp0: typing.Final[types.String] = cp0
        self.title: typing.Final[types.String] = title
        self.data: typing.Final[types.String] = data

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `StartingMcrun` from OUTP.

        Parameters:
            source: OUTP for `StartingMcrun`.

        Returns:
            `StartingMcrun`.
        """

        tokens = StartingMcrun._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        cp0 = types.String.from_mcnp(tokens[1])
        title = types.String.from_mcnp(tokens[2])
        data = types.String.from_mcnp(tokens[3])

        return StartingMcrun(
            cp0,
            title,
            data,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `StartingMcrun`.

        Returns:
            OUTP for `StartingMcrun`.
        """

        return f"""
1starting mcrun.      cp0 = {self.cp0:5}                                                                       print table 110

      {self.title:80}


     nps    x          y          z          cell       surf     u          v          w        energy     weight      time
 
{self.data}
"""[1:-1]
