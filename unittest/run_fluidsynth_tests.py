#! /usr/bin/env python
"""

================================================================================

	Music theory Python package, test suite
	Copyright (C) 2008, Bart Spaans

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

================================================================================

	Separated fluidsynth tests.

================================================================================

"""

import unittest

import test_fluidsynth

suite = unittest.TestSuite([test_fluidsynth.suite()])

unittest.TextTestRunner(verbosity=2).run(suite)

