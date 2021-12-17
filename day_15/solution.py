from copy import deepcopy
from heapq import heappush, heappop


def increment(matrix):
    new = deepcopy(matrix)
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            new[i][j] += 1

            if new[i][j] == 10:
                new[i][j] = 1

    return new


def flatten_horizontal(tiles):
    new = []

    for i in range(len(tiles[0])):
        new_row = []

        for j in range(len(tiles)):
            new_row.extend(deepcopy(tiles[j][i]))

        new.append(new_row)

    return new


def flatten_vertical(tiles):
    new = []

    for tile in tiles:
        for row in tile:
            new.append(row)

    return new


def find_cheapest_cost(matrix, source, target):
    heap = [(0, source[0], source[1])]
    visited = set()
    best = {}
    m = len(matrix)
    n = len(matrix[0])

    while heap:
        cost, i1, j1 = heappop(heap)

        if (i1, j1) in visited:
            continue

        if (i1, j1) == target:
            return cost

        visited.add((i1, j1))

        for i2, j2 in [(i1-1, j1), (i1+1, j1), (i1, j1-1), (i1, j1+1)]:
            if i2 < 0 or i2 >= m or j2 < 0 or j2 >= n or (i2, j2) in visited:
                continue

            candidate_best = cost + matrix[i2][j2]

            if (i2, j2) not in best or candidate_best < best[i2, j2]:
                best[i2, j2] = candidate_best
                heappush(heap, (candidate_best, i2, j2))

    return float('inf')


def solve_part_1(matrix):
    m = len(matrix)
    n = len(matrix[0])

    return find_cheapest_cost(matrix, (0, 0), (m-1, n-1))


def solve_part_2(matrix):
    full_matrix = []
    horizontal_tile = []
    prev = matrix

    for _ in range(5):
        horizontal_tile = [deepcopy(prev)]
        tmp = prev

        for _ in range(4):
            tmp = increment(tmp)
            horizontal_tile.append(tmp)

        prev = increment(prev)
        full_matrix.append(flatten_horizontal(horizontal_tile))

    full_matrix = flatten_vertical(full_matrix)

    m = len(full_matrix)
    n = len(full_matrix[0])

    return find_cheapest_cost(full_matrix, (0, 0), (m-1, n-1))


if __name__ == '__main__':
    with open('input_01.txt') as f:
        matrix = []

        for line in f.readlines():
            matrix.append([int(x) for x in line.strip()])

        print(solve_part_1(matrix))
        print(solve_part_2(matrix))
