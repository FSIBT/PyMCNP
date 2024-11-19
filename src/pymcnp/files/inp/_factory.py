# ruff: noqa

from ..utils import types


_DEBUG_DATA = False
_DEBUG_CELL = True
_DEBUG_SURFACE = False

_DEBUG_DATA_TEST = False
_DEBUG_CELL_TEST = False
_DEBUG_SURFACE_TEST = False


def debug_print(o):
    for i, line in enumerate(o.split('\n')):
        print(f'{i + 1:03d} : {line}')


class AttributeFactory:
    def __init__(self, name, type, description, restriction):
        self.name = name
        self.type = type
        self.description = description
        self.restriction = restriction


class DataFactory:
    def __init__(self, mnemonic, has_suffix, has_designator, attributes, entries, options):
        self.mnemonic = mnemonic
        self.name = mnemonic[0].upper() + mnemonic[1:]
        self.enum = mnemonic.upper()
        self.has_suffix = has_suffix
        self.has_designator = has_designator
        self.attributes = attributes
        self.entries = entries
        self.options = options

        if options:
            self.attributes.append(
                AttributeFactory('pairs', 'dict[DataOption]', 'Dictionary of options', '')
            )

    def build(self):
        o = ''

        # DATA.ENTRY

        for entry in self.entries:
            o += entry.build()

        # DATA.OPTION

        if self.options:
            o += DataKeywordFactory(self.mnemonic, self.options).build()

        for option in self.options:
            o += option.build(self.name, self.mnemonic)

        # DATA

        o += f'class {self.name}(Data):\n'
        o += f'    """\n'
        o += f'    Represents INP {self.mnemonic} data cards.\n'
        o += f'\n'
        o += f'    ``{self.name}`` implements ``Data``\n.'
        o += f'\n'
        o += f'    Attributes:\n'

        for attribute in self.attributes:
            o += f'        {attribute.name}: {attribute.description}.\n'

        if self.has_suffix:
            o += f'        suffix: card suffix.\n'

        if self.has_designator:
            o += f'        designator: card designator.\n'

        o += f'    """\n'
        o += f'\n'

        # DATA.__init__

        t = []
        for attribute in self.attributes:
            t.append(f'{attribute.name}: {attribute.type}')

        if self.has_suffix:
            t.append('suffix: types.McnpInteger')

        if self.has_designator:
            t.append('designator: types.Designator')

        o += f'    def __init__(self, {", ".join(t)}):\n'
        o += f'        """\n'
        o += f'        Initializes ``{self.name}``.\n'
        o += f'\n'
        o += f'        Parameters:\n'

        for attribute in self.attributes:
            o += f'            {attribute.name}: {attribute.description}.\n'

        if self.has_suffix:
            o += f'            suffix: card suffix.\n'

        if self.has_designator:
            o += f'            designator: card designator.\n'

        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSemanticError: INVALID_DATUM_PARAMETERS.\n'
        o += f'        """\n'
        o += f'\n'

        for attribute in self.attributes:
            o += f'        if {attribute.name} is None:\n'
            o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)\n'

            if attribute.type.startswith('tuple'):
                o += f'\n'
                o += f'        for entry in {attribute.name}:\n'

                if attribute.restriction:
                    o += f'            if entry is None or not ({attribute.restriction}):\n'
                else:
                    o += f'            if entry is None:\n'

                o += f'                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)\n'

            o += f'\n'

        if self.has_suffix:
            o += f'        if suffix is None:\n'
            o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)\n'
            o += f'\n'

        if self.has_designator:
            o += f'        if designator is None:\n'
            o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)\n'
            o += f'\n'

        o += f'        self.mnemonic: Final[DataMnemonic] = DataMnemonic.{self.enum}\n'

        t = []
        for attribute in self.attributes:
            if attribute.type.startswith('tuple'):
                t.append(f'list({attribute.name})')
            else:
                t.append(f'[{attribute.name}]')

        o += f'        self.parameters: Final[tuple[any]] = tuple({" + ".join(t)})\n'

        if self.has_suffix:
            o += f'        self.suffix: Final[types.McnpInteger] = suffix\n'

        if self.has_designator:
            o += f'        self.designator: Final[types.Designator] = designator\n'

        for attribute in self.attributes:
            o += f'        self.{attribute.name}: Final[{attribute.type}] = {attribute.name}\n'

        if self.has_suffix and self.has_designator:
            o += f'        self.ident: Final[str] = f"{self.mnemonic}{{self.suffix}}:{{self.designator}}"\n'
        elif self.has_designator:
            o += f'        self.ident: Final[str] = f"{self.mnemonic}:{{self.designator}}"\n'
        elif self.has_suffix:
            o += f'        self.ident: Final[str] = f"{self.mnemonic}{{self.suffix}}"\n'
        else:
            o += f'        self.ident: Final[str] = f"{self.mnemonic}"\n'

        o += f'\n'

        # DATA.from_mcnp

        o += f'    @staticmethod\n'
        o += f'    def from_mcnp(source: str):\n'
        o += f'        """\n'
        o += f'        Generates ``{self.name}`` objects from INP.\n'
        o += f'\n'
        o += f'        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += f'\n'
        o += f'        Parameters:\n'
        o += f'            source: INP for {self.mnemonic} data cards.\n'
        o += f'\n'
        o += f'        Returns:\n'
        o += f'            ``{self.name}`` object.\n'
        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSyntaxError: TOOFEW_DATUM, TOOLONG_DATUM, KEYWORD_DATUM_MNEMONIC.\n'
        o += f'        """\n'
        o += f'\n'
        o += f'        source = _parser.Preprocessor.process_inp(source)\n'
        o += f'        source, comments = _parser.Preprocessor.process_inp_comments(source)\n'
        o += f'        tokens = _parser.Parser(\n'
        o += f'            re.split(r" |:|=", source),\n'
        o += f'            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM),\n'
        o += f'        )\n'
        o += f'\n'
        o += f'        mnemonic = re.search(r"^[a-zA-Z*]+", tokens.peekl())\n'
        o += f'        mnemonic = mnemonic[0] if mnemonic else ""\n'
        o += f'        if mnemonic != "{self.mnemonic}":\n'
        o += f'            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD_DATUM_MNEMONIC)\n'
        o += f'\n'

        if self.has_suffix:
            o += f'        suffix = types.McnpInteger.from_mcnp(tokens.popl()[{len(self.mnemonic)}:])\n'
        else:
            o += f'        tokens.popl()\n'

        if self.has_designator:
            o += f'        designator = types.Designator.from_mcnp(tokens.popl())\n'

        o += f'\n'

        for attribute in self.attributes:
            if attribute.type.endswith('Option]'):
                # tuple[...Option]

                o += f'        {attribute.name} = {{}}\n'
                o += f'        keywords = re.findall(r"{'|'.join([option.mnemonic for option in self.options])}", " ".join(tokens.deque))\n'
                o += f'        values = re.split(r"{'|'.join([option.mnemonic for option in self.options])}", " ".join(tokens.deque))[1:]\n'
                o += f'        for keyword, value in zip(keywords, values):\n'
                o += f'            match keyword:\n'

                for option in self.options:
                    o += f'                case "{option.mnemonic}":\n'
                    o += f'                    {attribute.name}["{option.mnemonic}"] = {self.name}{option.name}.from_mcnp(f"{{keyword}}={{value}}")\n'

                o += f'\n'

            elif attribute.type.startswith('tuple'):
                inside_type = attribute.type[len('tuple[') : -1]

                if inside_type == 'str':
                    # tuple[str]
                    o += f'        {attribute.name} = [tokens.popl() for _ in range(0, len(tokens))]\n'
                elif 'Entry' in inside_type:
                    # ENTRY
                    index = [entry.name for entry in self.entries].index(inside_type[:-5])
                    entry_attributes = len(self.entries[index].attributes)
                    o += f'        {attribute.name} = [{inside_type}.from_mcnp(" ".join([tokens.popl() for __ in range(0, {entry_attributes})])) for _ in range(0, len(tokens), {entry_attributes})]\n'
                else:
                    # tuple[?]
                    o += f'        {attribute.name} = [{inside_type}.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))]\n'

            elif attribute.type == 'str':
                # str
                o += f'        {attribute.name} = tokens.popl()\n'

            elif 'Entry' in attribute.type:
                # ENTRY
                index = [entry.name for entry in self.entries].index(attribute.type[:-5])
                entry_attributes = len(self.entries[index].attributes)
                o += f'        {attribute.name} = {attribute.type}.from_mcnp(" ".join([tokens.popl() for _ in range(0, {entry_attributes})]))\n'
            else:
                # object
                o += f'        {attribute.name} = {attribute.type}.from_mcnp(tokens.popl())\n'

        o += f'\n'

        t = []
        for attribute in self.attributes:
            t.append(f'{attribute.name}')

        if self.has_suffix:
            t.append(f'suffix = suffix')

        if self.has_designator:
            t.append(f'designator = designator')

        o += f'        data = {self.name}({", ".join(t)})\n'
        o += f'        data.comment = comments\n'
        o += f'\n'
        o += f'        return data\n'
        o += f'\n'

        # DATA.to_mcnp

        o += f'    def to_mcnp(self) -> str:\n'
        o += f'        """\n'
        o += f'        Generates INP from ``{self.name}`` objects.\n'
        o += f'\n'
        o += f'        ``to_mcnp`` translates from PyMCNP to INP.\n'
        o += f'\n'
        o += f'        Returns:\n'
        o += f'            INP for ``{self.name}``.\n'
        o += f'        """\n'
        o += f'\n'

        if self.has_suffix and self.has_designator:
            o += f'        return _parser.Postprocessor.add_continuation_lines(f"{{self.mnemonic.to_mcnp()}}{{self.suffix.to_mcnp()}}:{{self.designator.to_mcnp()}}'
        elif self.has_designator:
            o += f'        return _parser.Postprocessor.add_continuation_lines(f"{{self.mnemonic.to_mcnp()}}:{{self.designator.to_mcnp()}}'
        elif self.has_suffix:
            o += f'        return _parser.Postprocessor.add_continuation_lines(f"{{self.mnemonic.to_mcnp()}}{{self.suffix.to_mcnp()}}'
        else:
            o += f'        return _parser.Postprocessor.add_continuation_lines(f"{{self.mnemonic.to_mcnp()}}'

        for attribute in self.attributes:
            if attribute.type.startswith('tuple'):
                o += f' {{" ".join(entry.to_mcnp() for entry in self.{attribute.name})}}'
            elif attribute.type.startswith('dict'):
                o += f' {{" ".join(entry.to_mcnp() for entry in self.{attribute.name}.values())}}'
            else:
                o += f' {{self.{attribute.name}.to_mcnp()}}'

        o += f'")\n'
        o += f'\n'

        if _DEBUG_DATA:
            debug_print(o)

        return o


class DataEntryFactory:
    def __init__(self, mnemonic, attributes):
        self.mnemonic = mnemonic
        self.name = mnemonic[0].upper() + mnemonic[1:]
        self.attributes = attributes

    def build(self):
        # DATA.ENTRY

        o = ''
        o += f'class {self.name}Entry(DataEntry):\n'
        o += f'    """\n'
        o += f'    Represents INP {self.mnemonic} data card entry.\n'
        o += f'\n'
        o += f'    ``{self.name}Entry`` implements ``DataEntry``\n.'
        o += f'\n'
        o += f'    Attributes:\n'

        for attribute in self.attributes:
            o += f'            {attribute.name}: {attribute.description}.\n'

        o += f'    """\n'
        o += f'\n'

        t = []
        for attribute in self.attributes:
            t.append(f'{attribute.name}: {attribute.type}')

        # DATA.ENTRY.__init__

        o += f'    def __init__(self, {", ".join(t)}):\n'
        o += f'        """\n'
        o += f'        Initializes ``{self.name}Entry``.\n'
        o += f'\n'
        o += f'        Parameters:\n'

        for attribute in self.attributes:
            o += f'                {attribute.name}: {attribute.description}.\n'

        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSemanticError: INVALID_DATUM_PARAMETERS.\n'
        o += f'        """\n'
        o += f'\n'

        for attribute in self.attributes:
            o += f'        if {attribute.name} is None:\n'
            o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)\n'

            if attribute.type.startswith('tuple'):
                o += f'\n'
                o += f'        for entry in {attribute.name}:\n'

                if attribute.restriction:
                    o += f'            if entry is None or not ({attribute.restriction}):\n'
                else:
                    o += f'            if entry is None:\n'

                o += f'                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)\n'

            o += f'\n'

        for attribute in self.attributes:
            o += f'        self.{attribute.name}: Final[{attribute.type}] = {attribute.name}\n'

        o += f'\n'

        # DATA.ENTRY.from_mcnp

        o += f'    @staticmethod\n'
        o += f'    def from_mcnp(source: str):\n'
        o += f'        """\n'
        o += f'        Generates ``{self.name}Entry`` objects from INP.\n'
        o += f'\n'
        o += f'        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += f'\n'
        o += f'        Parameters:\n'
        o += f'            source: INP for ``{self.name}Entry``.\n'
        o += f'\n'
        o += f'        Returns:\n'
        o += f'            ``{self.name}Entry`` object.\n'
        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSyntaxError: TOOFEW_DATUM, TOOLONG_DATUM.\n'
        o += f'        """\n'
        o += f'\n'
        o += f'        source = _parser.Preprocessor.process_inp(source)\n'
        o += f'        tokens = _parser.Parser(source.split(" "), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM))\n'
        o += f'\n'

        for attribute in self.attributes:
            if attribute.type != 'str':
                o += f'        {attribute.name} = {attribute.type}.from_mcnp(tokens.popl())\n'
            else:
                o += f'        {attribute.name} = tokens.popl()\n'

        o += f'\n'
        o += f'        if tokens:\n'
        o += f'           raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM)\n'
        o += f'\n'

        t = []
        for attribute in self.attributes:
            t.append(f'{attribute.name}')

        o += f'        return {self.name}Entry({", ".join(t)})\n'
        o += f'\n'

        # DATA.ENTRY.to_mcnp

        o += f'\n'
        o += f'    def to_mcnp(self):\n'
        o += f'        """\n'
        o += f'        Generates INP from ``{self.name}Entry`` objects.\n'
        o += f'\n'
        o += f'        ``to_mcnp`` translates from PyMCNP to INP.\n'
        o += f'\n'
        o += f'        Returns:\n'
        o += f'            INP for ``{self.name}Entry``.\n'
        o += f'        """\n'
        o += f'\n'

        t = []
        for attribute in self.attributes:
            if attribute.type != 'str':
                t.append(f'{{self.{attribute.name}.to_mcnp()}}')
            else:
                t.append(f'{{self.{attribute.name}}}')

        o += f'        return f"{" ".join(t)}"\n'
        o += f'\n'

        return o


class DataKeywordFactory:
    def __init__(self, mnemonic, options):
        self.mnemonic = mnemonic
        self.name = mnemonic[0].upper() + mnemonic[1:]
        self.options = options

    def build(self):
        # DATA.KEYWORD

        o = ''

        o += f'class {self.name}Keyword(DataKeyword):\n'
        o += f'    """\n'
        o += f'    Represents INP {self.mnemonic} data card option keywords.\n'
        o += f'\n'
        o += f'    ``{self.name}Keyword`` implements ``DataKeyword``\n.'
        o += f'    """\n'

        for option in self.options:
            o += f'    {option.enum} = "{option.mnemonic}"\n'

        o += f'\n'

        # DATA.KEYWORD.from_mcnp

        o += f'    @staticmethod\n'
        o += f'    def from_mcnp(source: str):\n'
        o += f'        """\n'
        o += f'        Generates ``{self.name}Keyword`` objects from INP.\n'
        o += f'\n'
        o += f'        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += f'\n'
        o += f'        Parameters:\n'
        o += f'            source: INP for ``{self.name}Keyword``.\n'
        o += f'\n'
        o += f'        Returns:\n'
        o += f'            ``{self.name}Keyword`` object.\n'
        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSemanticError: INVALID_DATUM_KEYWORD.\n'
        o += f'        """\n'
        o += f'\n'
        o += f'        source = _parser.Preprocessor.process_inp(source)\n'
        o += f'\n'
        o += f'        try:\n'
        o += f'            return {self.name}Keyword\n'
        o += f'        except:\n'
        o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_KEYWORD)\n'
        o += f'\n'

        return o


class DataOptionFactory:
    def __init__(self, mnemonic, attribute):
        self.mnemonic = mnemonic
        self.name = mnemonic[0].upper() + mnemonic[1:]
        self.enum = mnemonic.upper()
        self.attribute = attribute

    def build(self, name, mnemonic):
        # DATA.OPTION

        o = ''
        o += f'class {name}{self.name}(DataOption):\n'
        o += f'    """\n'
        o += f'    ``{name}{self.name}`` represents INP {mnemonic} data card {self.mnemonic} options.\n'
        o += f'\n'
        o += f'    ``{name}{self.name}`` implements ``DataOption``\n.'
        o += f'\n'
        o += f'    Attributes:\n'
        o += f'        {self.attribute.name}: {self.attribute.description}.\n'
        o += f'    """\n'
        o += f'\n'

        # DATA.OPTION.__init__

        o += f'    def __init__(self, {self.attribute.name}: {self.attribute.type}):\n'
        o += f'        """\n'
        o += f'        Initializes ``{name}{self.name}``.\n'
        o += f'\n'
        o += f'        Parameters:\n'
        o += f'            {self.attribute.name}: {self.attribute.description}.\n'
        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSemanticError: INVALID_DATUM_VALUE.\n'
        o += f'        """\n'
        o += f'\n'

        o += f'        if {self.attribute.name} is None:\n'
        o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)\n'

        if self.attribute.type.startswith('tuple'):
            o += f'        for entry in {self.attribute.name}:\n'

            if self.attribute.restriction:
                o += f'            if entry is None or not ({self.attribute.restriction}):\n'
            else:
                o += f'            if entry is None:\n'

            o += f'                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)\n'

        o += f'\n'

        o += f'        self.keyword: Final[{name}Keyword] = {name}Keyword.{self.enum}\n'
        o += f'        self.value: Final[{self.attribute.type}] = {self.attribute.name}\n'
        o += f'        self.{self.attribute.name}: Final[{self.attribute.type}] = {self.attribute.name}\n'
        o += f'\n'

        # DATA.OPTION.from_mcnp

        o += f'    @staticmethod\n'
        o += f'    def from_mcnp(source: str):\n'
        o += f'        """\n'
        o += f'        Generates ``{name}{self.name}`` objects from INP.\n'
        o += f'\n'
        o += f'        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += f'\n'
        o += f'        Parameters:\n'
        o += f'            source: INP for ``{name}{self.name}``.\n'
        o += f'\n'
        o += f'        Returns:\n'
        o += f'            ``{name}{self.name}`` object.\n'
        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSyntaxError: TOOFEW_DATUM, TOOLONG_DATUM.\n'
        o += f'        """\n'
        o += f'\n'
        o += f'        source = _parser.Preprocessor.process_inp(source)\n'
        o += f'        tokens = _parser.Parser(\n'
        o += f'            re.split(r"=| ", source),\n'
        o += f'            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_MATERIAL),\n'
        o += f'        )\n'
        o += f'\n'
        o += f'        keyword = {name}Keyword.from_mcnp(tokens.popl())\n'

        if self.attribute.type.startswith('tuple'):
            inner_type = self.attribute.type[len('tuple[') : -1]

            if inner_type == 'str':
                o += f'        value = tuple([tokens.popl() for _ in range(0, len(tokens))])\n'
            else:
                o += f'        value = tuple([{inner_type}.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])\n'

        elif self.attribute.type == 'str':
            o += f'        value = tokens.popl()\n'

        else:
            o += f'        value = {self.attribute.type}.from_mcnp(tokens.popl())\n'

        o += f'\n'
        o += f'        return {name}{self.name}(value)\n'
        o += f'\n'

        return o


class SurfaceFactory:
    def __init__(self, mnemonic, attributes):
        self.name = (mnemonic[0].upper() + mnemonic[1:]).replace('/', '_')
        self.enum = mnemonic.upper().replace('/', '_')
        self.mnemonic = mnemonic
        self.attributes = attributes

    def build(self):
        # SURFACE

        o = ''
        o += f'class {self.name}(Surface):\n'
        o += f'    """\n'
        o += f'    Represents INP {self.mnemonic} surface cards.\n'
        o += f'\n'
        o += f'    ``{self.name}`` implements ``Surface``\n.'
        o += f'\n'
        o += f'    Attributes:\n'

        for attribute in self.attributes:
            o += f'        {attribute.name}: {attribute.description}.\n'

        o += f'    """\n'
        o += f'\n'

        # SURFACE.__init__

        t = []
        for attribute in self.attributes:
            t.append(f'{attribute.name}: {attribute.type}')

        o += f'    def __init__(self, number: types.McnpInteger, transform: types.McnpInteger, {", ".join(t)}, is_whiteboundary: bool = False, is_reflecting: bool = False):\n'
        o += f'        """\n'
        o += f'        Initializes ``{self.name}``.\n'
        o += f'\n'
        o += f'\n'
        o += f'        Parameters:\n'

        for attribute in self.attributes:
            o += f'            {attribute.name}: {attribute.description}.\n'

        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSemanticError: INVALID_SURFACE_NUMBER.\n'
        o += f'            MCNPSemanticError: INVALID_SURFACE_TRANSFORMPERIODIC.\n'
        o += f'            MCNPSemanticError: INVALID_SURFACE_WHITEBOUNDARY.\n'
        o += f'            MCNPSemanticError: INVALID_SURFACE_REFLECTING.\n'
        o += f'            MCNPSemanticError: INVALID_SURFACE_PARAMETER.\n'
        o += f'        """\n'
        o += f'\n'
        o += f'        if number is None or not (1 <= number <= 99_999_999):\n'
        o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_NUMBER)\n'
        o += f'\n'
        o += f'        if transform is not None and not (-99_999_999 <= transform <= 999):\n'
        o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_TRANSFORMPERIODIC)\n'
        o += f'\n'
        o += f'        if is_whiteboundary is None:\n'
        o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_WHITEBOUNDARY)\n'
        o += f'\n'
        o += f'        if is_reflecting is None or (is_reflecting and is_whiteboundary):\n'
        o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_REFLECTING)\n'
        o += f'\n'

        for attribute in self.attributes:
            o += f'        if {attribute.name} is None:\n'
            o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_SURFACE_PARAMETER)\n'
            o += f'\n'

        o += f'        self.ident: Final[int] =  number.value\n'
        o += f'        self.number: Final[types.McnpInteger] = number\n'
        o += f'        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.{self.enum}\n'
        o += f'        self.transform: Final[types.McnpInteger] = transform\n'
        o += f'        self.is_reflecting: Final[bool] = is_reflecting\n'
        o += f'        self.is_whiteboundary: Final[bool] = is_whiteboundary\n'
        o += f'\n'

        t = []
        for attribute in self.attributes:
            o += f'        self.{attribute.name}: Final[types.McnpReal] = {attribute.name}\n'
            t.append(f'{attribute.name}')

        o += f'        self.parameters: Final[tuple[types.McnpReal]] = tuple([{", ".join(t)}])\n'
        o += f'\n'

        # SURFACE.from_mcnp

        o += f'    @staticmethod\n'
        o += f'    def from_mcnp(source: str):\n'
        o += f'        """\n'
        o += f'        Generates ``{self.name}`` objects from INP.\n'
        o += f'\n'
        o += f'        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += f'\n'
        o += f'        Parameters:\n'
        o += f'            source: INP for surface.\n'
        o += f'\n'
        o += f'        Returns:\n'
        o += f'            ``{self.name}`` object.\n'
        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSyntaxError: TOOFEW_SURFACE, TOOLONG_SURFACE.\n'
        o += f'        """\n'
        o += f'\n'
        o += f'        source = _parser.Preprocessor.process_inp(source)\n'
        o += f'        source, comments = _parser.Preprocessor.process_inp_comments(source)\n'
        o += f'        tokens = _parser.Parser(\n'
        o += f'            source.split(" "),\n'
        o += f'            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_SURFACE),\n'
        o += f'        )\n'
        o += f'\n'
        o += f'        if tokens.peekl()[0] == "+":\n'
        o += f'            is_whiteboundary = True\n'
        o += f'            is_reflecting = False\n'
        o += f'            tokens.pushl(tokens.popl()[1:])\n'
        o += f'        elif tokens.peekl()[0] == "*":\n'
        o += f'            is_whiteboundary = False\n'
        o += f'            is_reflecting = True\n'
        o += f'            tokens.pushl(tokens.popl()[1:])\n'
        o += f'        else:\n'
        o += f'            is_whiteboundary = False\n'
        o += f'            is_reflecting = False\n'
        o += f'\n'
        o += f'        number = types.McnpInteger.from_mcnp(tokens.popl())\n'
        o += f'\n'
        o += f'        try:\n'
        o += f'            transform = types.McnpInteger.from_mcnp(tokens.peekl())\n'
        o += f'            tokens.popl()\n'
        o += f'        except Exception:\n'
        o += f'            transform = None\n'
        o += f'\n'
        o += f'        mnemonic = SurfaceMnemonic.from_mcnp(tokens.popl())\n'
        o += f'\n'

        t = []
        for attribute in self.attributes:
            o += f'        {attribute.name} = types.McnpReal.from_mcnp(tokens.popl())\n'
            t.append(attribute.name)

        o += f'\n'
        o += f'        return {self.name}(number, transform, {", ".join(t)}, is_whiteboundary=is_whiteboundary, is_reflecting=is_reflecting)\n'

        if _DEBUG_SURFACE:
            debug_print(o)

        return o


class CellOptionFactory:
    def __init__(self, mnemonic, has_suffix, has_designator, attribute):
        self.name = mnemonic[0].upper() + mnemonic[1:]
        self.mnemonic = mnemonic
        self.enum = mnemonic.upper()
        self.has_suffix = has_suffix
        self.has_designator = has_designator
        self.attribute = attribute

    def build(self):
        o = ''
        o += f'class Cell{self.name}(CellOption):\n'
        o += f'    """\n'
        o += f'    Represents INP cell card {self.mnemonic} options.\n'
        o += f'\n'
        o += f'    ``Cell{self.name}`` implements ``_card.CardOption``.\n'
        o += f'\n'
        o += f'    Attributes:\n'
        o += f'        {self.attribute.name}: {self.attribute.description}\n'

        if self.has_suffix:
            o += f'        suffix: Cell card option suffix.\n'

        if self.has_designator:
            o += f'        designator: Cell card option particle designator.\n'

        o += f'    """\n'
        o += f'\n'

        # CELL.OPTION.__INIT__

        t = []
        t.append(f'{self.attribute.name}: {self.attribute.type}')

        if self.has_suffix:
            t.append(f'suffix: types.McnpInteger')

        if self.has_designator:
            t.append(f'designator: types.Designator')

        o += f'    def __init__(self, {", ".join(t)}):\n'
        o += f'        """\n'
        o += f'        Initializes ``{self.name}``.\n'
        o += f'\n'
        o += f'        Parameters:\n'
        o += f'            {self.attribute.name}: {self.attribute.description}.\n'

        if self.has_suffix:
            o += f'            suffix: Cell card option suffix.\n'

        if self.has_designator:
            o += f'            designator: Cell card option particle designator.\n'

        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSemanticError: INVALID_CELL_OPTION_VALUE.\n'
        o += f'        """\n'
        o += f'\n'

        if self.attribute.restriction:
            o += (
                f'        if {self.attribute.name} is None or not ({self.attribute.restriction}):\n'
            )
        else:
            o += f'        if {self.attribute.name} is None:\n'

        o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_VALUE)\n'
        o += f'\n'

        if self.has_suffix:
            o += f'        if suffix is None:\n'
            o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_SUFFIX)\n'
            o += f'\n'

        if self.has_designator:
            o += f'        if designator is None:\n'
            o += f'            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_CELL_OPTION_DESIGNATOR)\n'
            o += f'\n'

        o += f'        self.keyword: Final[CellKeyword] = CellKeyword.{self.enum}\n'
        o += f'        self.{self.attribute.name}: Final[{self.attribute.type}] = {self.attribute.name}\n'
        o += f'        self.value: Final[{self.attribute.type}] = {self.attribute.name}\n'

        if self.has_suffix:
            o += f'        self.suffix: Final[types.McnpInteger] = suffix\n'

        if self.has_designator:
            o += f'        self.designator: Final[types.Designator] = designator\n'

        o += f'\n'

        # CELL.OPTION.from_mcnp

        o += f'    @staticmethod\n'
        o += f'    def from_mcnp(source: str):\n'
        o += f'        """\n'
        o += f'        Generates ``Cell{self.name}`` objects from INP.\n'
        o += f'\n'
        o += f'        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += f'\n'
        o += f'        Parameters:\n'
        o += f'            source: INP for ``Cell{self.name}``.\n'
        o += f'\n'
        o += f'        Returns:\n'
        o += f'            ``Cell{self.name}`` object.\n'
        o += f'\n'
        o += f'        Raises:\n'
        o += f'            MCNPSyntaxError: TOOFEW_CELL_OPTION, TOOLONG_CELL_OPTION.\n'
        o += f'        """\n'
        o += f'\n'
        o += f'        source = _parser.Preprocessor.process_inp(source)\n'
        o += f'        tokens = _parser.Parser(\n'
        o += f'            re.split(r"=| |:", source),\n'
        o += f'            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_CELL_OPTION),\n'
        o += f'        )\n'
        o += f'\n'

        o += f'        keyword = re.search(r"^[a-zA-Z*]+", tokens.peekl())\n'
        o += f'        keyword = keyword[0] if keyword else ""\n'
        o += f'        if keyword != "{self.mnemonic}":\n'
        o += f'            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.KEYWORD)\n'
        o += f'\n'

        if self.has_suffix:
            o += f'        suffix = types.McnpInteger.from_mcnp(tokens.popl()[{len(self.mnemonic)}:])\n'
        else:
            o += f'        tokens.popl()\n'

        if self.has_designator:
            o += f'        designator = types.Designator.from_mcnp(tokens.popl())\n'

        if self.attribute.type.startswith('tuple'):
            inner_type = self.attribute.type[len('tuple[') : -1]

            if inner_type == 'str':
                o += f'        value = tuple([tokens.popl() for _ in range(0, len(tokens))])\n'
            else:
                o += f'        value = tuple([{inner_type}.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])\n'

        elif self.attribute.type == 'str':
            o += f'        value = tokens.popl()\n'

        else:
            o += f'        value = {self.attribute.type}.from_mcnp(tokens.popl())\n'

        o += f'\n'

        t = []
        t.append('value')

        if self.has_suffix:
            t.append('suffix')

        if self.has_designator:
            t.append('designator')

        o += f'        return Cell{self.name}({", ".join(t)})\n'
        o += f'\n'

        if _DEBUG_CELL:
            debug_print(o)

        return o

    def build_test(self):
        o = ''

        o += f'def test_init_valid(self):\n'

        t = [f'value']

        if self.has_suffix:
            t.append(f'suffix')

        if self.has_designator:
            t.append(f'designator')

        o += f'    for {", ".join(t)} in self.VALID_EXAMPLES:\n'

        if self.attribute.type.startswith('types'):
            o += f'        value = pymcnp.utils.{self.attribute.type}(value)\n'
        elif self.attribute.type == 'str':
            o += f'        value = value\n'
        else:
            o += f'        value = {self.attribute.type}(value)\n'

        if self.has_designator:
            o += f'        designator = pymcnp.utils.types.Designator(designator)\n'

        if self.has_suffix:
            o += f'        suffix = pymcnp.utils.types.McnpInteger(suffix)\n'

        o += f'        obj = pymcnp.inp.Cell{self.name}({", ".join(t)})\n'
        o += f'\n'
        o += f'        assert obj.keyword == pymcnp.inp.CellKeyword.{self.enum}\n'
        o += f'        assert obj.{self.attribute.name} == value\n'
        o += f'        assert obj.value == value\n'
        o += f'\n'
        o += f'def test_init_invalid(self):\n'
        o += f'    for {", ".join(t)} in self.INVALID_EXAMPLES:\n'
        o += f'        with pytest.raises(pymcnp.utils.errors.MCNPSemanticError):\n'

        if self.attribute.type.startswith('types'):
            o += f'            value = pymcnp.utils.{self.attribute.type}(value)\n'
        elif self.attribute.type == 'str':
            o += f'            value = value\n'
        else:
            o += f'            value = {self.attribute.type}(value)\n'

        if self.has_designator:
            o += f'            designator = pymcnp.utils.types.Designator(designator)\n'

        if self.has_suffix:
            o += f'            suffix = pymcnp.utils.types.McnpInteger(suffix)\n'

        o += f'            pymcnp.inp.Cell{self.name}({", ".join(t)})\n'
        o += f'\n'
        o += f'def test_fromMcnp_valid(self):\n'
        o += f'    for {", ".join(t)} in self.VALID_EXAMPLES:\n'

        if self.attribute.type.startswith('types'):
            o += f'        value = pymcnp.utils.{self.attribute.type}(value)\n'
        elif self.attribute.type == 'str':
            o += f'        value = value\n'
        else:
            o += f'        value = {self.attribute.type}(value)\n'

        if self.has_designator:
            o += f'        designator = pymcnp.utils.types.Designator(designator)\n'

        if self.has_suffix:
            o += f'        suffix = pymcnp.utils.types.McnpInteger(suffix)\n'

        if self.attribute.type == 'str':
            q = 'value'
        else:
            q = 'value.to_mcnp()'

        if self.has_suffix and self.has_designator:
            o += f'        obj = pymcnp.inp.Cell{self.name}.from_mcnp(f"{self.mnemonic}{{suffix.to_mcnp()}}:{{designator.to_mcnp()}}={{{q}}}")\n'
        elif self.has_suffix:
            o += f'        obj = pymcnp.inp.Cell{self.name}.from_mcnp(f"{self.mnemonic}{{suffix.to_mcnp()}}={{{q}}}")\n'
        elif self.has_designator:
            o += f'        obj = pymcnp.inp.Cell{self.name}.from_mcnp(f"{self.mnemonic}:{{designator.to_mcnp()}}={{{q}}}")\n'
        else:
            o += f'        obj = pymcnp.inp.Cell{self.name}.from_mcnp(f"{self.mnemonic}={{{q}}}")\n'

        o += f'\n'
        o += f'        assert obj.keyword == pymcnp.inp.CellKeyword.{self.enum}\n'
        o += f'        assert obj.{self.attribute.name} == value\n'
        o += f'        assert obj.value == value\n'
        o += f'\n'
        #        o += f'def test_fromMcnp_invalid(self):\n'
        #        o += f'    for {", ".join(t)} in self.INVALID_EXAMPLES:\n'
        #        o += f'        with pytest.raises(Excpetion):\n'

        #        if self.attribute.type.startswith('types'):
        #            o += f'            value = pymcnp.utils.{self.attribute.type}(value)\n'
        #        elif self.attribute.type == 'str':
        #            o += f'            value = value\n'
        #        else:
        #            o += f'            value = {self.attribute.type}(value)\n'

        #        if self.has_designator:
        #            o += f'            designator = pymcnp.utils.types.Designator(designator)\n'

        #        if self.has_suffix:
        #            o += f'            suffix = pymcnp.utils.types.McnpInteger(suffix)\n'

        #        if self.attribute.type == 'str':
        #            q = 'value'
        #        else:
        #            q = 'value.to_mcnp()'

        #        if self.has_suffix and self.has_designator:
        #            o += f'        obj = pymcnp.inp.Cell{self.name}.from_mcnp(f"{self.mnemonic}{{suffix.to_mcnp()}}:{{designator.to_mcnp()}}={{{q}}}")\n'
        #        elif self.has_suffix:
        #            o += f'        obj = pymcnp.inp.Cell{self.name}.from_mcnp(f"{self.mnemonic}{{suffix.to_mcnp()}}={{{q}}}")\n'
        #        elif self.has_designator:
        #            o += f'        obj = pymcnp.inp.Cell{self.name}.from_mcnp(f"{self.mnemonic}:{{designator.to_mcnp()}}={{{q}}}")\n'
        #        else:
        #            o += f'        obj = pymcnp.inp.Cell{self.name}.from_mcnp(f"{self.mnemonic}={{{q}}}")\n'

        #        o += f'\n'

        if _DEBUG_CELL_TEST:
            debug_print(o)

        return o
