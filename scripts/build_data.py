"""
Contains script for building ``Data`` subclasses.
"""

import pathlib

import _data


def build_DataEntry(entry: _data.DataEntryScheme):
    o = ''

    # DATA.ENTRY

    o += f'class {entry.name}Entry(DataEntry):\n'
    o += '    """\n'
    o += f'    Represents INP {entry.mnemonic} data card entry.\n'
    o += '\n'
    o += f'    ``{entry.name}Entry`` implements ``DataEntry``.\n'
    o += '\n'
    o += '    Attributes:\n'

    for attribute in entry.attributes:
        o += f'        {attribute.name}: {attribute.description}.\n'

    o += '    """\n'
    o += '\n'

    # DATA.ENTRY.__init__

    o += f'    def __init__(self, {", ".join(f'{attribute.name}: {attribute.type}' for attribute in entry.attributes)}):\n'
    o += '        """\n'
    o += f'        Initializes ``{entry.name}Entry``.\n'
    o += '\n'
    o += '        Parameters:\n'

    for attribute in entry.attributes:
        o += f'            {attribute.name}: {attribute.description}.\n'

    o += '\n'
    o += '        Raises:\n'

    for attribute in entry.attributes:
        o += f'            McnpError: {attribute.error}.\n'

    o += '        """\n'
    o += '\n'

    for attribute in entry.attributes:
        if attribute.restriction:
            o += f'        if {attribute.name} is None or not ({attribute.restriction}):\n'
        else:
            o += f'        if {attribute.name} is None:\n'

        o += f'            raise errors.McnpError(errors.McnpCode.{attribute.error})\n'

        if attribute.type.startswith('tuple'):
            o += '\n'
            o += f'        for entry in {attribute.name}:\n'

            if attribute.restriction:
                o += f'            if entry is None or not ({attribute.restriction}):\n'
            else:
                o += '            if entry is None:\n'

            o += (
                '                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)\n'
            )

        o += '\n'

    for attribute in entry.attributes:
        o += f'        self.{attribute.name}: Final[{attribute.type}] = {attribute.name}\n'

    o += '\n'

    # DATA.ENTRY.from_mcnp

    o += '    @staticmethod\n'
    o += '    def from_mcnp(source: str):\n'
    o += '        """\n'
    o += f'        Generates ``{entry.name}Entry`` objects from INP.\n'
    o += '\n'
    o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
    o += '\n'
    o += '        Parameters:\n'
    o += f'            source: INP for ``{entry.name}Entry``.\n'
    o += '\n'
    o += '        Returns:\n'
    o += f'            ``{entry.name}Entry`` object.\n'
    o += '\n'
    o += '        Raises:\n'
    o += '            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.\n'
    o += '        """\n'
    o += '\n'
    o += '        source = _parser.Preprocessor.process_inp(source)\n'
    o += '        tokens = _parser.Parser(source.split(" "), errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source))\n'
    o += '\n'

    for attribute in entry.attributes:
        if attribute.type != 'str':
            o += f'        {attribute.name} = {attribute.type}.from_mcnp(tokens.popl())\n'
        else:
            o += f'        {attribute.name} = tokens.popl()\n'

    o += '\n'
    o += '        if tokens:\n'
    o += '           raise errors.McnpError(errors.McnpCode.UNEXPECTED_TOKEN)\n'
    o += '\n'
    o += f'        return {entry.name}Entry({", ".join(f'{attribute.name}' for attribute in entry.attributes)})\n'
    o += '\n'

    # DATA.ENTRY.to_mcnp

    o += '\n'
    o += '    def to_mcnp(self):\n'
    o += '        """\n'
    o += f'        Generates INP from ``{entry.name}Entry`` objects.\n'
    o += '\n'
    o += '        ``to_mcnp`` translates from PyMCNP to INP.\n'
    o += '\n'
    o += '        Returns:\n'
    o += f'            INP for ``{entry.name}Entry``.\n'
    o += '        """\n'
    o += '\n'

    t = []
    for attribute in entry.attributes:
        if attribute.type != 'str':
            t.append(f'{{self.{attribute.name}.to_mcnp()}}')
        else:
            t.append(f'{{self.{attribute.name}}}')

    o += f'        return f"{" ".join(t)}"\n'
    o += '\n'

    return o


def build_DataKeyword(mnemonic: str, options: tuple[_data.DataOptionScheme]):
    o = ''

    # DATA.KEYWORD

    o += f'class {data.name}Keyword(DataKeyword):\n'
    o += '    """\n'
    o += f'    Represents INP {mnemonic} data card option keywords.\n'
    o += '\n'
    o += f'    ``{data.name}Keyword`` implements ``DataKeyword``.\n'
    o += '    """\n'
    o += '\n'

    for option in options:
        o += f'    {option.enum} = "{option.mnemonic}"\n'

    o += '\n'

    # DATA.KEYWORD.from_mcnp

    o += '    @staticmethod\n'
    o += '    def from_mcnp(source: str):\n'
    o += '        """\n'
    o += f'        Generates ``{data.name}Keyword`` objects from INP.\n'
    o += '\n'
    o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
    o += '\n'
    o += '        Parameters:\n'
    o += f'            source: INP for ``{data.name}Keyword``.\n'
    o += '\n'
    o += '        Returns:\n'
    o += f'            ``{data.name}Keyword`` object.\n'
    o += '\n'
    o += '        Raises:\n'
    o += '            McnpError: INVALID_DATUM_KEYWORD.\n'
    o += '        """\n'
    o += '\n'
    o += '        source = _parser.Preprocessor.process_inp(source)\n'
    o += '\n'
    o += '        try:\n'
    o += f'            return {data.name}Keyword\n'
    o += '        except ValueError:\n'
    o += '            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)\n'
    o += '\n'

    return o


def build_DataOption(option: _data.DataOptionScheme):
    o = ''

    # DATA.OPTION

    o += f'class {option.name}(DataOption):\n'
    o += '    """\n'
    o += f'    Represents INP {option.mnemonic} data card {option.mnemonic} options.\n'
    o += '\n'
    o += f'    ``{option.name}`` implements ``DataOption``.\n'
    o += '\n'
    o += '    Attributes:\n'
    o += f'        {option.attribute.name}: {option.attribute.description}.\n'
    o += '    """\n'
    o += '\n'

    # DATA.OPTION.__init__

    o += f'    def __init__(self, {option.attribute.name}: {option.attribute.type}):\n'
    o += '        """\n'
    o += f'        Initializes ``{data.name}``.\n'
    o += '\n'
    o += '        Parameters:\n'
    o += f'            {option.attribute.name}: {option.attribute.description}.\n'
    o += '\n'
    o += '        Raises:\n'
    o += '            McnpError: INVALID_DATUM_VALUE.\n'
    o += '        """\n'
    o += '\n'

    o += f'        if {option.attribute.name} is None:\n'
    o += '            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)\n'

    if option.attribute.type.startswith('tuple'):
        o += f'        for entry in {option.attribute.name}:\n'

        if option.attribute.restriction:
            o += f'            if entry is None or not ({option.attribute.restriction}):\n'
        else:
            o += '            if entry is None:\n'

        o += f'                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str({option.attribute.name}))\n'

    o += '\n'

    o += f'        self.keyword: Final[{data.name}Keyword] = {data.name}Keyword.{option.enum}\n'
    o += f'        self.value: Final[{option.attribute.type}] = {option.attribute.name}\n'
    o += f'        self.{option.attribute.name}: Final[{option.attribute.type}] = {option.attribute.name}\n'
    o += '\n'

    # DATA.OPTION.from_mcnp

    o += '    @staticmethod\n'
    o += '    def from_mcnp(source: str):\n'
    o += '        """\n'
    o += f'        Generates ``{option.name}`` objects from INP.\n'
    o += '\n'
    o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
    o += '\n'
    o += '        Parameters:\n'
    o += f'            source: INP for ``{option.name}``.\n'
    o += '\n'
    o += '        Returns:\n'
    o += f'            ``{option.name}`` object.\n'
    o += '\n'
    o += '        Raises:\n'
    o += '            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.\n'
    o += '        """\n'
    o += '\n'
    o += '        source = _parser.Preprocessor.process_inp(source)\n'
    o += '        tokens = _parser.Parser(\n'
    o += '            re.split(r"=| ", source),\n'
    o += '            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),\n'
    o += '        )\n'
    o += '\n'
    o += f'        if tokens.popl() != "{option.mnemonic}":\n'
    o += '            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)\n'
    o += '\n'

    if option.attribute.type.startswith('tuple'):
        inner_type = option.attribute.type[len('tuple[') : -1]

        if inner_type == 'str':
            o += '        value = tuple([tokens.popl() for _ in range(0, len(tokens))])\n'
        else:
            o += f'        value = tuple([{inner_type}.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])\n'

    elif option.attribute.type == 'str':
        o += '        value = tokens.popl()\n'

    elif option.attribute.type.startswith('Union'):
        inside_types = option.attribute.type[len('Union[') : -1].split(', ')

        for inside_type in inside_types:
            o += '        try:\n'

            if inside_type.startswith('tuple'):
                inside_inside_type = inside_type[len('tuple[') : -1]

                if inside_inside_type == 'str':
                    # Union[tuple[str], ..]
                    o += '                value = [tokens.popl() for _ in range(0, len(tokens))]\n'
                else:
                    # Union[tuple[?], ..]
                    o += f'                value = [{inside_inside_type}.popl() for _ in range(0, len(tokens))]\n'
            elif inside_type == 'str':
                # Union[str, ..]
                o += '                value = tokens.popl()\n'
            else:
                # Union[?, ..]
                o += f'                value = {inside_type}.from_mcnp(tokens.popl())\n'

            o += '        except Exception:\n'
            o += '            pass\n'

    else:
        o += f'        value = {option.attribute.type}.from_mcnp(tokens.popl())\n'

    o += '\n'
    o += f'        return {option.name}(value)\n'
    o += '\n'

    return o


def build_Data(data: _data.DataScheme):
    o = ''

    o += '"""\n'
    o += f'Contains the ``{data.name}`` subclass of ``Data``.\n'
    o += '"""\n'
    o += '\n'
    o += 'import re\n'
    o += 'from typing import Final, Union\n'
    o += '\n'
    o += 'from ..data import Data\n'
    o += 'from ..data_mnemonic import DataMnemonic\n'
    o += 'from ..data_entry import DataEntry\n' if data.entries else ''
    o += 'from ..data_option import DataOption\n' if data.options else ''
    o += 'from ..data_keyword import DataKeyword\n' if data.options else ''
    o += 'from ...utils import types\n'
    o += 'from ...utils import errors\n'
    o += 'from ...utils import _parser\n'
    o += '\n'

    # DATA.ENTRY

    for entry in data.entries:
        o += build_DataEntry(entry)

    # DATA.OPTION

    if data.options:
        o += build_DataKeyword(data.mnemonic, data.options)

        for option in data.options:
            o += build_DataOption(option)

    # DATA

    o += f'class {data.name}(Data):\n'
    o += '    """\n'
    o += f'    Represents INP {data.mnemonic} data cards.\n'
    o += '\n'
    o += f'    ``{data.name}`` implements ``Data``.\n'
    o += '\n'
    o += '    Attributes:\n'

    for attribute in data.attributes:
        o += f'        {attribute.name}: {attribute.description}.\n'

    o += '    """\n'
    o += '\n'

    # DATA.__init__

    t = []
    for attribute in data.attributes:
        t.append(f'{attribute.name}: {attribute.type}')

    o += f'    def __init__(self, {", ".join(f'{attribute.name}: {attribute.type}' for attribute in data.attributes)}):\n'
    o += '        """\n'
    o += f'        Initializes ``{data.name}``.\n'
    o += '\n'
    o += '        Parameters:\n'

    for attribute in data.attributes:
        o += f'            {attribute.name}: {attribute.description}.\n'

    o += '\n'
    o += '        Raises:\n'
    o += '            McnpError: INVALID_DATUM_PARAMETERS.\n'
    o += '        """\n'
    o += '\n'

    for attribute in data.attributes:
        if attribute.type.startswith('tuple'):
            o += f'        if {attribute.name} is None:\n'
            o += f'            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str({attribute.name}))\n'
            o += '\n'
            o += f'        for entry in {attribute.name}:\n'

            if attribute.restriction:
                o += f'            if entry is None or not ({attribute.restriction}):\n'
            else:
                o += '            if entry is None:\n'

            o += f'                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str({attribute.name}))\n'
        else:
            if attribute.restriction:
                o += f'        if {attribute.name} is None or not ({attribute.restriction}):\n'
            else:
                o += f'        if {attribute.name} is None:\n'

            o += f'            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str({attribute.name}))\n'

        o += '\n'

    o += f'        self.mnemonic: Final[DataMnemonic] = DataMnemonic.{data.enum}\n'

    t = []
    for attribute in data.attributes:
        if attribute.type.startswith('tuple'):
            t.append(f'list({attribute.name})')
        else:
            t.append(f'[{attribute.name}]')

    o += f'        self.parameters: Final[tuple[any]] = tuple({" + ".join(t)})\n'

    for attribute in data.attributes:
        o += f'        self.{attribute.name}: Final[{attribute.type}] = {attribute.name}\n'

    attribute_names = [attribute.name for attribute in data.attributes]
    if 'suffix' in attribute_names and 'designator' in attribute_names:
        o += f'        self.ident: Final[str] = f"{data.mnemonic}{{self.suffix}}:{{self.designator}}"\n'
    elif 'designator' in attribute_names:
        o += f'        self.ident: Final[str] = f"{data.mnemonic}:{{self.designator}}"\n'
    elif 'suffix' in attribute_names:
        o += f'        self.ident: Final[str] = f"{data.mnemonic}{{self.suffix}}"\n'
    else:
        o += f'        self.ident: Final[str] = "{data.mnemonic}"\n'

    o += '\n'

    # DATA.from_mcnp

    o += '    @staticmethod\n'
    o += '    def from_mcnp(source: str):\n'
    o += '        """\n'
    o += f'        Generates ``{data.name}`` objects from INP.\n'
    o += '\n'
    o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
    o += '\n'
    o += '        Parameters:\n'
    o += f'            source: INP for {data.mnemonic} data cards.\n'
    o += '\n'
    o += '        Returns:\n'
    o += f'            ``{data.name}`` object.\n'
    o += '\n'
    o += '        Raises:\n'
    o += '            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN, KEYWORD_DATUM_MNEMONIC.\n'
    o += '        """\n'
    o += '\n'
    o += '        source = _parser.Preprocessor.process_inp(source)\n'
    o += '        source, comments = _parser.Preprocessor.process_inp_comments(source)\n'
    o += '        tokens = _parser.Parser(\n'
    o += '            re.split(r" |:|=", source),\n'
    o += '            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),\n'
    o += '        )\n'
    o += '\n'
    o += '        mnemonic = re.search(r"^[a-zA-Z*]+", tokens.peekl())\n'
    o += '        mnemonic = mnemonic[0] if mnemonic else ""\n'
    o += f'        if mnemonic != "{data.mnemonic}":\n'
    o += '            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)\n'
    o += '\n'

    attributes = data.attributes
    if 'designator' in attribute_names:
        o += '        designator = types.Designator.from_mcnp(tokens.popl())\n'
        attributes = attributes[:-1]

    if 'suffix' in attribute_names:
        o += f'        suffix = types.McnpInteger.from_mcnp(tokens.popl()[{len(data.mnemonic)}:])\n'
        attributes = attributes[:-1]
    else:
        o += '        tokens.popl()\n'

    o += '\n'

    for attribute in data.attributes:
        if attribute.name == 'suffix' or attribute.name == 'designator':
            continue

        if attribute.type.endswith('Option]'):
            # tuple[..Option]

            o += f'        {attribute.name} = {{}}\n'
            o += f'        keywords = re.findall(r"{'|'.join([option.mnemonic for option in data.options])}", " ".join(tokens.deque))\n'
            o += f'        values = re.split(r"{'|'.join([option.mnemonic for option in data.options])}", " ".join(tokens.deque))[1:]\n'
            o += '        for keyword, value in zip(keywords, values):\n'
            o += '            match keyword:\n'

            for option in data.options:
                o += f'                case "{option.mnemonic}":\n'
                o += f'                    {attribute.name}["{option.mnemonic}"] = {option.name}.from_mcnp(f"{{keyword}}={{value}}")\n'

            o += '\n'

        elif attribute.type.startswith('Union'):
            inside_types = attribute.type[len('Union[') : -1].split(', ')

            a = True
            for inside_type in inside_types:
                o += f'        {'if' if a else 'elif'} isinstance(inside_type, {inside_type}):\n'

                if inside_type.startswith('tuple'):
                    inside_inside_type = inside_type[len('tuple[') : -1]

                    if inside_inside_type == 'str':
                        # Union[tuple[str], ..]
                        o += f'            {attribute.name} = [tokens.popl() for _ in range(0, len(tokens))]\n'
                    else:
                        # Union[tuple[?], ..]
                        o += f'            {attribute.name} = [{inside_inside_type}.popl() for _ in range(0, len(tokens))]\n'
                elif inside_type == 'str':
                    # Union[str, ..]
                    o += f'            {attribute.name} = tokens.popl()\n'
                else:
                    # Union[?, ..]
                    o += f'            {attribute.name} = {inside_type}.from_mcnp(tokens.popl())\n'

                a = False

        elif attribute.type.startswith('tuple'):
            inside_type = attribute.type[len('tuple[') : -1]

            if inside_type == 'str':
                # tuple[str]
                o += f'        {attribute.name} = [tokens.popl() for _ in range(0, len(tokens))]\n'
            elif 'Entry' in inside_type:
                # ENTRY
                index = [entry.name for entry in data.entries].index(inside_type[:-5])
                entry_attributes = len(data.entries[index].attributes)
                o += f'        {attribute.name} = [{inside_type}.from_mcnp(" ".join([tokens.popl() for __ in range(0, {entry_attributes})])) for _ in range(0, len(tokens), {entry_attributes})]\n'
            else:
                # tuple[?]
                o += f'        {attribute.name} = [{inside_type}.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]\n'

        elif attribute.type == 'str':
            # str
            o += f'        {attribute.name} = tokens.popl()\n'

        elif 'Entry' in attribute.type:
            # ENTRY
            index = [entry.name for entry in data.entries].index(attribute.type[:-5])
            entry_attributes = len(data.entries[index].attributes)
            o += f'        {attribute.name} = {attribute.type}.from_mcnp(" ".join([tokens.popl() for _ in range(0, {entry_attributes})]))\n'
        else:
            # ?
            o += f'        {attribute.name} = {attribute.type}.from_mcnp(tokens.popl())\n'

    o += '\n'
    o += f'        data = {data.name}({", ".join(f'{attribute.name}' for attribute in data.attributes)})\n'
    o += '        data.comment = comments\n'
    o += '\n'
    o += '        return data\n'
    o += '\n'

    # DATA.to_mcnp

    o += '    def to_mcnp(self) -> str:\n'
    o += '        """\n'
    o += f'        Generates INP from ``{data.name}`` objects.\n'
    o += '\n'
    o += '        ``to_mcnp`` translates from PyMCNP to INP.\n'
    o += '\n'
    o += '        Returns:\n'
    o += f'            INP for ``{data.name}``.\n'
    o += '        """\n'
    o += '\n'

    if 'suffix' in attribute_names and 'designator' in attribute_names:
        o += '        return _parser.Postprocessor.add_continuation_lines(f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()}:{self.designator.to_mcnp()}'
    elif 'designator' in attribute_names:
        o += '        return _parser.Postprocessor.add_continuation_lines(f"{self.mnemonic.to_mcnp()}:{self.designator.to_mcnp()}'
    elif 'suffix' in attribute_names:
        o += '        return _parser.Postprocessor.add_continuation_lines(f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()}'
    else:
        o += '        return _parser.Postprocessor.add_continuation_lines(f"{self.mnemonic.to_mcnp()}'

    for attribute in data.attributes:
        if attribute.name == 'designator' or attribute.name == 'suffix':
            continue

        if attribute.type.startswith('tuple'):
            o += f" {{' '.join(entry.to_mcnp() for entry in self.{attribute.name})}}"
        elif attribute.type.startswith('dict'):
            o += f" {{' '.join(entry.to_mcnp() for entry in self.{attribute.name}.values())}}"
        else:
            o += f' {{self.{attribute.name}.to_mcnp()}}'

    o += '")\n'
    o += '\n'

    return o


init_imports = []
init_all = []

for data in _data.DATA_CARDS:
    filename = pathlib.Path(__file__).parent / pathlib.Path(
        f'../src/pymcnp/files/inp/data_cards/{data.name.lower()}.py'
    )
    with filename.open('w') as file:
        file.write(build_Data(data))
        init_imports.append(f'from .{data.name.lower()} import {data.name}')
        init_all.append(f'"{data.name}",')

init_path = pathlib.Path(__file__).parent / pathlib.Path(
    '../src/pymcnp/files/inp/data_cards/__init__.py'
)
with init_path.open('w') as file:
    file.write(
        '\n'.join(init_imports) + '\n\n__all__ = [\n    ' + '\n    '.join(init_all) + '\n]\n'
    )
