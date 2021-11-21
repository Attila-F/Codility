# -*- coding: utf-8 -*-

def solution(A):
    Apos = [0]
    # Filter for positive integers only
    for elem in A:
        if elem > 0:
            Apos.append(elem)

    # Case: No positive integers in A
    if len(Apos):
        Apos.sort()
    else:
        return 1

    # Case: A has a value gap somewhere
    for i in range(len(Apos)-1):
        if Apos[i+1] - Apos[i] > 1:
            return Apos[i] + 1

    # Case: The solution is larger than max(A)
    return Apos[-1] + 1