
"""
$Id$
$URL$

Copyright (C) 2004 Matteo Merli <matteo.merli@gmail.com>

This code is licenced under the GPL. See LICENSE file.
"""

## Here is defined the program version

major = 0
middle = 2
minor = None
extra = 'svn'

######################################

# Automized version string
string = "%u.%u" % (major, middle)
if minor is not None: string += '.%u' % minor
if type(extra) is str: string += '-%s' % extra


