"""
Contains script for building ``Surface`` subclasses.
"""

import pathlib

import _data


def build_Surface(surface: _data.SurfaceScheme):
    o = ''

    # SURFACE

    o += 'from typing import Final\n'
    o += '\n'
    o += 'from ..surface import Surface\n'
    o += 'from ..surface_mnemonic import SurfaceMnemonic\n'
    o += 'from ...utils import types, errors, _parser\n'
    o += '\n'
    o += f'class {surface.name}(Surface):\n'
    o += '    """\n'
    o += f'    Represents INP {surface.mnemonic} surface cards.\n'
    o += '\n'
    o += f'    ``{surface.name}`` implements ``Surface``.\n'
    o += '\n'
    o += '    Attributes:\n'

    for attribute in surface.attributes:
        o += f'        {attribute.name}: {attribute.description}.\n'

    o += '    """\n'
    o += '\n'

    # SURFACE.__init__

    t = []
    for attribute in surface.attributes:
        t.append(f'{attribute.name}: {attribute.type}')

    o += f'    def __init__(self, number: types.McnpInteger, transform: types.McnpInteger, {", ".join(t)}, is_whiteboundary: bool = False, is_reflecting: bool = False):\n'
    o += '        """\n'
    o += f'        Initializes ``{surface.name}``.\n'
    o += '\n'
    o += '\n'
    o += '        Parameters:\n'

    for attribute in surface.attributes:
        o += f'            {attribute.name}: {attribute.description}.\n'

    o += '\n'
    o += '        Raises:\n'
    o += '            McnpError: INVALID_SURFACE_NUMBER.\n'
    o += '            McnpError: INVALID_SURFACE_TRANSFORMPERIODIC.\n'
    o += '            McnpError: INVALID_SURFACE_WHITEBOUNDARY.\n'
    o += '            McnpError: INVALID_SURFACE_REFLECTING.\n'
    o += '            McnpError: INVALID_SURFACE_PARAMETER.\n'
    o += '        """\n'
    o += '\n'
    o += '        if number is None or not (1 <= number <= 99_999_999):\n'
    o += '            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_NUMBER, str(number))\n'
    o += '\n'
    o += '        if transform is not None and not (-99_999_999 <= transform <= 999):\n'
    o += '            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_TRANSFORMPERIODIC, str(transform))\n'
    o += '\n'
    o += '        if is_whiteboundary is None:\n'
    o += '            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_WHITEBOUNDARY, str(is_whiteboundary))\n'
    o += '\n'
    o += '        if is_reflecting is None or (is_reflecting and is_whiteboundary):\n'
    o += '            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_REFLECTING, str(is_reflecting))\n'
    o += '\n'

    for attribute in surface.attributes:
        o += f'        if {attribute.name} is None:\n'
        o += f'            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str({attribute.name}))\n'
        o += '\n'

    o += '        self.ident: Final[int] =  number.value\n'
    o += '        self.number: Final[types.McnpInteger] = number\n'
    o += f'        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.{surface.enum}\n'
    o += '        self.transform: Final[types.McnpInteger] = transform\n'
    o += '        self.is_reflecting: Final[bool] = is_reflecting\n'
    o += '        self.is_whiteboundary: Final[bool] = is_whiteboundary\n'
    o += '\n'

    t = []
    for attribute in surface.attributes:
        o += f'        self.{attribute.name}: Final[types.McnpReal] = {attribute.name}\n'
        t.append(f'{attribute.name}')

    o += f'        self.parameters: Final[tuple[types.McnpReal]] = tuple([{", ".join(t)}])\n'
    o += '\n'

    # SURFACE.from_mcnp

    o += '    @staticmethod\n'
    o += '    def from_mcnp(source: str):\n'
    o += '        """\n'
    o += f'        Generates ``{surface.name}`` objects from INP.\n'
    o += '\n'
    o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
    o += '\n'
    o += '        Parameters:\n'
    o += '            source: INP for surface.\n'
    o += '\n'
    o += '        Returns:\n'
    o += f'            ``{surface.name}`` object.\n'
    o += '\n'
    o += '        Raises:\n'
    o += '            McnpError: EXPECTED_TOKEN.\n'
    o += '            McnpError: UNEXPECTED_TOKEN.\n'
    o += '            McnpError: UNRECOGNIZED_KEYWORD.\n'
    o += '        """\n'
    o += '\n'
    o += '        source = _parser.Preprocessor.process_inp(source)\n'
    o += '        source, comments = _parser.Preprocessor.process_inp_comments(source)\n'
    o += '        tokens = _parser.Parser(\n'
    o += '            source.split(" "),\n'
    o += '            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),\n'
    o += '        )\n'
    o += '\n'
    o += '        if tokens.peekl()[0] == "+":\n'
    o += '            is_whiteboundary = True\n'
    o += '            is_reflecting = False\n'
    o += '            tokens.pushl(tokens.popl()[1:])\n'
    o += '        elif tokens.peekl()[0] == "*":\n'
    o += '            is_whiteboundary = False\n'
    o += '            is_reflecting = True\n'
    o += '            tokens.pushl(tokens.popl()[1:])\n'
    o += '        else:\n'
    o += '            is_whiteboundary = False\n'
    o += '            is_reflecting = False\n'
    o += '\n'
    o += '        number = types.McnpInteger.from_mcnp(tokens.popl())\n'
    o += '\n'
    o += '        try:\n'
    o += '            transform = types.McnpInteger.from_mcnp(tokens.peekl())\n'
    o += '            tokens.popl()\n'
    o += '        except Exception:\n'
    o += '            transform = None\n'
    o += '\n'
    o += f'        if tokens.popl() != "{surface.mnemonic}":\n'
    o += '            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, info=source)\n'
    o += '\n'

    t = []
    for attribute in surface.attributes:
        o += f'        {attribute.name} = types.McnpReal.from_mcnp(tokens.popl())\n'
        t.append(attribute.name)

    o += '\n'
    o += f'        return {surface.name}(number, transform, {", ".join(t)}, is_whiteboundary=is_whiteboundary, is_reflecting=is_reflecting)\n'
    o += '\n'

    return o


init_imports = []
init_all = []

for surface in _data.SURFACE_CARDS:
    filename = pathlib.Path(__file__).parent / pathlib.Path(
        f'../src/pymcnp/files/inp/surface_cards/{surface.name.lower()}.py'
    )
    with filename.open('w') as file:
        file.write(
            f'"""\n Contains the ``{surface.name}`` subclass of ``Surface``.\n"""\n\n'
            + build_Surface(surface)
        )
        init_imports.append(f'from .{surface.name.lower()} import {surface.name}')
        init_all.append(f'"{surface.name}",')

init_path = pathlib.Path(__file__).parent / pathlib.Path(
    '../src/pymcnp/files/inp/surface_cards/__init__.py'
)
# with init_path.open('w') as file:
#     file.write(
#         '\n'.join(init_imports) + '\n\n__all__ = [\n    ' + '\n    '.join(init_all) + '\n]\n'
#     )
