from itertools import combinations


def find_number_pairs(numbers, N=10):
    return [(x, y) for x, y in combinations(numbers, 2) if x + y == N]
