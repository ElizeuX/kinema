#!/usr/bin/env python3
# vim:fileencoding=utf-8
import os

__license__ = 'GPL v3'
__copyright__ = '2019, Elizeu Xavier <elizeu.xavier at gmail.comt>'

# This file is part of Kinema.

# Kinema is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Kinema is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Kinema.  If not, see <https://www.gnu.org/licenses/>.

#
# Name: ValidateDirectoryWritable Function
#
# Desc: Function that will validate a directory path as 
#           existing and writable.  Used for argument validation only
#
# Input: a directory path string
#  
# Actions: 
#              if valid will return the Directory String
#
#              if invalid it will raise an ArgumentTypeError within argparse
#              which will inturn be reported by argparse to the user
#
def ValidateDirectoryWritable(theDir):

    # Validate the path is a directory
    if not os.path.isdir(theDir):
        raise argparse.ArgumentTypeError('Directory does not exist')

    # Validate the path is writable
    if os.access(theDir, os.W_OK):
        return theDir
    else:
        raise RuntimeError('Directory is not writablee') from error

#End ValidateDirectoryWritable ===================================
