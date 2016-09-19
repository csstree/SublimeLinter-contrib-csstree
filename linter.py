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

from SublimeLinter.lint import Linter, util


class CssTree(Linter):
    """Provides an interface to csstree validator."""

    syntax = ('css', 'css3', 'html')
    cmd = 'csstree-validator @ --reporter checkstyle'
    version_args = '--version'
    version_re = r'(?P<version>\d+\.\d+\.\d+)'
    version_requirement = '>= 1.0'
    regex = r'''(?mix)
        line="(?P<line>\d+)".+column="(?P<col>\d+)".+message="(?P<message>[\s\S]+?)(?<!\\)"
    '''
    multiline = True
    error_stream = util.STREAM_BOTH
    tempfile_suffix = 'css'
    selectors = {
        'html': 'source.css.embedded.html'
    }
