#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os


def abs_path(p: str) -> str:
    """
    return the absolute path of a relative path
    """
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), p)
