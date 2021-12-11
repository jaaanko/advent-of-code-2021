from collections import deque
from copy import deepcopy

def increase_energy(matrix):
    m = len(matrix)
    n = len(matrix[0])

    for i in range(m):
        for j in range(n):
            matrix[i][j] += 1
    
def flash(matrix):
    res = 0
    m = len(matrix)
    n = len(matrix[0])

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    flashed = set()
    queue = deque()

    for i in range(m):
        for j in range(n):
            if matrix[i][j] > 9:
                queue.append((i, j))
                flashed.add((i, j))

    while queue:
        i,j = queue.popleft()
        res += 1

        for di,dj in directions:
            ni = di + i
            nj = dj + j

            if ni < 0 or ni >= m or nj < 0 or nj >= n or (ni, nj) in flashed:
                continue
            
            matrix[ni][nj] += 1

            if matrix[ni][nj] > 9:
                flashed.add((ni, nj))
                queue.append((ni, nj))
        
    for i,j in flashed:
        matrix[i][j] = 0

    return res

def solve_part_1(matrix, steps):
    res = 0
    
    for _ in range(steps):
        increase_energy(matrix)
        res += flash(matrix)

    return res

def solve_part_2(matrix):
    m = len(matrix)
    n = len(matrix[0])
    steps = flashes = 0

    while flashes != m * n:
        increase_energy(matrix)
        flashes = flash(matrix)
        steps += 1

    return steps

if __name__ == '__main__':
    with open('input_01.txt') as f:
        matrix = []

        for line in f.readlines():
            matrix.append([int(x) for x in line.strip()])

        print(solve_part_1(deepcopy(matrix), 100))
        print(solve_part_2(deepcopy(matrix)))