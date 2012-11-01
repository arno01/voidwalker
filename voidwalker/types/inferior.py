# (void)walker base types
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

from ..utils.decorators import singleton


class Inferior(object):
    def __init__(self, cpu):
        self._cpu = cpu

    def cpu(self):
        return self._cpu


@singleton
class InferiorManager(object):
    def init(self, inferior_factory):
        self._factory = inferior_factory

    def __init__(self):
        self._inferiors = {}
        self._factory = None

    def add_inferior(self, inferior_num, inferior):
        self._inferiors[inferior_num] = inferior

    def inferior(self, inferior_num):
        if inferior_num in self._inferiors:
            return self._inferiors[inferior_num]
        inferior = self._factory.create_inferior(inferior_num)
        self.add_inferior(inferior_num, inferior)
        return inferior
