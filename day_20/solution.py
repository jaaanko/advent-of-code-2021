from collections import Counter
from copy import copy


def generate_row(i, j, dirs, image, border_pixel):
    row = []

    for di, dj in dirs:
        ni = di + i
        nj = dj + j

        if (ni, nj) not in image:
            row.append(border_pixel)
        else:
            row.append(image[ni, nj])

    return row


def pixels_to_decimal(pixels):
    binary = ['0' if pixel == '.' else '1' for pixel in pixels]
    return int(''.join(binary), 2)


def add_layer(image, border_pixel):
    new = copy(image)
    min_m = min_n = float('inf')
    max_m = max_n = float('-inf')

    for i, j in image:
        min_m = min(min_m, i)
        min_n = min(min_n, j)

        max_m = max(max_m, i)
        max_n = max(max_n, j)

    for j in range(min_n, max_n+1):
        new[min_m-1, j] = border_pixel
        new[max_m+1, j] = border_pixel

    for i in range(min_m, max_m+1):
        new[i, min_n-1] = border_pixel
        new[i, max_n+1] = border_pixel

    # top left
    new[min_m-1, min_n-1] = border_pixel

    # top right
    new[min_m-1, max_n+1] = border_pixel

    # bottom left
    new[max_m+1, min_n-1] = border_pixel

    # bottom right
    new[max_m+1, max_n+1] = border_pixel

    return new


def enhance(algorithm, image, border_pixel):
    enhanced = {}
    top_dirs = [(-1, -1), (-1, 0), (-1, 1)]
    mid_dirs = [(0, -1), (0, 0), (0, 1)]
    bot_dirs = [(1, -1), (1, 0), (1, 1)]

    for i, j in image:
        pixels = []

        for dirs in [top_dirs, mid_dirs, bot_dirs]:
            pixels.extend(generate_row(i, j, dirs, image, border_pixel))

        enhanced[i, j] = algorithm[pixels_to_decimal(pixels)]

    return enhanced


def solve_part_1(algorithm, image, steps):
    for i in range(steps):
        border_pixel = '.' if i % 2 == 0 else algorithm[0]
        image = add_layer(image, border_pixel)
        image = enhance(algorithm, image, border_pixel)

    return Counter(image.values())['#']


def solve_part_2(algorithm, image, steps):
    return solve_part_1(algorithm, image, steps)


if __name__ == '__main__':
    with open('input_01.txt') as f:
        algorithm, grid = f.read().split('\n\n')
        algorithm = ''.join([line for line in algorithm.split('\n')])
        grid = [line for line in grid.split('\n')]

        image = {}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                image[i, j] = grid[i][j]

        print(solve_part_1(algorithm, image, 2))
        print(solve_part_2(algorithm, image, 50))
