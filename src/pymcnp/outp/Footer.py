import typing

from .. import abc


class Footer(abc.Nonterminal):
    """
    Represents footer.

    Attributes:
        preamble: footer ``r' \\*{119}\\n\\n'`` symbol.
        dump_number_preamble: footer ``r' dump no\\. '`` symbol.
        dump_number: footer dump number.
        dump_number_postable: footer ``r' on file runtp.'`` symbol.
        nps_preamble: footer ``r'     nps = '`` symbol.
        nps: footer nps.
        coll_preamble: footer ``r'     coll = '`` symbol.
        coll: footer coll.
        ctm_preamble: footer ``r'     ctm = '`` symbol.
        ctm: footer ctm.
        nrn_preamble: footer ``r'   nrn = *\\n *'`` symbol.
        nrn: footer nrn.
        files_written: footer messages about files written, e.g. ascii PTRAC files.
        warnings_preamble: footer ``r'\\n\\n '`` symbol.
        warnings: footer warnings.
        warnings_postamble: footer ``r' warning messages so far\\.\\n\\n\\n'`` symbol.
        terminated_preamble: footer ``r' run terminated when '`` symbol.
        terminated: footer terminated when.
        run_time_preamble: footer ``r'\\n\\n computer time = '`` symbol.
        run_time: footer run time.
        run_time_postamble: footer ``r' minutes'`` symbol.
        version_preamble: footer ``r'\\n\\n mcnp     version '`` symbol.
        version: footer version.
        date_build: footer date build.
        date_output: footer date output.
        probid_preamble: footer ``r'                     probid =  '`` symbol.
        probid: footer probid.
        newline: footer final newline, if any.
    """

    preamble: typing.Annotated[abc.Terminal, r'\n \*{119}\n\n']
    dump_number_preamble: typing.Annotated[abc.Terminal, r' dump no\. ']
    dump_number: typing.Annotated[abc.Terminal, r'.{4}']
    dump_number_postable: typing.Annotated[abc.Terminal, r' on file runtp.']
    nps_preamble: typing.Annotated[abc.Terminal, r'     nps = ']
    nps: typing.Annotated[abc.Terminal, r'.{11}']
    coll_preamble: typing.Annotated[abc.Terminal, r'     coll = ']
    coll: typing.Annotated[abc.Terminal, r'.{14}']
    ctm_preamble: typing.Annotated[abc.Terminal, r'     ctm = ']
    ctm: typing.Annotated[abc.Terminal, r'.{11}']
    nrn_preamble: typing.Annotated[abc.Terminal, r'   nrn = *\n *']
    nrn: typing.Annotated[abc.Terminal, r'\d+']
    files_written: typing.Annotated[abc.Terminal, r'(?:\n [^\n]* written with [^\n]*\n[^\n]*)*']
    warnings_preamble: typing.Annotated[abc.Terminal, r'\n\n ']
    warnings: typing.Annotated[abc.Terminal, r'.{9}']
    warnings_postamble: typing.Annotated[abc.Terminal, r' warning messages so far\.\n\n\n']
    terminated_preamble: typing.Annotated[abc.Terminal, r' run terminated when ']
    terminated: typing.Annotated[abc.Terminal, r'.+']
    run_time_preamble: typing.Annotated[abc.Terminal, r'\n\n computer time = ']
    run_time: typing.Annotated[abc.Terminal, r' *[0-9.]+']
    run_time_postamble: typing.Annotated[abc.Terminal, r' minutes']
    version_preamble: typing.Annotated[abc.Terminal, r'\n\n mcnp     version ']
    version: typing.Annotated[abc.Terminal, r'.']
    date_build: typing.Annotated[abc.Terminal, r'.{13}']
    date_output: typing.Annotated[abc.Terminal, r'.{38}']
    probid_preamble: typing.Annotated[abc.Terminal, r'                     probid =  ']
    probid: typing.Annotated[abc.Terminal, r'.{18}']
    newline: typing.Annotated[abc.Terminal, r'\n?']
