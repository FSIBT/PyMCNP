import typing

from .. import abc


class Header(abc.Nonterminal):
    """
    Represents headers.

    Attributes:
        version_preable: header version preambles.
        version: header code name and version.
        logo: header logo.
        copyright: header copyright.
    """

    version_preable: typing.Annotated[abc.Terminal, r'          Code Name & Version = ']
    version: typing.Annotated[abc.Terminal, r'.+']
    logo: (
        typing.Annotated[
            abc.Terminal,
            r'\n  \n         _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/ \n    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/        \n   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/     \n  _/      _/      _/             _/    _/_/       _/           _/    _/    \n _/      _/        _/_/_/       _/      _/       _/             _/_/       ',
        ]
        | typing.Annotated[
            abc.Terminal,
            r'\n  \n     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/\n    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/       \n   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/    \n  _/      _/      _/             _/    _/_/       _/           _/    _/   \n _/      _/        _/_/_/       _/      _/       _/             _/_/      ',
        ]
        | typing.Annotated[
            abc.Terminal,
            r'\n  \n     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/ \n    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/        \n   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/     \n  _/      _/      _/             _/    _/_/       _/           _/    _/    \n _/      _/        _/_/_/       _/      _/       _/             _/_/       ',
        ]
    )
    copyright: (
        typing.Annotated[
            abc.Terminal,
            r'\n  \n  \+---------------------------------------------------------------------\+\n  \| Copyright 2008\. Los Alamos National Security, LLC\.  All rights      \|\n  \| reserved\.                                                           \|\n  \|   This material was produced under U\.S\. Government contract         \|\n  \| DE-AC52-06NA25396 for Los Alamos National Laboratory, which is      \|\n  \| operated by Los Alamos National Security, LLC, for the U\.S\.         \|\n  \| Department of Energy\. The Government is granted for itself and      \|\n  \| others acting on its behalf a paid-up, nonexclusive, irrevocable    \|\n  \| worldwide license in this material to reproduce, prepare derivative \|\n  \| works, and perform publicly and display publicly\. Beginning five    \|\n  \| \(5\) years after 2008, subject to additional five-year worldwide     \|\n  \| renewals, the Government is granted for itself and others acting on \|\n  \| its behalf a paid-up, nonexclusive, irrevocable worldwide license   \|\n  \| in this material to reproduce, prepare derivative works, distribute \|\n  \| copies to the public, perform publicly and display publicly, and to \|\n  \| permit others to do so\. NEITHER THE UNITED STATES NOR THE UNITED    \|\n  \| STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL SECURITY, LLC, \|\n  \| NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY, EXPRESS OR IMPLIED, \|\n  \| OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY,  \|\n  \| COMPLETENESS, OR USEFULNESS OF ANY INFORMATION, APPARATUS, PRODUCT, \|\n  \| OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE WOULD NOT INFRINGE \|\n  \| PRIVATELY OWNED RIGHTS\.                                             \|\n  \+---------------------------------------------------------------------\+\n  \n',
        ]
        | typing.Annotated[
            abc.Terminal,
            r'\n  \n  \+-----------------------------------------------------------------------\+\n  \| Copyright \(2018\)\.  Los Alamos National Security, LLC\.  All rights     !\n  \| reserved\.                                                             !\n  \|  This material was produced under U\.S\. Government contract            !\n  \| DE-AC52-06NA25396 for Los Alamos National Laboratory, which is        !\n  \| operated by Los Alamos National Security, LLC for the U.S\.            !\n  \| Department of Energy\. The Government is granted for itself and        !\n  \| others acting on its behalf a paid-up, nonexclusive, irrevocable      !\n  \| worldwide license in this material to reproduce, prepare derivative   !\n  \| works, and perform publicly and display publicly\. Beginning five \(5\)  !\n  \| years after February 14, 2018, subject to additional five-year        !\n  \| worldwide renewals, the Government is granted for itself and others   !\n  \| acting on its behalf a paid-up, nonexclusive, irrevocable worldwide   !\n  \| license in this material to reproduce, prepare derivative works,      !\n  \| distribute copies to the public, perform publicly and display         !\n  \| publicly, and to permit others to do so\. NEITHER THE UNITED STATES    !\n  \| NOR THE UNITED STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL   !\n  \| SECURITY, LLC, NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY,        !\n  \| EXPRESS OR IMPLIED, OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY  !\n  \| FOR THE ACCURACY, COMPLETENESS, OR USEFULNESS OF ANY INFORMATION,     !\n  \| APPARATUS, PRODUCT, OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE  !\n  \| WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS\.                            !\n  \+-----------------------------------------------------------------------\+\n  \n',
        ]
    )
