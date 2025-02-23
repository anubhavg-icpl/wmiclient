#! /usr/bin/env python
###########################################################################
#
# This program is part of Zenoss Core, an open source monitoring platform.
# Copyright (C) 2008-2010, Zenoss Inc.
#
# This program is free software; you can redistribute it and/or modify it
# under the terms of the GNU General Public License version 2, or (at your
# option) any later version, as published by the Free Software Foundation.
#
# For complete information please visit: http://www.zenoss.com/oss/
#
###########################################################################
import sys
import os

try:
    import version
    version = version.VERSION
except ImportError:
    version = '.'.join(map(str, sys.version_info[:2]))

if len(sys.argv) > 1:
    version = sys.argv[1]

# Make compatible with both Python 2 and 3
if sys.version_info[0] >= 3:
    print(os.path.join(sys.prefix, 'include', 'python' + version))
else:
    print os.path.join(sys.prefix, 'include', 'python' + version)

