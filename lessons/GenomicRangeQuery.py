# -*- coding: utf-8 -*-

IMPACT_FACTOR = {'A': 1,
                 'C': 2,
                 'G': 3,
                 'T': 4}

def get_min_impact(impacts, limit):
    # Iterate through the last occurrences of the 4 impact factors in increasing order
    for i, val in enumerate(impacts):
        # If the impact factor has occurred before the end of the query, return that value.
        if val >= 0 and val <= limit:
            return i+1

    # One of the elements of suf_min[k] == k for each k, therefore a return value is guaranteed.


def solution(S, P, Q):
    # Generate suffix min index array to solve in O(N+M)

    # Starting from the last element of S,
    # store the index of the last occurrence of that impact factor.

    # A running list to track the impact factors
    last_imp_idx = [-1, -1, -1, -1]
    # The suffix list to store the last occurrences
    suf_min = [None] * len(S)

    # Iterate backwards through N nucleoids and store the last index of each nucleoid
    for i in range(len(S), 0, -1):
        # Map the nucleoid character to impact int
        imp = IMPACT_FACTOR[S[i-1]]
        # Set the element corresponding to the current impact value to the current index
        # -1 means that value hasn't been encountered yet.
        last_imp_idx[imp-1] = i-1
        # Store a copy of the array.
        suf_min[i-1] = last_imp_idx.copy()

    # The return array
    ret = [None] * len(P)

    # Iterate through M queries and get the smallest impact factor
    for i in range(len(P)):
        ret[i] = get_min_impact(impacts=suf_min[P[i]], limit=Q[i])

    return ret