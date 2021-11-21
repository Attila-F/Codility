
def solution(A):
    west_sum = 0
    east_sum = 0
    # Iterate through the array right to left
    for j in range(len(A)):
        if A[-(j + 1)] == 1:  # west passing
            west_sum += 1
        else:  # east passing
            east_sum += west_sum  # add the current sum of west passing cars
        if east_sum > 1e9:  # return -1 if the number of pairs of passing cars exceeds 1,000,000,000
            return -1

    return east_sum