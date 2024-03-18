#!/usr/bin/env python3
"""Augment/Function that correct duck-typed annotations
"""

import typing


def safe_first_element(lst: typing.Sequence[typing.Any]) -> \
        typing.Union[typing.Any, None]:
    """Returns duck-typed annotation"""
    if lst:
        return lst[0]
    else:
        return None
