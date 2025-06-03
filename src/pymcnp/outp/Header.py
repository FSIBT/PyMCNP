import re
import typing

from . import _block
from ..utils import types
from ..utils import errors


class Header(_block.Block):
    """
    Represents OUTP header tables.

    Attributes:
        name: name name & version
    """

    _REGEX = re.compile(
        r'\A          Code Name & Version = (.+)\n'
        r'  \n'
        r'     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/\n'
        r'    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/       \n'
        r'   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/    \n'
        r'  _/      _/      _/             _/    _/_/       _/           _/    _/   \n'
        r' _/      _/        _/_/_/       _/      _/       _/             _/_/      \n'
        r'  \n'
        r'  [+]---------------------------------------------------------------------[+]\n'
        r'  [|] Copyright 2008[.] Los Alamos National Security, LLC[.]  All rights      [|]\n'
        r'  [|] reserved[.]                                                           [|]\n'
        r'  [|]   This material was produced under U[.]S[.] Government contract         [|]\n'
        r'  [|] DE-AC52-06NA25396 for Los Alamos National Laboratory, which is      [|]\n'
        r'  [|] operated by Los Alamos National Security, LLC, for the U[.]S[.]         [|]\n'
        r'  [|] Department of Energy[.] The Government is granted for itself and      [|]\n'
        r'  [|] others acting on its behalf a paid-up, nonexclusive, irrevocable    [|]\n'
        r'  [|] worldwide license in this material to reproduce, prepare derivative [|]\n'
        r'  [|] works, and perform publicly and display publicly[.] Beginning five    [|]\n'
        r'  [|] [(]5[)] years after 2008, subject to additional five-year worldwide     [|]\n'
        r'  [|] renewals, the Government is granted for itself and others acting on [|]\n'
        r'  [|] its behalf a paid-up, nonexclusive, irrevocable worldwide license   [|]\n'
        r'  [|] in this material to reproduce, prepare derivative works, distribute [|]\n'
        r'  [|] copies to the public, perform publicly and display publicly, and to [|]\n'
        r'  [|] permit others to do so[.] NEITHER THE UNITED STATES NOR THE UNITED    [|]\n'
        r'  [|] STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL SECURITY, LLC, [|]\n'
        r'  [|] NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY, EXPRESS OR IMPLIED, [|]\n'
        r'  [|] OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY,  [|]\n'
        r'  [|] COMPLETENESS, OR USEFULNESS OF ANY INFORMATION, APPARATUS, PRODUCT, [|]\n'
        r'  [|] OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE WOULD NOT INFRINGE [|]\n'
        r'  [|] PRIVATELY OWNED RIGHTS[.]                                             [|]\n'
        r'  [+]---------------------------------------------------------------------[+]\n'
        r'  \n\Z'
    )

    def __init__(self, name: types.String):
        """
        Initializes ``Header``.

        Parameters:
            name: Simulation name.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if name is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, name)

        self.name: typing.Final[types.String] = name

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Header`` from OUTP.

        Parameters:
            source: OUTP for ``Header``.

        Returns:
            ``Header``.

        Raises:
            OutpError: SYNTAX_TABLE.
        """

        tokens = Header._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        name = types.String.from_mcnp(tokens[1])

        return Header(
            name,
        )

    def to_mcnp(self):
        """
        Generates OUTP from ``Header``.

        Returns:
            OUTP for ``Header``.
        """

        return f"""
          Code Name & Version = {self.version}
  
     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/
    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/       
   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/    
  _/      _/      _/             _/    _/_/       _/           _/    _/   
 _/      _/        _/_/_/       _/      _/       _/             _/_/      
  
  +---------------------------------------------------------------------+
  | Copyright 2008. Los Alamos National Security, LLC.  All rights      |
  | reserved.                                                           |
  |   This material was produced under U.S. Government contract         |
  | DE-AC52-06NA25396 for Los Alamos National Laboratory, which is      |
  | operated by Los Alamos National Security, LLC, for the U.S.         |
  | Department of Energy. The Government is granted for itself and      |
  | others acting on its behalf a paid-up, nonexclusive, irrevocable    |
  | worldwide license in this material to reproduce, prepare derivative |
  | works, and perform publicly and display publicly. Beginning five    |
  | (5) years after 2008, subject to additional five-year worldwide     |
  | renewals, the Government is granted for itself and others acting on |
  | its behalf a paid-up, nonexclusive, irrevocable worldwide license   |
  | in this material to reproduce, prepare derivative works, distribute |
  | copies to the public, perform publicly and display publicly, and to |
  | permit others to do so. NEITHER THE UNITED STATES NOR THE UNITED    |
  | STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL SECURITY, LLC, |
  | NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY, EXPRESS OR IMPLIED, |
  | OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY,  |
  | COMPLETENESS, OR USEFULNESS OF ANY INFORMATION, APPARATUS, PRODUCT, |
  | OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE WOULD NOT INFRINGE |
  | PRIVATELY OWNED RIGHTS.                                             |
  +---------------------------------------------------------------------+
  
"""[-1:1]
