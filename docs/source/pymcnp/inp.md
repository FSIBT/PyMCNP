# `pymcnp.inp` Subpackage

```{eval-rst}
.. warning::
   The following non-terminals are not currently supported:

   * `Field` (3.3.3.12)
   * `Mplot` (3.3.7.2.5)
   * `Burn` (3.3.4.13)
   * `Embed.Overlap` (3.3.1.6.2)
   * `Tmesh` (3.3.5.24)
   * `Spabi` (3.3.6.16)

   The following non-terminals are partial supported:

   * `Fm` (3.3.5.7)
   * `Ft` (3.3.5.18)
```

`pymcnp.inp` contains the INP parser. PyMCNP implements an object-oriented recursive
descent parser, approximating INP as the following context-free-grammar described in modified Backus-Naur form:

```
<CellOption> = ...;
<Cell> = <Integer> " " <Integer> ( " " <Real> )? " " <Geometry> ( " " <CellOption>)*;

<SurfaceOption> = ...;
<Surface> = ( "+" | "*" ) <Integer> ( " " <Integer> )? <SurfaceOption>;

<DataOption> = ...;
<Data> = <DataOption>;
```

## Table of Contents

```{eval-rst}
.. toctree::
   :maxdepth: 1

   inp/cell
   inp/like
   inp/surface
   inp/act
   inp/bfld
   inp/dawwg
   inp/dd
   inp/df_1
   inp/ds_1
   inp/ds_2
   inp/dxt
   inp/embed
   inp/embee
   inp/f_1
   inp/f_2
   inp/files
   inp/fmesh
   inp/fmult
   inp/kopts
   inp/kpert
   inp/ksen
   inp/ksrc
   inp/m_0
   inp/mesh
   inp/mplot
   inp/pert
   inp/pikmt
   inp/ptrac
   inp/rand
   inp/sdef
   inp/ssr
   inp/ssw
   inp/stop
   inp/t_1
   inp/tropt
   inp/uran
   inp/var
```

## AST Classes

PyMCNP represents INP non-terminals with AST classes and stores them in nested subpackages.
These AST class have methods for translating between PyMCNP and INP:

* `from_mcnp`. Parses INP source, checking for syntax and semantic errors.
* `to_mcnp`. Generates INP source from PyMCNP objects, reformatting.

### `Comment` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Comment
   :members:
   :inherited-members:
```

### `Cell` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Cell
   :members:
   :inherited-members:
```

[cell subpackage](inp/cell)

### `Like` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Like
   :members:
   :inherited-members:
```

[like subpackage](inp/like)

### `Surface` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Surface
   :members:
   :inherited-members:
```

[surface subpackage](inp/surface)

### `Act` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Act
   :members:
   :inherited-members:
```

[act subpackage](inp/act)

### `Area` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Area
   :members:
   :inherited-members:
```

### `Awtab` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Awtab
   :members:
   :inherited-members:
```

### `Bbrem` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Bbrem
   :members:
   :inherited-members:
```

### `Bflcl` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Bflcl
   :members:
   :inherited-members:
```

### `Bfld` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Bfld
   :members:
   :inherited-members:
```

[bfld subpackage](inp/bfld)

### `C` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.C
   :members:
   :inherited-members:
```


### `Cf` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Cf
   :members:
   :inherited-members:
```

### `Cm` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Cm
   :members:
   :inherited-members:
```

### `Cosy` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Cosy
   :members:
   :inherited-members:
```

### `Cosyp` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Cosyp
   :members:
   :inherited-members:
```

### `Ctme` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ctme
   :members:
   :inherited-members:
```

### `Cut` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Cut
   :members:
   :inherited-members:
```

### `Dawwg` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Dawwg
   :members:
   :inherited-members:
```

[dawwg subpackage](inp/dawwg)

### `Dbcn` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Dbcn
   :members:
   :inherited-members:
```

### `Dd` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Dd
   :members:
   :inherited-members:
```

[dd subpackage](inp/dd)

### `De` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.De
   :members:
   :inherited-members:
```

### `Df_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Df_0
   :members:
   :inherited-members:
```

### `Df_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Df_1
   :members:
   :inherited-members:
```

[df_1 subpackage](inp/df_1)

### `Dm` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Dm
   :members:
   :inherited-members:
```

### `Drxs` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Drxs
   :members:
   :inherited-members:
```

### `Ds_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ds_0
   :members:
   :inherited-members:
```

### `Ds_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ds_1
   :members:
   :inherited-members:
```

[ds_1 subpackage](inp/ds_1)

### `Ds_2` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ds_2
   :members:
   :inherited-members:
```

[ds_2 subpackage](inp/ds_2)

### `Ds_3` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ds_3
   :members:
   :inherited-members:
```

### `Dxc` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Dxc
   :members:
   :inherited-members:
```

### `Dxt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Dxt
   :members:
   :inherited-members:
```

[dxt subpackage](inp/dxt)

### `E` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.E
   :members:
   :inherited-members:
```

### `Elpt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Elpt
   :members:
   :inherited-members:
```

### `Em` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Em
   :members:
   :inherited-members:
```

### `Embdb` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Embdb
   :members:
   :inherited-members:
```

### `Embdf` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Embdf
   :members:
   :inherited-members:
```

### `Embeb` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Embeb
   :members:
   :inherited-members:
```

### `Embed` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Embed
   :members:
   :inherited-members:
```

[embed subpackage](inp/embed)

### `Embee` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Embee
   :members:
   :inherited-members:
```

[embee subpackage](inp/embee)

### `Embem` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Embem
   :members:
   :inherited-members:
```

### `Embtb` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Embtb
   :members:
   :inherited-members:
```

### `Embtm` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Embtm
   :members:
   :inherited-members:
```

### `Esplt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Esplt
   :members:
   :inherited-members:
```

### `Ext` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ext
   :members:
   :inherited-members:
```

### `F_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.F_0
   :members:
   :inherited-members:
```

### `F_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.F_1
   :members:
   :inherited-members:
```

[f_1 subpackage](inp/f_1)

### `F_2` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.F_2
   :members:
   :inherited-members:
```

[f_2 subpackage](inp/f_2)

### `F_3` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.F_3
   :members:
   :inherited-members:
```

### `F_4` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.F_4
   :members:
   :inherited-members:
```

### `Fc` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fc
   :members:
   :inherited-members:
```

### `Fcl` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fcl
   :members:
   :inherited-members:
```

### `Fic` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fic
   :members:
   :inherited-members:
```

### `Files` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Files
   :members:
   :inherited-members:
```

[files subpackage](inp/files)

### `Fill` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fill
   :members:
   :inherited-members:
```

### `Fip` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fip
   :members:
   :inherited-members:
```

### `Fir` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fir
   :members:
   :inherited-members:
```

### `Fm` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fm
   :members:
   :inherited-members:
```

### `Fmesh` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fmesh
   :members:
   :inherited-members:
```

[fmesh subpackage](inp/fmesh)

### `Fmult` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fmult
   :members:
   :inherited-members:
```

[fmult subpackage](inp/fmult)

### `Fq` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fq
   :members:
   :inherited-members:
```

### `Fs` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fs
   :members:
   :inherited-members:
```

### `Ft` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ft
   :members:
   :inherited-members:
```

### `Fu` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Fu
   :members:
   :inherited-members:
```

### `Histp` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Histp
   :members:
   :inherited-members:
```

### `Hsrc` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Hsrc
   :members:
   :inherited-members:
```

### `Idum` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Idum
   :members:
   :inherited-members:
```

### `Imp` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Imp
   :members:
   :inherited-members:
```

### `Kcode` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Kcode
   :members:
   :inherited-members:
```

### `Kopts` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Kopts
   :members:
   :inherited-members:
```

[kopts subpackage](inp/kopts)

### `Kpert` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Kpert
   :members:
   :inherited-members:
```

[kpert subpackage](inp/kpert)

### `Ksen` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ksen
   :members:
   :inherited-members:
```

[ksen subpackage](inp/ksen)

### `Ksrc` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ksrc
   :members:
   :inherited-members:
```

[ksrc subpackage](inp/ksrc)

### `Lat` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Lat
   :members:
   :inherited-members:
```

### `Lca` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Lca
   :members:
   :inherited-members:
```

### `Lcb` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Lcb
   :members:
   :inherited-members:
```

### `Lcc` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Lcc
   :members:
   :inherited-members:
```

### `Lea` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Lea
   :members:
   :inherited-members:
```

### `Leb` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Leb
   :members:
   :inherited-members:
```

### `Lost` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Lost
   :members:
   :inherited-members:
```

### `M_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.M_0
   :members:
   :inherited-members:
```

[m_0 subpackage](inp/m_0)

### `M_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.M_1
   :members:
   :inherited-members:
```

### `Mesh` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Mesh
   :members:
   :inherited-members:
```

[mesh subpackage](inp/mesh)

### `Mgopt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Mgopt
   :members:
   :inherited-members:
```

### `Mode` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Mode
   :members:
   :inherited-members:
```

### `Mphys` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Mphys
   :members:
   :inherited-members:
```

### `Mplot` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Mplot
   :members:
   :inherited-members:
```

[mplot subpackage](inp/mplot)

### `Mt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Mt
   :members:
   :inherited-members:
```

### `Mx` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Mx
   :members:
   :inherited-members:
```

### `Nonu` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Nonu
   :members:
   :inherited-members:
```

### `Notrn` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Notrn
   :members:
   :inherited-members:
```

### `Nps` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Nps
   :members:
   :inherited-members:
```

### `Otfdb` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Otfdb
   :members:
   :inherited-members:
```

### `Pd` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Pd
   :members:
   :inherited-members:
```

### `Pert` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Pert
   :members:
   :inherited-members:
```

[pert subpackage](inp/pert)

### `Phys_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Phys_0
   :members:
   :inherited-members:
```

### `Phys_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Phys_1
   :members:
   :inherited-members:
```

### `Phys_2` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Phys_2
   :members:
   :inherited-members:
```

### `Phys_3` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Phys_3
   :members:
   :inherited-members:
```

### `Phys_4` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Phys_4
   :members:
   :inherited-members:
```

### `Pikmt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Pikmt
   :members:
   :inherited-members:
```

[pikmt subpackage](inp/pikmt)

### `Prdmp` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Prdmp
   :members:
   :inherited-members:
```

### `Print` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Print
   :members:
   :inherited-members:
```

### `Ptrac` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ptrac
   :members:
   :inherited-members:
```

[ptrac subpackage](inp/ptrac)

### `Pwt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Pwt
   :members:
   :inherited-members:
```

### `Rand` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Rand
   :members:
   :inherited-members:
```

[rand subpackage](inp/rand)

### `Rdum` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Rdum
   :members:
   :inherited-members:
```

### `Sb_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Sb_0
   :members:
   :inherited-members:
```

### `Sb_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Sb_1
   :members:
   :inherited-members:
```

### `Sc` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Sc
   :members:
   :inherited-members:
```

### `Sd` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Sd
   :members:
   :inherited-members:
```

### `Sdef` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Sdef
   :members:
   :inherited-members:
```

[sdef subpackage](inp/sdef)

### `Sf` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Sf
   :members:
   :inherited-members:
```

### `Si_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Si_0
   :members:
   :inherited-members:
```

### `Si_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Si_1
   :members:
   :inherited-members:
```

### `Sp_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Sp_0
   :members:
   :inherited-members:
```

### `Sp_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Sp_1
   :members:
   :inherited-members:
```

### `Spdtl` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Spdtl
   :members:
   :inherited-members:
```

### `Ssr` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ssr
   :members:
   :inherited-members:
```

[ssr subpackage](inp/ssr)

### `Ssw` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Ssw
   :members:
   :inherited-members:
```

[ssw subpackage](inp/ssw)

### `Stop` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Stop
   :members:
   :inherited-members:
```

[stop subpackage](inp/stop)

### `T_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.T_0
   :members:
   :inherited-members:
```

### `T_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.T_1
   :members:
   :inherited-members:
```

[t_1 subpackage](inp/t_1)

### `Talnp` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Talnp
   :members:
   :inherited-members:
```

### `Thtme` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Thtme
   :members:
   :inherited-members:
```

### `Tf_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Tf_0
   :members:
   :inherited-members:
```

### `Tf_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Tf_1
   :members:
   :inherited-members:
```

### `Tm` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Tm
   :members:
   :inherited-members:
```

### `Totnu` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Totnu
   :members:
   :inherited-members:
```

### `Tr_0` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Tr_0
   :members:
   :inherited-members:
```

### `Tr_1` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Tr_1
   :members:
   :inherited-members:
```

### `Tr_2` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Tr_2
   :members:
   :inherited-members:
```

### `Tr_3` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Tr_3
   :members:
   :inherited-members:
```

### `Tr_4` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Tr_4
   :members:
   :inherited-members:
```

### `Tropt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Tropt
   :members:
   :inherited-members:
```

[tropt subpackage](inp/tropt)

### `Tsplt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Tsplt
   :members:
   :inherited-members:
```

### `U` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.U
   :members:
   :inherited-members:
```

### `Unc` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Unc
   :members:
   :inherited-members:
```

### `Uran` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Uran
   :members:
   :inherited-members:
```

[uran subpackage](inp/uran)

### `Var` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Var
   :members:
   :inherited-members:
```

[var subpackage](inp/var)

### `Void` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Void
   :members:
   :inherited-members:
```

### `Vol` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Vol
   :members:
   :inherited-members:
```

### `Wwe` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Wwe
   :members:
   :inherited-members:
```

### `Wwg` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Wwg
   :members:
   :inherited-members:
```

### `Wwge` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Wwge
   :members:
   :inherited-members:
```

### `Wwgt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Wwgt
   :members:
   :inherited-members:
```

### `Wwn` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Wwn
   :members:
   :inherited-members:
```

### `Wwp` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Wwp
   :members:
   :inherited-members:
```

### `Wwt` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Wwt
   :members:
   :inherited-members:
```

### `Xs` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Xs
   :members:
   :inherited-members:
```

### `Za` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Za
   :members:
   :inherited-members:
```

### `Zb` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Zb
   :members:
   :inherited-members:
```

### `Zc` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Zc
   :members:
   :inherited-members:
```

### `Zd` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Zd
   :members:
   :inherited-members:
```
