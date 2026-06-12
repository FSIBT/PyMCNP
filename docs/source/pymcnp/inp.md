# `pymcnp.inp` Subpackage

```{eval-rst}
.. warning::
   The following surface visualizations are not currently supported:

   * `Rhp` (10 Parameters)
   * `Arb`
   * `Gq`
   * `Sq`
   * `X`
   * `Y`
   * `Z`
```

```{eval-rst}
.. warning::
   The following cards are not currently supported:

	* `card.data.Cmesh`
	* `card.data.Rmesh`
	* `card.data.Smesh`
	* `card.data.Cora`
	* `card.data.Corb`
	* `card.data.Corc`
	* `card.data.Ergsh`
	* `card.data.Fm`
	* `card.data.Mshmf`
	* `card.data.Rmesh`
	* `card.data.Sd`
	* `card.data.Smesh`
	* `card.data.Spabi`
	* `card.data.Spdtl`
	* `card.data.Ssw`
	* `card.data.Tmesh`

   The following options are not currently supported:

   * `option.data.burn.Omit`
   * `option.data.burn.Matmod`
   * `option.data.burn.Swapb`
   * `option.data.ptrac.Filter`
   * `option.data.ft.`

```

`pymcnp.inp` contains PyMCNP's input file parser.

## Table of Contents

```{eval-rst}
.. toctree::
	:maxdepth: 1

	inp/literal
	inp/group
	inp/option
	inp/card
```

## AST Classes

PyMCNP represents INP nonterminals with AST classes and stores them in nested subpackages.
These AST class have methods for translating between PyMCNP and INP:

* `from_mcnp`. Parses INP source, checking for syntax and semantic errors.
* `to_mcnp`. Generates INP source from PyMCNP objects, reformatting.

### `Card` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Card
   :members:
   :inherited-members:
```

[card subpackage](inp/card)

### `Group` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Group
   :members:
   :inherited-members:
```

[group subpackage](inp/group)

### `Literal` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Literal
   :members:
   :inherited-members:
```

[literal subpackage](inp/literal)

### `Option` Class

```{eval-rst}
.. autoclass:: pymcnp.inp.Option
   :members:
   :inherited-members:
```

[option subpackage](inp/option)
