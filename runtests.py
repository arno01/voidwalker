#!/usr/bin/env python

# (void)walker unit tests
# Copyright (C) 2012 David Holm <dholmster@gmail.com>

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import unittest

from voidwalker.interface.parameter import ParameterFactory
from voidwalker.interface.parameter import ParameterManager
from voidwalker.ui.terminal import SysTerminal
from voidwalker.ui.theme import ThemeManager
from voidwalker.utils.decorators import singleton_implementation
import tests


@singleton_implementation(ParameterFactory)
class TestParameterFactory(object):
    def create_parameter(self, parameter_type):
        parameter = parameter_type()
        parameter.value = parameter.default_value()
        return parameter

ParameterManager().init()
terminal = SysTerminal()
ThemeManager().init(terminal.depth())

suite = tests.suite()
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
sys.exit({True: 0, False: 3}[result.wasSuccessful()])
