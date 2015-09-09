#!/usr/bin/env python
# -*- coding: utf-8 -*-
#copyRight by heibanke

import itertools

horses=[1,2,3,4]
races = itertools.permutations(horses)

a=itertools.product([1,2],[3,4])
b=itertools.repeat([1,2],4)

c=itertools.chain(races, a, b)

print [i for i in c]
