import copy


def moveRight(grid):
    grid = copy.deepcopy(grid)
    done = set()
    m = len(grid)
    n = len(grid[0])
    has_moves = False
    to_replace = set()

    for i in range(m):
        for j in range(n):
            if (i, j) in done:
                continue

            done.add((i, j))

            if grid[i][j] == '>':
                if grid[i][(j+1) % n] != '.':
                    continue

                has_moves = True
                to_replace.add((i, j))
                grid[i][(j+1) % n] = '>'
                done.add((i, j))
                done.add((i, (j+1) % n))

    for i, j in to_replace:
        grid[i][j] = '.'

    return grid, has_moves


def moveDown(grid):
    grid = copy.deepcopy(grid)
    done = set()
    m = len(grid)
    n = len(grid[0])
    has_moves = False
    to_replace = set()

    for i in range(m):
        for j in range(n):
            if (i, j) in done:
                continue

            done.add((i, j))

            if grid[i][j] == 'v':
                if grid[(i+1) % m][j] != '.':
                    continue

                has_moves = True
                to_replace.add((i, j))
                grid[(i+1) % m][j] = 'v'
                done.add(((i+1) % m, j))

    for i, j in to_replace:
        grid[i][j] = '.'

    return grid, has_moves


def solve_part_1(grid):
    steps = 0
    has_moves_right = has_moves_down = True

    while has_moves_right or has_moves_down:
        grid, has_moves_right = moveRight(grid)
        grid, has_moves_down = moveDown(grid)
        steps += 1

    return steps


if __name__ == '__main__':
    with open('input_01.txt') as f:
        grid = [list(line.strip()) for line in f.readlines()]
        print(solve_part_1(grid))
