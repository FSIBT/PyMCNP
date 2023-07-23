"""Read an MCNP input file and return block of lines.

1. read all lines
2. replace tabs
3. some error checking
4. remove trailing whitespace
5. merge continuation lines into a single line
6. split into blocks
    a) message block
    b) title
    c) cells
    d) surfaces
    e) data
    f) extra

The blocks are separated by blank lines. The first and last block are optionsl.

See manual 1.3.1: INP files

TODO:
* more error checking
* more special cases, e.g. CONTINUE

"""

from typing import Union
from pathlib import Path
import re

from rich import print

from ..input_line import InputLine


def replace_tab(line: str) -> str:
    """Replaces tabs with spaces.

    Tabs are in multiple of 8 spaces, that means that the character
    after the tab ends up in column 9, 17, 25,...

    """
    while (idx := line.find("\t")) != -1:
        spaces_needed = 8 - (idx % 8)
        line = line.replace("\t", " " * spaces_needed)
    return line


def split_inline_comment(line: str) -> (str, str):
    idx = line.find("$")
    comment = ""
    if idx != -1:
        comment = line[idx + 1 :].strip()
        line = line[:idx]
    return line, comment


def remove_continuation_character(line: str) -> str:
    idx = line.find("&")
    if idx != -1:
        line = line[:idx]
    return line, idx != -1


def remove_duplicate_whitespace(line: str) -> str:
    return " ".join(line.split())


def remove_spaces_around_equal_sign(line: str) -> str:
    return re.sub(r"\s*=\s*", "=", line)


def parse_file(filename: Union[str, Path]) -> dict:
    """Reads in the MCNP input file and parses it.

    Returns a dictionary that has the lines separated by type,
    e.g. title, cells, etc. Comments removed and continuation lines joined.

    Each line will be representated by a InputLine instance that can
    keep track of the content and the inline comment (or the last
    inline commment for multi-line inputs).

    We use a statemeachine to keep track in which section of the input file we
    currently are. This is useful, since for example in the message block
    there are no comment lines starting with "c" allowed.

    """

    MCNP_FILE_START = None
    MCNP_FILE_MESSAGE = "message"
    MCNP_FILE_TITLE = "title"
    MCNP_FILE_CELLS = "cells"
    MCNP_FILE_SURFACES = "surfaces"
    MCNP_FILE_DATA = "data"
    MCNP_FILE_EXTRA = "extra"

    if isinstance(filename, str):
        filename = Path(filename)

    if not filename.is_file():
        print(f"[red]ERROR[/] cannot find file {filename}")

    lines = filename.read_text().split("\n")
    lines = [replace_tab(l) for l in lines]
    # left whitespace will be important for columns 1-5
    lines = [l.rstrip() for l in lines]

    # some error checking
    for i, line in enumerate(lines):
        if len(line) > 80:
            print(f"[orange3]Warning[/] line {i} is longer than 80 characters")

    out = {
        "message": None,
        "title": "",
        "cells": [],
        "surfaces": [],
        "materials": [],
        "data": [],
        "extra": [],
    }

    state = MCNP_FILE_START
    current = ""  # joined multi-lines if applicable
    comment = ""  # last inline comment

    # add an empty line to the input, so that we always can iterate
    # over two lines at a time
    lines.append("")
    for line, next_line in zip(lines[:-1], lines[1:]):
        # ignore comments
        if state not in [MCNP_FILE_START, MCNP_FILE_MESSAGE]:
            if "c " in line.lower()[:5]:
                continue

        if state not in [MCNP_FILE_START, MCNP_FILE_MESSAGE, MCNP_FILE_TITLE]:
            line, comment = split_inline_comment(line)

        if state not in [MCNP_FILE_START, MCNP_FILE_MESSAGE, MCNP_FILE_TITLE]:
            if line.endswith("&"):
                current += " " + line[:-1]
                continue
            if next_line.startswith("     "):
                current += " " + line.strip()
                continue

        line = remove_spaces_around_equal_sign(line)

        if line.lower().startswith("message:") and state == MCNP_FILE_START:
            # start of MESSAGE block
            state = MCNP_FILE_MESSAGE
            line, comment = split_inline_comment(line)
            line, _ = remove_continuation_character(line)
            current += line
        elif line != "" and state == MCNP_FILE_MESSAGE:
            # continuation of MESSAGE block
            line, comment = split_inline_comment(line)
            line, _ = remove_continuation_character(line)
            current += line
        elif (
            (not line.lower().startswith("message:")) and state == MCNP_FILE_START
        ) or state == MCNP_FILE_TITLE:
            # title line
            out[MCNP_FILE_TITLE] = InputLine(line)
            state = MCNP_FILE_CELLS
        elif line == "":
            # end of section
            if state in [MCNP_FILE_MESSAGE]:
                out[state] = InputLine(current, comment)
            current = ""
            comment = ""
            if state == MCNP_FILE_MESSAGE:
                state = MCNP_FILE_TITLE
            elif state == MCNP_FILE_CELLS:
                state = MCNP_FILE_SURFACES
            elif state == MCNP_FILE_SURFACES:
                state = MCNP_FILE_DATA
            elif state == MCNP_FILE_DATA:
                state = MCNP_FILE_EXTRA
        elif state in [
            MCNP_FILE_CELLS,
            MCNP_FILE_SURFACES,
            MCNP_FILE_DATA,
            MCNP_FILE_EXTRA,
        ]:
            # this must be the end of a line in these blocks.
            current += line
            current = remove_duplicate_whitespace(current)
            if (
                (state == MCNP_FILE_DATA)
                and (current.lower()[0] == "m")
                and (current[1] in "0123456789")
            ):
                out["materials"].append(InputLine(current, comment))
            else:
                out[state].append(InputLine(current, comment))
            current = ""
            comment = ""
        else:
            current += line

    return out
