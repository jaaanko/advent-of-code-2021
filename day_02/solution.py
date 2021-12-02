UP = 'up'
DOWN = 'down'

def solve_part_1(moves):
    horizontal = depth = 0

    for dr, x in moves:
        if dr == UP:
            depth -= x
        elif dr == DOWN:
            depth += x
        else:
            horizontal += x

    return horizontal * depth

def solve_part_2(moves):
    horizontal = depth = aim = 0

    for dr, x in moves:
        if dr == UP:
            aim -= x 
        elif dr == DOWN:
            aim += x
        else:
            horizontal += x
            depth += aim * x

    return horizontal * depth

if __name__ == '__main__':
    with open('input_01.txt') as f:
        moves = []

        for line in f.readlines():
            dr, x = line.strip().split(' ')
            moves.append((dr, int(x)))

        print(solve_part_1(moves))
        print(solve_part_2(moves))