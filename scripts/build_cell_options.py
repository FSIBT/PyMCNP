"""
Contains script for building ``CellOption`` subclasses.
"""

import pathlib

import _data


def build_CellOption(cell_option: _data.CellOptionScheme):
    o = ''

    # CELL.OPTION

    o += 'import re\n'
    o += 'from typing import Final\n'
    o += '\n'
    o += 'from ..cell_option import CellOption\n'
    o += 'from ..cell_keyword import CellKeyword\n'
    o += 'from ...utils import types, errors, _parser\n'
    o += '\n'
    o += f'class {cell_option.name}(CellOption):\n'
    o += '    """\n'
    o += f'    Represents INP cell card {cell_option.mnemonic} options.\n'
    o += '\n'
    o += f'    ``{cell_option.name}`` implements ``_card.CardOption``.\n'
    o += '\n'
    o += '    Attributes:\n'

    for attribute in cell_option.attributes:
        o += f'        {attribute.name}: {attribute.description}\n'

    o += '    """\n'
    o += '\n'

    # CELL.OPTION.__INIT__

    o += f'    def __init__(self, {", ".join(f'{attribute.name}: {attribute.type}' for attribute in cell_option.attributes)}):\n'
    o += '        """\n'
    o += f'        Initializes ``{cell_option.name}``.\n'
    o += '\n'
    o += '        Parameters:\n'

    for attribute in cell_option.attributes:
        o += f'            {attribute.name}: {attribute.description}\n'

    o += '\n'
    o += '        Raises:\n'

    for attribute in cell_option.attributes:
        o += f'            McnpError: {attribute.error}.\n'

    o += '        """\n'
    o += '\n'

    for attribute in cell_option.attributes:
        if attribute.type.startswith('tuple'):
            o += f'        if {attribute.name} is None:\n'
            o += f'            raise errors.McnpError(errors.McnpCode.{attribute.error}, str({attribute.name}))\n'
            o += '\n'
            o += f'        for entry in {attribute.name}:\n'

            if attribute.restriction:
                o += f'            if entry is None or not ({attribute.restriction}):\n'
            else:
                o += '            if entry is None:\n'
        else:
            if attribute.restriction:
                o += f'        if {attribute.name} is None or not ({attribute.restriction}):\n'
            else:
                o += f'        if {attribute.name} is None:\n'

        o += f'                raise errors.McnpError(errors.McnpCode.{attribute.error}, str({attribute.name}))\n'

    o += '\n'

    o += f'        self.keyword: Final[CellKeyword] = CellKeyword.{cell_option.enum}\n'
    o += f'        self.value: Final[{cell_option.attributes[0].type}] = {cell_option.attributes[0].name}\n'

    for attribute in cell_option.attributes:
        o += f'        self.{attribute.name}: Final[{attribute.type}] = {attribute.name}\n'

    o += '\n'

    # CELL.OPTION.from_mcnp

    o += '    @staticmethod\n'
    o += '    def from_mcnp(source: str):\n'
    o += '        """\n'
    o += f'        Generates ``{cell_option.name}`` objects from INP.\n'
    o += '\n'
    o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
    o += '\n'
    o += '        Parameters:\n'
    o += f'            source: INP for ``{cell_option.name}``.\n'
    o += '\n'
    o += '        Returns:\n'
    o += f'            ``{cell_option.name}`` object.\n'
    o += '\n'
    o += '        Raises:\n'
    o += '            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.\n'
    o += '        """\n'
    o += '\n'
    o += '        source = _parser.Preprocessor.process_inp(source)\n'
    o += '        tokens = _parser.Parser(\n'
    o += '            re.split(r"=| |:", source),\n'
    o += '            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),\n'
    o += '        )\n'
    o += '\n'
    o += '        keyword = re.search(r"^[a-zA-Z*]+", tokens.peekl())\n'
    o += '        keyword = keyword[0] if keyword else ""\n'
    o += f'        if keyword != "{cell_option.mnemonic}":\n'
    o += '            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))\n'
    o += '\n'

    if 'suffix' in [attribute.name for attribute in cell_option.attributes]:
        o += f'        suffix = types.McnpInteger.from_mcnp(tokens.popl()[{len(cell_option.mnemonic)}:])\n'
    else:
        o += '        tokens.popl()\n'

    if 'designator' in [attribute.name for attribute in cell_option.attributes]:
        o += '        designator = types.Designator.from_mcnp(tokens.popl())\n'

    if cell_option.attributes[0].type.startswith('tuple'):
        # value: tuple[...]
        inner_type = cell_option.attributes[0].type[len('tuple[') : -1]

        if inner_type == 'str':
            # value: tuple[str]
            o += f'        {cell_option.attributes[0].name} = tuple([tokens.popl() for _ in range(0, len(tokens))])\n'
        else:
            # value: tuple[?]
            o += f'        {cell_option.attributes[0].name} = tuple([{inner_type}.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])\n'

    elif attribute.type == 'str':
        # value: str
        o += f'        {cell_option.attributes[0].name} = tokens.popl()\n'

    else:
        # value: ?
        o += f'        {cell_option.attributes[0].name} = {cell_option.attributes[0].type}.from_mcnp(tokens.popl())\n'

    o += '\n'

    o += f'        return {cell_option.name}({", ".join(f'{attribute.name}' for attribute in cell_option.attributes)})\n'
    o += '\n'

    return o


init_imports = []
init_all = []

for cell_option in _data.CELL_OPTIONS:
    filename = pathlib.Path(__file__).parent / pathlib.Path(
        f'../src/pymcnp/files/inp/cell_options/{cell_option.mnemonic}.py'
    )
    with filename.open('w') as file:
        file.write(
            f'"""\n Contains the ``{cell_option.name}`` subclass of ``CellOption``.\n"""\n\n'
            + build_CellOption(cell_option)
        )
        init_imports.append(f'from .{cell_option.name.lower()} import {cell_option.name}')
        init_all.append(f'"{cell_option.name}",')

init_path = pathlib.Path(__file__).parent / pathlib.Path(
    '../src/pymcnp/files/inp/cell_options/__init__.py'
)
with init_path.open('w') as file:
    file.write(
        '\n'.join(init_imports) + '\n\n__all__ = [\n    ' + '\n    '.join(init_all) + '\n]\n'
    )
