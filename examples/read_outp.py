"""
Example reading OUTP files.
"""

import pathlib

import pymcnp

# Reading OUTP using ``from_file`.
path = pathlib.Path(__file__).parent.parent / 'files' / 'outp' / 'example_00.outp'
inp = pymcnp.Outp.from_file(path)

print(inp)

# Reading OUTP using ``from_mcnp``.
outp = pymcnp.Outp.from_mcnp("""          Code Name & Version = MCNP_6.20, 6.2.0
  
     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/ 
    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/        
   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/     
  _/      _/      _/             _/    _/_/       _/           _/    _/    
 _/      _/        _/_/_/       _/      _/       _/             _/_/       
  
  +-----------------------------------------------------------------------+
  | Copyright (2018).  Los Alamos National Security, LLC.  All rights     !
  | reserved.                                                             !
  |  This material was produced under U.S. Government contract            !
  | DE-AC52-06NA25396 for Los Alamos National Laboratory, which is        !
  | operated by Los Alamos National Security, LLC for the U.S.            !
  | Department of Energy. The Government is granted for itself and        !
  | others acting on its behalf a paid-up, nonexclusive, irrevocable      !
  | worldwide license in this material to reproduce, prepare derivative   !
  | works, and perform publicly and display publicly. Beginning five (5)  !
  | years after February 14, 2018, subject to additional five-year        !
  | worldwide renewals, the Government is granted for itself and others   !
  | acting on its behalf a paid-up, nonexclusive, irrevocable worldwide   !
  | license in this material to reproduce, prepare derivative works,      !
  | distribute copies to the public, perform publicly and display         !
  | publicly, and to permit others to do so. NEITHER THE UNITED STATES    !
  | NOR THE UNITED STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL   !
  | SECURITY, LLC, NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY,        !
  | EXPRESS OR IMPLIED, OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY  !
  | FOR THE ACCURACY, COMPLETENESS, OR USEFULNESS OF ANY INFORMATION,     !
  | APPARATUS, PRODUCT, OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE  !
  | WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS.                            !
  +-----------------------------------------------------------------------+
  
1mcnp     version 6     ld=02/20/18                     06/17/25 16:52:59 
 *************************************************************************                 probid =  06/17/25 16:52:59 
 i=valid_3_3g.i


 bad trouble in subroutine oldcd1 of imcn                             

 too many entries on fill card.
""")

print(outp)
