"""
Contains classes for building classes for ``inp``.
"""

_DEBUG_DATA = False
_DEBUG_CELL = False
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
        o += '    """\n'
        o += f'    Represents INP {self.mnemonic} data cards.\n'
        o += '\n'
        o += f'    ``{self.name}`` implements ``Data``.\n'
        o += '\n'
        o += '    Attributes:\n'

        for attribute in self.attributes:
            o += f'        {attribute.name}: {attribute.description}.\n'

        if self.has_suffix:
            o += '        suffix: card suffix.\n'

        if self.has_designator:
            o += '        designator: card designator.\n'

        o += '    """\n'
        o += '\n'

        # DATA.__init__

        t = []
        for attribute in self.attributes:
            t.append(f'{attribute.name}: {attribute.type}')

        if self.has_suffix:
            t.append('suffix: types.McnpInteger')

        if self.has_designator:
            t.append('designator: types.Designator')

        o += f'    def __init__(self, {", ".join(t)}):\n'
        o += '        """\n'
        o += f'        Initializes ``{self.name}``.\n'
        o += '\n'
        o += '        Parameters:\n'

        for attribute in self.attributes:
            o += f'            {attribute.name}: {attribute.description}.\n'

        if self.has_suffix:
            o += '            suffix: card suffix.\n'

        if self.has_designator:
            o += '            designator: card designator.\n'

        o += '\n'
        o += '        Raises:\n'
        o += '            McnpError: INVALID_DATUM_PARAMETERS.\n'
        o += '        """\n'
        o += '\n'

        for attribute in self.attributes:
            if attribute.restriction:
                o += f'        if {attribute.name} is None or not ({attribute.restriction}):\n'
            else:
                o += f'        if {attribute.name} is None:\n'

            o += f'            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str({attribute.name}))\n'

            if attribute.type.startswith('tuple'):
                o += '\n'
                o += f'        for entry in {attribute.name}:\n'

                if attribute.restriction:
                    o += f'            if entry is None or not ({attribute.restriction}):\n'
                else:
                    o += '            if entry is None:\n'

                o += f'                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str({attribute.name}))\n'

            o += '\n'

        if self.has_suffix:
            o += '        if suffix is None:\n'
            o += '            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_SUFFIX, str(suffix))\n'
            o += '\n'

        if self.has_designator:
            o += '        if designator is None:\n'
            o += '            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_DESIGNATOR, str(designator))\n'
            o += '\n'

        o += f'        self.mnemonic: Final[DataMnemonic] = DataMnemonic.{self.enum}\n'

        t = []
        for attribute in self.attributes:
            if attribute.type.startswith('tuple'):
                t.append(f'list({attribute.name})')
            else:
                t.append(f'[{attribute.name}]')

        o += f'        self.parameters: Final[tuple[any]] = tuple({" + ".join(t)})\n'

        if self.has_suffix:
            o += '        self.suffix: Final[types.McnpInteger] = suffix\n'

        if self.has_designator:
            o += '        self.designator: Final[types.Designator] = designator\n'

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

        o += '\n'

        # DATA.from_mcnp

        o += '    @staticmethod\n'
        o += '    def from_mcnp(source: str):\n'
        o += '        """\n'
        o += f'        Generates ``{self.name}`` objects from INP.\n'
        o += '\n'
        o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += '\n'
        o += '        Parameters:\n'
        o += f'            source: INP for {self.mnemonic} data cards.\n'
        o += '\n'
        o += '        Returns:\n'
        o += f'            ``{self.name}`` object.\n'
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
        o += f'        if mnemonic != "{self.mnemonic}":\n'
        o += '            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)\n'
        o += '\n'

        if self.has_suffix:
            o += f'        suffix = types.McnpInteger.from_mcnp(tokens.popl()[{len(self.mnemonic)}:])\n'
        else:
            o += '        tokens.popl()\n'

        if self.has_designator:
            o += '        designator = types.Designator.from_mcnp(tokens.popl())\n'

        o += '\n'

        for attribute in self.attributes:
            if attribute.type.endswith('Option]'):
                # tuple[...Option]

                o += f'        {attribute.name} = {{}}\n'
                o += f'        keywords = re.findall(r"{'|'.join([option.mnemonic for option in self.options])}", " ".join(tokens.deque))\n'
                o += f'        values = re.split(r"{'|'.join([option.mnemonic for option in self.options])}", " ".join(tokens.deque))[1:]\n'
                o += '        for keyword, value in zip(keywords, values):\n'
                o += '            match keyword:\n'

                for option in self.options:
                    o += f'                case "{option.mnemonic}":\n'
                    o += f'                    {attribute.name}["{option.mnemonic}"] = {self.name}{option.name}.from_mcnp(f"{{keyword}}={{value}}")\n'

                o += '\n'

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

        o += '\n'

        t = []
        for attribute in self.attributes:
            t.append(f'{attribute.name}')

        if self.has_suffix:
            t.append('suffix = suffix')

        if self.has_designator:
            t.append('designator = designator')

        o += f'        data = {self.name}({", ".join(t)})\n'
        o += '        data.comment = comments\n'
        o += '\n'
        o += '        return data\n'
        o += '\n'

        # DATA.to_mcnp

        o += '    def to_mcnp(self) -> str:\n'
        o += '        """\n'
        o += f'        Generates INP from ``{self.name}`` objects.\n'
        o += '\n'
        o += '        ``to_mcnp`` translates from PyMCNP to INP.\n'
        o += '\n'
        o += '        Returns:\n'
        o += f'            INP for ``{self.name}``.\n'
        o += '        """\n'
        o += '\n'

        if self.has_suffix and self.has_designator:
            o += '        return _parser.Postprocessor.add_continuation_lines(f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()}:{self.designator.to_mcnp()}'
        elif self.has_designator:
            o += '        return _parser.Postprocessor.add_continuation_lines(f"{self.mnemonic.to_mcnp()}:{self.designator.to_mcnp()}'
        elif self.has_suffix:
            o += '        return _parser.Postprocessor.add_continuation_lines(f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()}'
        else:
            o += '        return _parser.Postprocessor.add_continuation_lines(f"{self.mnemonic.to_mcnp()}'

        for attribute in self.attributes:
            if attribute.type.startswith('tuple'):
                o += f' {{" ".join(entry.to_mcnp() for entry in self.{attribute.name})}}'
            elif attribute.type.startswith('dict'):
                o += f' {{" ".join(entry.to_mcnp() for entry in self.{attribute.name}.values())}}'
            else:
                o += f' {{self.{attribute.name}.to_mcnp()}}'

        o += '")\n'
        o += '\n'

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
        o += '    """\n'
        o += f'    Represents INP {self.mnemonic} data card entry.\n'
        o += '\n'
        o += f'    ``{self.name}Entry`` implements ``DataEntry``\n.'
        o += '\n'
        o += '    Attributes:\n'

        for attribute in self.attributes:
            o += f'            {attribute.name}: {attribute.description}.\n'

        o += '    """\n'
        o += '\n'

        t = []
        for attribute in self.attributes:
            t.append(f'{attribute.name}: {attribute.type}')

        # DATA.ENTRY.__init__

        o += f'    def __init__(self, {", ".join(t)}):\n'
        o += '        """\n'
        o += f'        Initializes ``{self.name}Entry``.\n'
        o += '\n'
        o += '        Parameters:\n'

        for attribute in self.attributes:
            o += f'                {attribute.name}: {attribute.description}.\n'

        o += '\n'
        o += '        Raises:\n'
        o += '            McnpError: INVALID_DATUM_PARAMETERS.\n'
        o += '        """\n'
        o += '\n'

        for attribute in self.attributes:
            o += f'        if {attribute.name} is None:\n'
            o += '            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)\n'

            if attribute.type.startswith('tuple'):
                o += '\n'
                o += f'        for entry in {attribute.name}:\n'

                if attribute.restriction:
                    o += f'            if entry is None or not ({attribute.restriction}):\n'
                else:
                    o += '            if entry is None:\n'

                o += '                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)\n'

            o += '\n'

        for attribute in self.attributes:
            o += f'        self.{attribute.name}: Final[{attribute.type}] = {attribute.name}\n'

        o += '\n'

        # DATA.ENTRY.from_mcnp

        o += '    @staticmethod\n'
        o += '    def from_mcnp(source: str):\n'
        o += '        """\n'
        o += f'        Generates ``{self.name}Entry`` objects from INP.\n'
        o += '\n'
        o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += '\n'
        o += '        Parameters:\n'
        o += f'            source: INP for ``{self.name}Entry``.\n'
        o += '\n'
        o += '        Returns:\n'
        o += f'            ``{self.name}Entry`` object.\n'
        o += '\n'
        o += '        Raises:\n'
        o += '            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.\n'
        o += '        """\n'
        o += '\n'
        o += '        source = _parser.Preprocessor.process_inp(source)\n'
        o += '        tokens = _parser.Parser(source.split(" "), errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source))\n'
        o += '\n'

        for attribute in self.attributes:
            if attribute.type != 'str':
                o += f'        {attribute.name} = {attribute.type}.from_mcnp(tokens.popl())\n'
            else:
                o += f'        {attribute.name} = tokens.popl()\n'

        o += '\n'
        o += '        if tokens:\n'
        o += '           raise errors.McnpError(errors.McnpCode.UNEXPECTED_TOKEN)\n'
        o += '\n'

        t = []
        for attribute in self.attributes:
            t.append(f'{attribute.name}')

        o += f'        return {self.name}Entry({", ".join(t)})\n'
        o += '\n'

        # DATA.ENTRY.to_mcnp

        o += '\n'
        o += '    def to_mcnp(self):\n'
        o += '        """\n'
        o += f'        Generates INP from ``{self.name}Entry`` objects.\n'
        o += '\n'
        o += '        ``to_mcnp`` translates from PyMCNP to INP.\n'
        o += '\n'
        o += '        Returns:\n'
        o += f'            INP for ``{self.name}Entry``.\n'
        o += '        """\n'
        o += '\n'

        t = []
        for attribute in self.attributes:
            if attribute.type != 'str':
                t.append(f'{{self.{attribute.name}.to_mcnp()}}')
            else:
                t.append(f'{{self.{attribute.name}}}')

        o += f'        return f"{" ".join(t)}"\n'
        o += '\n'

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
        o += '    """\n'
        o += f'    Represents INP {self.mnemonic} data card option keywords.\n'
        o += '\n'
        o += f'    ``{self.name}Keyword`` implements ``DataKeyword``\n.'
        o += '    """\n'

        for option in self.options:
            o += f'    {option.enum} = "{option.mnemonic}"\n'

        o += '\n'

        # DATA.KEYWORD.from_mcnp

        o += '    @staticmethod\n'
        o += '    def from_mcnp(source: str):\n'
        o += '        """\n'
        o += f'        Generates ``{self.name}Keyword`` objects from INP.\n'
        o += '\n'
        o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += '\n'
        o += '        Parameters:\n'
        o += f'            source: INP for ``{self.name}Keyword``.\n'
        o += '\n'
        o += '        Returns:\n'
        o += f'            ``{self.name}Keyword`` object.\n'
        o += '\n'
        o += '        Raises:\n'
        o += '            McnpError: INVALID_DATUM_KEYWORD.\n'
        o += '        """\n'
        o += '\n'
        o += '        source = _parser.Preprocessor.process_inp(source)\n'
        o += '\n'
        o += '        try:\n'
        o += f'            return {self.name}Keyword\n'
        o += '        except:\n'
        o += '            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)\n'
        o += '\n'

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
        o += '    """\n'
        o += f'    ``{name}{self.name}`` represents INP {mnemonic} data card {self.mnemonic} options.\n'
        o += '\n'
        o += f'    ``{name}{self.name}`` implements ``DataOption``\n.'
        o += '\n'
        o += '    Attributes:\n'
        o += f'        {self.attribute.name}: {self.attribute.description}.\n'
        o += '    """\n'
        o += '\n'

        # DATA.OPTION.__init__

        o += f'    def __init__(self, {self.attribute.name}: {self.attribute.type}):\n'
        o += '        """\n'
        o += f'        Initializes ``{name}{self.name}``.\n'
        o += '\n'
        o += '        Parameters:\n'
        o += f'            {self.attribute.name}: {self.attribute.description}.\n'
        o += '\n'
        o += '        Raises:\n'
        o += '            McnpError: INVALID_DATUM_VALUE.\n'
        o += '        """\n'
        o += '\n'

        o += f'        if {self.attribute.name} is None:\n'
        o += '            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)\n'

        if self.attribute.type.startswith('tuple'):
            o += f'        for entry in {self.attribute.name}:\n'

            if self.attribute.restriction:
                o += f'            if entry is None or not ({self.attribute.restriction}):\n'
            else:
                o += '            if entry is None:\n'

            o += f'                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str({self.attribute.name}))\n'

        o += '\n'

        o += f'        self.keyword: Final[{name}Keyword] = {name}Keyword.{self.enum}\n'
        o += f'        self.value: Final[{self.attribute.type}] = {self.attribute.name}\n'
        o += f'        self.{self.attribute.name}: Final[{self.attribute.type}] = {self.attribute.name}\n'
        o += '\n'

        # DATA.OPTION.from_mcnp

        o += '    @staticmethod\n'
        o += '    def from_mcnp(source: str):\n'
        o += '        """\n'
        o += f'        Generates ``{name}{self.name}`` objects from INP.\n'
        o += '\n'
        o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += '\n'
        o += '        Parameters:\n'
        o += f'            source: INP for ``{name}{self.name}``.\n'
        o += '\n'
        o += '        Returns:\n'
        o += f'            ``{name}{self.name}`` object.\n'
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
        o += f'        keyword = {name}Keyword.from_mcnp(tokens.popl())\n'

        if self.attribute.type.startswith('tuple'):
            inner_type = self.attribute.type[len('tuple[') : -1]

            if inner_type == 'str':
                o += '        value = tuple([tokens.popl() for _ in range(0, len(tokens))])\n'
            else:
                o += f'        value = tuple([{inner_type}.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])\n'

        elif self.attribute.type == 'str':
            o += '        value = tokens.popl()\n'

        else:
            o += f'        value = {self.attribute.type}.from_mcnp(tokens.popl())\n'

        o += '\n'
        o += f'        return {name}{self.name}(value)\n'
        o += '\n'

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
        o += '    """\n'
        o += f'    Represents INP {self.mnemonic} surface cards.\n'
        o += '\n'
        o += f'    ``{self.name}`` implements ``Surface``\n.'
        o += '\n'
        o += '    Attributes:\n'

        for attribute in self.attributes:
            o += f'        {attribute.name}: {attribute.description}.\n'

        o += '    """\n'
        o += '\n'

        # SURFACE.__init__

        t = []
        for attribute in self.attributes:
            t.append(f'{attribute.name}: {attribute.type}')

        o += f'    def __init__(self, number: types.McnpInteger, transform: types.McnpInteger, {", ".join(t)}, is_whiteboundary: bool = False, is_reflecting: bool = False):\n'
        o += '        """\n'
        o += f'        Initializes ``{self.name}``.\n'
        o += '\n'
        o += '\n'
        o += '        Parameters:\n'

        for attribute in self.attributes:
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

        for attribute in self.attributes:
            o += f'        if {attribute.name} is None:\n'
            o += f'            raise errors.McnpError(errors.McnpCode.INVALID_SURFACE_PARAMETER, str({attribute.name}))\n'
            o += '\n'

        o += '        self.ident: Final[int] =  number.value\n'
        o += '        self.number: Final[types.McnpInteger] = number\n'
        o += f'        self.mnemonic: Final[SurfaceMnemonic] = SurfaceMnemonic.{self.enum}\n'
        o += '        self.transform: Final[types.McnpInteger] = transform\n'
        o += '        self.is_reflecting: Final[bool] = is_reflecting\n'
        o += '        self.is_whiteboundary: Final[bool] = is_whiteboundary\n'
        o += '\n'

        t = []
        for attribute in self.attributes:
            o += f'        self.{attribute.name}: Final[types.McnpReal] = {attribute.name}\n'
            t.append(f'{attribute.name}')

        o += f'        self.parameters: Final[tuple[types.McnpReal]] = tuple([{", ".join(t)}])\n'
        o += '\n'

        # SURFACE.from_mcnp

        o += '    @staticmethod\n'
        o += '    def from_mcnp(source: str):\n'
        o += '        """\n'
        o += f'        Generates ``{self.name}`` objects from INP.\n'
        o += '\n'
        o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += '\n'
        o += '        Parameters:\n'
        o += '            source: INP for surface.\n'
        o += '\n'
        o += '        Returns:\n'
        o += f'            ``{self.name}`` object.\n'
        o += '\n'
        o += '        Raises:\n'
        o += '            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.\n'
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
        o += '        mnemonic = SurfaceMnemonic.from_mcnp(tokens.popl())\n'
        o += '\n'

        t = []
        for attribute in self.attributes:
            o += f'        {attribute.name} = types.McnpReal.from_mcnp(tokens.popl())\n'
            t.append(attribute.name)

        o += '\n'
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
        o += '    """\n'
        o += f'    Represents INP cell card {self.mnemonic} options.\n'
        o += '\n'
        o += f'    ``Cell{self.name}`` implements ``_card.CardOption``.\n'
        o += '\n'
        o += '    Attributes:\n'
        o += f'        {self.attribute.name}: {self.attribute.description}\n'

        if self.has_suffix:
            o += '        suffix: Cell card option suffix.\n'

        if self.has_designator:
            o += '        designator: Cell card option particle designator.\n'

        o += '    """\n'
        o += '\n'

        # CELL.OPTION.__INIT__

        t = []
        t.append(f'{self.attribute.name}: {self.attribute.type}')

        if self.has_suffix:
            t.append('suffix: types.McnpInteger')

        if self.has_designator:
            t.append('designator: types.Designator')

        o += f'    def __init__(self, {", ".join(t)}):\n'
        o += '        """\n'
        o += f'        Initializes ``{self.name}``.\n'
        o += '\n'
        o += '        Parameters:\n'
        o += f'            {self.attribute.name}: {self.attribute.description}.\n'

        if self.has_suffix:
            o += '            suffix: Cell card option suffix.\n'

        if self.has_designator:
            o += '            designator: Cell card option particle designator.\n'

        o += '\n'
        o += '        Raises:\n'
        o += '            McnpError: INVALID_CELL_OPTION_VALUE.\n'
        o += '        """\n'
        o += '\n'

        if self.attribute.restriction:
            o += (
                f'        if {self.attribute.name} is None or not ({self.attribute.restriction}):\n'
            )
        else:
            o += f'        if {self.attribute.name} is None:\n'

        o += f'            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_VALUE, str({self.attribute.name}))\n'
        o += '\n'

        if self.has_suffix:
            o += '        if suffix is None:\n'
            o += '            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_SUFFIX, str(suffix))\n'
            o += '\n'

        if self.has_designator:
            o += '        if designator is None:\n'
            o += '            raise errors.McnpError(errors.McnpCode.INVALID_CELL_OPTION_DESIGNATOR, str(designator))\n'
            o += '\n'

        o += f'        self.keyword: Final[CellKeyword] = CellKeyword.{self.enum}\n'
        o += f'        self.{self.attribute.name}: Final[{self.attribute.type}] = {self.attribute.name}\n'
        o += f'        self.value: Final[{self.attribute.type}] = {self.attribute.name}\n'

        if self.has_suffix:
            o += '        self.suffix: Final[types.McnpInteger] = suffix\n'

        if self.has_designator:
            o += '        self.designator: Final[types.Designator] = designator\n'

        o += '\n'

        # CELL.OPTION.from_mcnp

        o += '    @staticmethod\n'
        o += '    def from_mcnp(source: str):\n'
        o += '        """\n'
        o += f'        Generates ``Cell{self.name}`` objects from INP.\n'
        o += '\n'
        o += '        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.\n'
        o += '\n'
        o += '        Parameters:\n'
        o += f'            source: INP for ``Cell{self.name}``.\n'
        o += '\n'
        o += '        Returns:\n'
        o += f'            ``Cell{self.name}`` object.\n'
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
        o += f'        if keyword != "{self.mnemonic}":\n'
        o += '            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, str(keyword))\n'
        o += '\n'

        if self.has_suffix:
            o += f'        suffix = types.McnpInteger.from_mcnp(tokens.popl()[{len(self.mnemonic)}:])\n'
        else:
            o += '        tokens.popl()\n'

        if self.has_designator:
            o += '        designator = types.Designator.from_mcnp(tokens.popl())\n'

        if self.attribute.type.startswith('tuple'):
            inner_type = self.attribute.type[len('tuple[') : -1]

            if inner_type == 'str':
                o += '        value = tuple([tokens.popl() for _ in range(0, len(tokens))])\n'
            else:
                o += f'        value = tuple([{inner_type}.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])\n'

        elif self.attribute.type == 'str':
            o += '        value = tokens.popl()\n'

        else:
            o += f'        value = {self.attribute.type}.from_mcnp(tokens.popl())\n'

        o += '\n'

        t = []
        t.append('value')

        if self.has_suffix:
            t.append('suffix')

        if self.has_designator:
            t.append('designator')

        o += f'        return Cell{self.name}({", ".join(t)})\n'
        o += '\n'

        if _DEBUG_CELL:
            debug_print(o)

        return o

    def build_test(self):
        o = ''

        o += 'def test_init_valid(self):\n'

        t = ['value']

        if self.has_suffix:
            t.append('suffix')

        if self.has_designator:
            t.append('designator')

        o += f'    for {", ".join(t)} in self.VALID_EXAMPLES:\n'

        if self.attribute.type.startswith('types'):
            o += f'        value = pymcnp.utils.{self.attribute.type}(value)\n'
        elif self.attribute.type == 'str':
            o += '        value = value\n'
        else:
            o += f'        value = {self.attribute.type}(value)\n'

        if self.has_designator:
            o += '        designator = pymcnp.utils.types.Designator(designator)\n'

        if self.has_suffix:
            o += '        suffix = pymcnp.utils.types.McnpInteger(suffix)\n'

        o += f'        obj = pymcnp.inp.Cell{self.name}({", ".join(t)})\n'
        o += '\n'
        o += f'        assert obj.keyword == pymcnp.inp.CellKeyword.{self.enum}\n'
        o += f'        assert obj.{self.attribute.name} == value\n'
        o += '        assert obj.value == value\n'
        o += '\n'
        o += 'def test_init_invalid(self):\n'
        o += f'    for {", ".join(t)} in self.INVALID_EXAMPLES:\n'
        o += '        with pytest.raises(pymcnp.utils.errors.McnpError):\n'

        if self.attribute.type.startswith('types'):
            o += f'            value = pymcnp.utils.{self.attribute.type}(value)\n'
        elif self.attribute.type == 'str':
            o += '            value = value\n'
        else:
            o += f'            value = {self.attribute.type}(value)\n'

        if self.has_designator:
            o += '            designator = pymcnp.utils.types.Designator(designator)\n'

        if self.has_suffix:
            o += '            suffix = pymcnp.utils.types.McnpInteger(suffix)\n'

        o += f'            pymcnp.inp.Cell{self.name}({", ".join(t)})\n'
        o += '\n'
        o += 'def test_fromMcnp_valid(self):\n'
        o += f'    for {", ".join(t)} in self.VALID_EXAMPLES:\n'

        if self.attribute.type.startswith('types'):
            o += f'        value = pymcnp.utils.{self.attribute.type}(value)\n'
        elif self.attribute.type == 'str':
            o += '        value = value\n'
        else:
            o += f'        value = {self.attribute.type}(value)\n'

        if self.has_designator:
            o += '        designator = pymcnp.utils.types.Designator(designator)\n'

        if self.has_suffix:
            o += '        suffix = pymcnp.utils.types.McnpInteger(suffix)\n'

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

        o += '\n'
        o += f'        assert obj.keyword == pymcnp.inp.CellKeyword.{self.enum}\n'
        o += f'        assert obj.{self.attribute.name} == value\n'
        o += '        assert obj.value == value\n'
        o += '\n'
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
