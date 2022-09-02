#
# linter.py
# Linter for SublimeLinter3, a code checking framework for Sublime Text 3
#
# Written by Sergey Melykov
# Copyright (c) 2016 Sergey Melykov
#
# License: MIT
#

"""This module exports the CssTree plugin class."""

from SublimeLinter.lint import Linter


class CssTree(Linter):
    """Provides an interface to csstree validator."""

    cmd = 'csstree-validator $temp_file --reporter checkstyle'
    tempfile_suffix = 'css'
    defaults = {
        'selector': 'source.css - meta.attribute-with-value',
    }
    regex = r'''(?mix)
        line="(?P<line>\d+)".+column="(?P<col>\d+)".+message="(?P<message>[\s\S]+?)(?<!\\)"
    '''
    multiline = True
