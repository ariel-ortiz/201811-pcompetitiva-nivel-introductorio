# coding: utf-8

from __future__ import print_function
from __future__ import division

from sys import stdin

entrada = (int(i) for i in stdin.read().split())

T = next(entrada)
for i in range(T):
    N = next(entrada)
    A = []
    for j in range(N):
        A.append(next(entrada))
    O = sorted(A)
    c = 0
    for x, y in zip(A, O):
        if x != y:
            c += 1
    print(c)