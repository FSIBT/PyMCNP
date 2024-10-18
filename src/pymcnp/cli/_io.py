"""
'_utils'
"""

import datetime


ERROR_INSUFFICENT_ARGS = '\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m Insufficent Arguments.'
ERROR_EXCESSIVE_ARGS = '\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m Excesive Arguments.'
ERROR_UNRECOGNIZED_ARGS = '\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m Unrecognized Arguments.'
ERROR_UNRECOGNIZED_OPTION = '\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m Unrecognized Option.'
ERROR_ALIAS_NOT_FOUND = '\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m INP Alias Not Found.'
ERROR_FILE_NOT_FOUND = '\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m File Not Found.'


def ERROR_INP_VALUE(msg: str) -> str:
    return '\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m INP Syntax Error: ' + msg


def ERROR_INP_SYNTAX(msg: str) -> str:
    return '\x1b[1mpymcnp: \x1b[31mERROR:\x1b[0m INP Value Error: ' + msg


INFO_RUNNING_CQEDITOR = '\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Launching CQ-Editor.'
INFO_RUNNING_MCNP = '\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Launching MCNP.'
INFO_BUILD_INP = '\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built INP.'
INFO_BUILD_CELL = '\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Cell.'
INFO_BUILD_SURFACE = '\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Surface.'
INFO_BUILD_DATUM = '\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Datum.'
INFO_BUILD_TITLE = '\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Title.'
INFO_BUILD_MESSAGE = '\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Message.'
INFO_BUILD_OTHER = '\x1b[1mpymcnp: \x1b[31m\x1b[34mINFO:\x1b[0m Built Other.'


def get_timestamp() -> str:
    return datetime.datetime.today().strftime('%Y-%m-%d--%H-%M-%S')


def error(msg):
    print(msg)
    exit(1)
