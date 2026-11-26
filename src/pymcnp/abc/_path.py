from __future__ import annotations

import re
import operator

_SEGMENT = re.compile(r'(?P<name>[A-Za-z][A-Za-z0-9_]*)?(?P<indices>(?:\[-?\d+\])*)|(?P<bare>-?\d+)')
_INDEX = re.compile(r'\[(-?\d+)\]')


def _steps(path: str) -> list[tuple[bool, object]]:
    """
    Parses paths into steps, each ``(is_attribute, key)``.

    Accepted syntax: dotted attributes, bracketed integer indices, and bare integer segments, e.g., ``cells[0].j`` and ``options.0.value``. Names starting with an underscore are rejected.

    Raises:
        AttributeError: Invalid paths.
    """

    steps: list[tuple[bool, object]] = []
    for segment in path.split('.'):
        match = _SEGMENT.fullmatch(segment)
        if match is None or not segment:
            raise AttributeError(f'Invalid path {path!r}.')

        if match['bare'] is not None:
            steps.append((False, int(match['bare'])))
            continue

        if match['name'] is not None:
            steps.append((True, match['name']))

        steps.extend((False, int(index)) for index in _INDEX.findall(match['indices']))

    return steps


def _join(steps: list[tuple[bool, object]]) -> str:
    """
    Joins steps, as ``_steps`` returns them, into a path.
    """

    return ''.join(f'.{key}' if is_attribute else f'[{key}]' for is_attribute, key in steps).removeprefix('.')


def _step(obj: object, is_attribute: bool, key: object) -> object:
    if is_attribute:
        return getattr(obj, key)  # type: ignore[arg-type]

    try:
        return operator.getitem(obj, key)  # type: ignore[arg-type]
    except TypeError:
        raise AttributeError(f'{type(obj).__name__!r} object is not subscriptable.') from None


def get_path(obj: object, path: str) -> object:
    """
    Gets values by path, without evaluating code.

    Parameters:
        obj: Object to start from.
        path: Path, e.g., ``cells[0].j`` or ``options.0.value``.

    Returns:
        Value at the path.

    Raises:
        AttributeError: Missing attributes or invalid paths.
        IndexError: Missing indices.
        KeyError: Missing keys.
    """

    for is_attribute, key in _steps(path):
        obj = _step(obj, is_attribute, key)

    return obj


def set_path(obj: object, path: str, value: object) -> None:
    """
    Sets values by path, without evaluating code.

    Parameters:
        obj: Object to start from.
        path: Path, e.g., ``cells[0].j`` or ``options.0.value``.
        value: Value to set.

    Raises:
        AttributeError: Missing attributes or invalid paths.
        IndexError: Missing indices.
        KeyError: Missing keys.
    """

    steps = _steps(path)
    for is_attribute, key in steps[:-1]:
        obj = _step(obj, is_attribute, key)

    is_attribute, key = steps[-1]
    if is_attribute:
        setattr(obj, key, value)  # type: ignore[arg-type]
    else:
        try:
            operator.setitem(obj, key, value)  # type: ignore[arg-type,index]
        except TypeError:
            raise AttributeError(f'{type(obj).__name__!r} object does not support item assignment.') from None
