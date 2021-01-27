#! /usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright © 2016-2020 Cyril Desjouy <cyril.desjouy@univ-lemans.fr>
#
# This file is part of hwc
#
# hwc is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hwc is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with hwc. If not, see <http://www.gnu.org/licenses/>.
#
# Creation Date : 2021-01-27 - 11:39:40
"""
-----------
Help With Choice (HWC)
-----------
"""


import json
import itertools
import numpy as np
import pandas


class Distribute:
    """Find best combination."""

    def __init__(self, file, pmin=None):

        with open(file) as json_file:
            data = json.load(json_file)

        self.names = list(data.keys())
        self.choices = list(data.values())
        self.pmin = pmin

        self.choices = [g[:pmin] if len(g)>pmin else g for g in self.choices]
        self.vassign = [seq for seq in itertools.product(*self.choices)
                        if len(seq) == len(set(seq))]
        self.cassign = [[self.choices[i].index(self.vassign[j][i]) for i in range(len(self.choices))]
                        for j in range(len(self.vassign))]

        print(f'{len(self.vassign)} possibilities found.')

    def get_possibilities(self):
        """Get all possibilities."""
        return self.vassign

    def get_optimal_possibilities(self):
        """Get a list of best possibilities"""
        if self.cassign:
            pertinence = [sum(self.cassign[i]) for i in range(len(self.cassign))]
            best = np.array(self.vassign)[np.array(pertinence) == min(pertinence)]
            return best
        return []

    def display_possibilities(self):
        """Display all possibilities."""
        best = self.get_possibilities()
        print(f'{len(best)} choices:')
        dic = {n: [best[i][j] for i in range(len(best))] for j, n in enumerate(self.names)}
        return pandas.DataFrame(dic)

    def display_optimal_possibilities(self):
        """Display best possibilities."""
        best = self.get_optimal_possibilities()
        print(f'{len(best)} best choices:')
        dic = {n: [best[i][j] for i in range(len(best))] for j, n in enumerate(self.names)}
        return pandas.DataFrame(dic)



if __name__ == "__main__":

    d = Distribute('datatest.json', pmin=3)
    print(d.display_optimal_possibilities())
